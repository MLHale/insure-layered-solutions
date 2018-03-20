# @Author: Matthew Hale <matthale>
# @Date:   2018-03-20T12:18:08-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: vulnCode.py
# @Last modified by:   matthale
# @Last modified time: 2018-03-20T12:57:05-05:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



import requests
import json
import pprint
import re
import time
import datetime
from bs4 import BeautifulSoup
from dateparser import parse
from datetime import datetime
from time import mktime

class vulnObject:

    numVulns = 0

    def __init__(self, vulnID):
        self.vulnID = vulnID
        vulnObject.numVulns +=1

    def setSearchURL(self, search_url):
        self.search_url = search_url

    def setCVEID(self, cveID):
        self.cveID = cveID

    def setDatePublic(self, datePublic):
        self.datePublic = datePublic

    def setDateFirstPublished(self, dateFirstPublished):
<<<<<<< HEAD
        self.dateFirstPublished = dateFirstPublished
=======
        print dateFirstPublished
        # print time.mktime(dateFirstPublished)
        days = dateFirstPublished[1:3]
        month = dateFirstPublished[3:6]
        year = dateFirstPublished[6:]
        print days, month, year
        lookup_table = {'Jan':1,'Feb':2, 'Mar':3, 'Apr':4, 'May':5,'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        date_obj = datetime.date(int(year), int(lookup_table[month]), int(days))
        timestamp = time.mktime(date_obj.timetuple())
        print timestamp
        print datetime.datetime.fromtimestamp(timestamp)
        self. dateFirstPublished = dateFirstPublished
>>>>>>> c93427c3fe85c4fc2c95888008684368d3bd1508

    def setDateLastUpdated(self, dateLastUpdated):
        self.dateLastUpdated = dateLastUpdated

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

    def searchVuln(self):
        vulnList = []
        urlList = []
        searchDict = {}
        payload = {'query': 'cisco', 'searchmax': '1000', 'searchorder': '1'}
        start = datetime.datetime.now()
        results = requests.get('https://kb.cert.org/vuls/byid?searchview', params=payload)
        end = datetime.datetime.now()
        print end - start
        soup = BeautifulSoup(results.text, 'html.parser')


        for link in soup.find_all('a'):
            if re.search('/vuls/id/[0-9]*', str(link)):
                vulnList.append(str(re.findall('/vuls/id/[0-9]*', str(link))))

        for num in range(0,len(vulnList)):
            string = re.sub('[^0-9]+','',vulnList[num])
            urlList.append(string)

        for num in range(len(urlList)):
            vuln = vulnObject(urlList[num])
            search_url = 'https://kb.cert.org/vuls/id/' + urlList[num]
            vuln.setSearchURL(search_url)
            tempList = []
            vul_results = requests.get(search_url)
            parsed_results = BeautifulSoup(vul_results.text, 'html.parser')
            other_info = parsed_results.find(id="other-info")
            print(other_info)

            for li in other_info.find_all('li'):
                data1 = li.find_all('span')[0]
                data2 = li.find_all('span')[1]
                string1 = re.sub('[\[,\], \']', '',str(data1.contents))
                string2 = re.sub('[\[,\], \']', '',str(data2.contents))

                if re.search('<ahref=', string2):
                    string2 = re.search('C[A,V][N,E]-[0-9]*-[0-9]*', string2).group()

                tempList.append(string1)
                tempList.append(string2)

            vuln.setCVEID(tempList[1])
            vuln.setDatePublic(tempList[3])
            vuln.setDateFirstPublished(tempList[5])
            vuln.setDateLastUpdated(tempList[7])
            vuln.setSeverityMetric(tempList[9])
            vuln.setDocumentRevision(tempList[11])

            searchDict[urlList[num]] = vuln

        return searchDict


    def run(self):
        results = self.searchVuln()
        print("Total number of vulns scraped: {}\n".format(len(results)))

        for item in results:
            print(str(results[item]))

if __name__ == "__main__":
    Search().run()
