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

    #Functions below are used to set the elements of the object
    def setSearchURL(self, search_url):
        self.search_url = search_url

    def setCVEID(self, cveID):
        self.cveID = self.cveID + cveID

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
    def searchVuln(self):
        vulnList = [] #List to store parsed URLs from the query
        urlList = [] #List to store the vulnIDs
        searchDict = {} #Dict to hold the vuln objects with the key being the vulnID
        #payload = {}
         #payload dict that is passed to the get request
        results = requests.get('https://cve.circl.lu/api/search/' + 'cisco' + '/' + 'anyconnect') #get request to obtain results 
        #soup = BeautifulSoup(results.text, 'html.parser') #BeutifulSoup is used to parse the reults
        parsed_json = json.loads(results.text)
        for key in parsed_json:
            print(key['id'])
            #print('\n')
        



    def run(self):
        #results = self.searchVuln(debug, product, searchMax)
        #print("Total number of vulns scraped: {}\n".format(len(results)))

        #for item in results:
            #print(str(results[item]))
        self.searchVuln()

if __name__ == "__main__":
    #Parsing the command line for arguments
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-d', '--debug', help='turn on script debugging', action='store_true', default=False)
    #parser.add_argument('product', type=str)
    #parser.add_argument('searchMax', type=str)
    #args = parser.parse_args()
    #print(args)

    Search().run()



    