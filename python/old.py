mport requests
import AdvancedHTMLParser
import json
import pprint
import re

payload = {'query': 'cisco', 'searchmax': '10', 'searchorder': '1'}
results = requests.get('https://kb.cert.org/vuls/byid?searchview', params=payload)
#print(results)

from bs4 import BeautifulSoup
soup = BeautifulSoup(results.text, 'html.parser')

vulnList = []
urlList = []
searchDict = {}

for link in soup.find_all('a'):
    if re.search('/vuls/id/[0-9]*', str(link)):
        vulnList.append(str(re.findall('/vuls/id/[0-9]*', str(link))))

for num in range(0,len(vulnList)):
    string = re.sub('[^0-9]+','',vulnList[num])
    urlList.append(string)

for num in range(len(urlList)):
    search_url = 'https://kb.cert.org/vuls/id/' + urlList[num]
    print(search_url)
    print('VU#' + urlList[num])
    vul_results = requests.get(search_url)
    parsed_results = BeautifulSoup(vul_results.text, 'html.parser')
    other_info = parsed_results.find(id="other-info")

    for li in other_info.find_all('li'):
            data1 = li.find_all('span')[0]
            data2 = li.find_all('span')[1]
            string1 = re.sub('[\[,\], \']', '',str(data1.contents))
            string2 = re.sub('[\[,\], \']', '',str(data2.contents))

            if re.search('<ahref=', string2):
                #print(string2)
                string2 = re.search('C[A,V][N,E]-[0-9]*-[0-9]*', string2).group()

            print(string1 + ' ' + string2)

    print()