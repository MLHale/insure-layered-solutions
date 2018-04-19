import sys
import argparse
import requests
import re
import traceback
import datetime
import json
from bs4 import BeautifulSoup
from time import mktime


#Class to store relevant information about the vulnerbility.
class vulnObject:

    numVulns = 0

    #Init method
    def __init__(self, vulnID, debug):
        self.vulnID = vulnID #CVE.org Vuln ID
        self.search_url ='' #search URL that obtianed the info
        self.cveID = '' #Relevant CVE ID, if any
        self.datePublic = 0.0 #Date that the vuln went public
        self.dateFirstPublished = 0.0 #Date vuln was first published in database
        self.dateLastUpdated = 0.0 #Date vuln we last updated in database
        self.severityMetric = 0.0 #Severith metric associated with the vuln
        self.documentRevision = 0.0 #Document revision
        self.debug = debug #Flag to set debug mode on or off

        vulnObject.numVulns +=1

    #Function to convert the Gregorian calander dates to UNIX Epoch dates
    def convertDate2Epoch(self, days, month, year, debug):
        self.debug = debug

        try:
            date_obj = datetime.date(int(year), int(month), int(days))
            timestamp = mktime(date_obj.timetuple())

        except Exception as e:
            if self.debug:
                print('Error: date info below')
                print(days, month, year)
                print (timestamp)
                print (datetime.datetime.fromtimestamp(timestamp))
                print()

            return e

        return timestamp

    #Functions below are used to set the elements of the object
    def setSearchURL(self, search_url):
        self.search_url = search_url

    def setCVEID(self, cveID):
        self.cveID = self.cveID + cveID

    def setDatePublic(self, days, month, year):
        self.datePublic = self.convertDate2Epoch(days, month, year, self.debug)

    def setDateFirstPublished(self, days, month, year):
        self.dateFirstPublished = self.convertDate2Epoch(days, month, year, self.debug)

    def setDateLastUpdated(self, days, month, year):
        self.dateLastUpdated = self.convertDate2Epoch(days, month, year, self.debug)

    def setSeverityMetric(self, severityMetric):
        self.severityMetric = severityMetric

    def setDocumentRevision(self, documentRevision):
        self.documentRevision = documentRevision

    #String function for vuln object
    def __str__(self):
        return('''
            Search URL:             {}
            VU#:                    {}
            CVEID:                  {}
            Date Public:            {}
            Date First Published:   {}
            Date Last Updated:      {}
            Severity Metric:        {}
            Document Revision:      {}'''.format(self.search_url, self.vulnID, self.cveID, self.datePublic, self.dateFirstPublished, self.dateLastUpdated, self.severityMetric, self.documentRevision))

