import sys
import argparse
import requests
import re
import traceback
import datetime
from bs4 import BeautifulSoup
from time import mktime

class vulnObject:

    numVulns = 0

    def __init__(self, vulnID, debug):
        self.vulnID = vulnID
        self.search_url =''
        self.cveID = ''
        self.datePublic = 0.0 
        self.dateFirstPublished = 0.0
        self.dateLastUpdated = 0.0
        self.severityMetric = 0.0
        self.documentRevision = 0.0
        self.debug = debug

        vulnObject.numVulns +=1

    def convertDate2Epoch(self, date, debug):
        self.debug = debug
        days = date[0:2]
        month = date[2:5]
        year = int(date[5:])

        if (year < 2000):
            year = year + 1900

        try:
            lookup_table = {'Jan':1,'Feb':2, 'Mar':3, 'Apr':4, 'May':5,'Jun': 6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
            date_obj = datetime.date(int(year), int(lookup_table[month]), int(days))
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

    def setSearchURL(self, search_url):
        self.search_url = search_url

    def setCVEID(self, cveID):
        self.cveID = cveID

    def setDatePublic(self, datePublic):
        self.datePublic = self.convertDate2Epoch(datePublic, self.debug)

    def setDateFirstPublished(self, dateFirstPublished):
        self.dateFirstPublished = self.convertDate2Epoch(dateFirstPublished, self.debug)

    def setDateLastUpdated(self, dateLastUpdated):
        self.dateLastUpdated = self.convertDate2Epoch(dateLastUpdated, self.debug)

    def setSeverityMetric(self, severityMetric):
        self.severityMetric = severityMetric

    def setDocumentRevision(self, documentRevision):
        self.documentRevision = documentRevision

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

class Search:

    def searchVuln(self, debug, product, searchMax):
        vulnList = []
        urlList = []
        searchDict = {}
        payload = {'query': product, 'searchmax': searchMax, 'searchorder': '1'}
        results = requests.get('https://kb.cert.org/vuls/byid?searchview', params=payload)
        soup = BeautifulSoup(results.text, 'html.parser')

        for link in soup.find_all('a'):
            if re.search('/vuls/id/[0-9]*', str(link)):
                vulnList.append(str(re.findall('/vuls/id/[0-9]*', str(link))))

        for num in range(0,len(vulnList)):
            string = re.sub('[^0-9]+','',vulnList[num])
            urlList.append(string)

        for num in range(len(urlList)):
            vuln = vulnObject(urlList[num], debug)
            search_url = 'https://kb.cert.org/vuls/id/' + urlList[num]
            vuln.setSearchURL(search_url)
            tempList = []
            vul_results = requests.get(search_url)
            parsed_results = BeautifulSoup(vul_results.text, 'html.parser')
            other_info = parsed_results.find(id="other-info")

            for li in other_info.find_all('li'):
                data1 = li.find_all('span')[0]
                data2 = li.find_all('span')[1]
                string1 = re.sub('[\[,\], \']', '',str(data1.contents))
                string2 = re.sub('[\[,\], \']', '',str(data2.contents))

                try:
                    if re.match('<ahref=', string2):
                        string2 = re.search('C[A-Z]*-[0-9]*-[0-9]*', string2).group()

                except AttributeError:
                    if debug:
                        print('AttributeError:  {}  {}'.format(string1,string2))

                    continue

                try:

                    if (string1 == 'CVEIDs:'):
                        vuln.setCVEID(string2)

                    elif (string1 == 'DatePublic:'):
                        vuln.setDatePublic(string2)

                    elif (string1 == 'DateFirstPublished:'):
                        vuln.setDateFirstPublished(string2)

                    elif (string1 == 'DateLastUpdated:'):
                        vuln.setDateLastUpdated(string2)

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
                    traceback.print_exc()

                    if debug:
                        break

                    else:
                        return e


            searchDict[urlList[num]] = vuln

        return searchDict


    def run(self, debug, product, searchMax):
        results = self.searchVuln(debug, product, searchMax)
        print("Total number of vulns scraped: {}\n".format(len(results)))

        for item in results:
            print(str(results[item]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', help='turn on script debugging', action='store_true', default=False)
    parser.add_argument('product', type=str)
    parser.add_argument('searchMax', type=str)
    args = parser.parse_args()
    #print(args)

    Search().run(args.debug, args.product, args.searchMax)



    