#Class to search the database. It is passed three parameters. A true or false debug flag, the product being searched for, and the max number of results to return
class Search:

    #Function that will search and parse the results from the search
    def searchVuln(self, debug, vendor, product, searchMax):
        vulnList = [] #List to store parsed URLs from the query
        urlList = [] #List to store the vulnIDs
        searchDict = {} #Dict to hold the vuln objects with the key being the vulnID
        lookup_table = {'Jan':1,'Feb':2, 'Mar':3, 'Apr':4, 'May':5,'Jun': 6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        queryString = vendor + ' AND ' + product
        payload = {'query': queryString, 'searchmax': searchMax, 'searchorder': '1'} #payload dict that is passed to the get request
        results = requests.get('https://kb.cert.org/vuls/byid?searchview', params=payload) #get request to obtain results 
        soup = BeautifulSoup(results.text, 'html.parser') #BeutifulSoup is used to parse the reults

        for link in soup.find_all('a'): #Searches through the results for links and using regex to match a pattern to obtain partial urls with vulnIDs
            if re.search('/vuls/id/[0-9]*', str(link)):
                vulnList.append(str(re.findall('/vuls/id/[0-9]*', str(link))))

        for num in range(0,len(vulnList)): #parses the vulnList for the vulnIDs
            string = re.sub('[^0-9]+','',vulnList[num])
            urlList.append(string)

        #For each vulnID in the vulnList:
        for num in range(len(urlList)): 
            vuln = vulnObject(urlList[num], debug) #instantiate the vuln object
            search_url = 'https://kb.cert.org/vuls/id/' + urlList[num] #search URL used to obtain results
            vuln.setSearchURL(search_url)
            vul_results = requests.get(search_url) #Get request to pull details of the vulnerability
            parsed_results = BeautifulSoup(vul_results.text, 'html.parser') #Parsing the results with BeautifulSoup
            other_info = parsed_results.find(id="other-info") #Find the other-info section from the parsed results and creating a reference to them. This section holds in information on the vuln we are interested in

            #Find all the information from the other-info section and place the information we are interested in into the appropriate place in the vulnObject
            for li in other_info.find_all('li'):
                data1 = li.find_all('span')[0]
                data2 = li.find_all('span')[1]
                string1 = re.sub('[\[,\], \']', '',str(data1.contents))
                string2 = re.sub('[\[,\], \']', '',str(data2.contents))

                try:
                    if re.match('<ahref=', string2):
                        stringList = re.findall('C[A-Z]*-[0-9]*-[0-9]*', string2)
                        string2 = str(stringList[0])
                        if (len(stringList) > 1):
                            for pos in range(1,len(stringList)):
                                if (pos%2 == 0):
                                    string2 = string2 + ', ' +   stringList[pos]


                except AttributeError:
                    if debug:
                        print('AttributeError:  {}  {}'.format(string1,string2))

                    continue

                try:

                    if (string1 == 'CVEIDs:'):
                        vuln.setCVEID(string2)

                    elif (string1 == 'DatePublic:'):
                        days = string2[0:2]
                        month = string2[2:5]
                        year = int(string2[5:])
                        month = lookup_table[month]

                        if (year < 2000):
                            year = year + 1900

                        vuln.setDatePublic(days, month, year)

                    elif (string1 == 'DateFirstPublished:'):
                        days = string2[0:2]
                        month = string2[2:5]
                        year = int(string2[5:])
                        month = lookup_table[month]

                        if (year < 2000):
                            year = year + 1900

                        vuln.setDateFirstPublished(days, month, year)

                    elif (string1 == 'DateLastUpdated:'):
                        days = string2[0:2]
                        month = string2[2:5]
                        year = int(string2[5:])
                        month = lookup_table[month]

                        if (year < 2000):
                            year = year + 1900

                        vuln.setDateLastUpdated(days, month, year)

                    elif (string1 == 'SeverityMetric:'):
                        vuln.setSeverityMetric(string2)

                    elif (string1 == 'DocumentRevision:'):
                        vuln.setDocumentRevision(string2)

                    else:
                        continue

                except Exception as e:
                    print('Error from strings   {}    {}'.format(string1,string2))
                    print(search_url)
                    print (str(e))
                    print(traceback.print_exc())

                    if debug:
                        break

                    else:
                        return e


            searchDict[urlList[num]] = vuln

        return searchDict


    def run(self, debug, vendor, product, searchMax):
        results = self.searchVuln(debug, vendor, product, searchMax)
        nvdResults = requests.get('https://cve.circl.lu/api/search/' + vendor + '/' + product)
        parsed_json = json.loads(nvdResults.text)
        print(json.dumps(parsed_json))

        for key in parsed_json:
            cve = key['id']
            #print('CVE = {}'.format(cve))
            #print('\n')
            numMatches = 0

            for item in results:
                cveID = results[item].cveID
                #print('cveID = {}'.format(cveID))

                if re.findall(cve, cveID):
                    numMatches += 1
                    #print('Matched {} {} times'.format(cve, numMatches))
                
            if (numMatches == 0):
                year = key['Published'][0:4]
                month = key['Published'][5:7]
                days = key['Published'][8:10]
                #print(key['Published'])
                #print('Year = {} Month = {} Days = {}'.format(year, month, days))

                vuln = vulnObject(cve, debug)
                vuln.search_url = 'https://nvd.nist.gov/vuln/detail/' + cve
                vuln.cveID = cve

                vuln.setDatePublic(days, month, year)
                year = key['Modified'][0:4]
                month = key['Modified'][5:7]
                days = key['Modified'][8:10]

                vuln.setDateLastUpdated(days, month,year)
                #print('Year = {} Month = {} Days = {}'.format(year, month, days))
                vuln.severityMetric = key['cvss']
                results[cve] = vuln


        #print("Total number of vulns scraped: {}\n".format(len(results)))

        for item in results:
            print(str(results[item]))

        out = ''
        for item in results:
            out = out + json.dumps(results[item], default=lambda o: o.__dict__)

        print(out)



if __name__ == "__main__":
    #Parsing the command line for arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', help='turn on script debugging', action='store_true', default=False)
    parser.add_argument('vendor', type=str)
    parser.add_argument('product', type=str)
    parser.add_argument('searchMax', type=str)
    args = parser.parse_args()
    #print(args)

    Search().run(args.debug, args.vendor, args.product, args.searchMax)



    