# Progress Report 3/26/2018
## Overview


In milestone 1, our plan was to scrape the National Vulnerability Database to collect vulnerability information using Circle API.  As we began researching the data we had been collecting, we realized that the published dates of the vulnerabilities were not accurate and standardized.  Some of the dates, were very recent and did not accurately reflect when the patch was released and we could not determine the exact patch dates for the vulnerabilities. For this research project, we felt that patch dates were important to draw the timeline and to define the window of opportunities for the attacks. 

Because, we were not confident in the dates that National Vulnerability Database provided, we altered our approach.  With continued vigilance, we discovered the Carnegie Mellon University and US Cert vulnerability website, which depicted more accurate dates for the vulnerabilities.  The US Cert database contained the published date and the update date of the vulnerability, which we considered as patch date for the vulnerability. For extracting published and update date and other information from the US cert database we have written a python script to convert the HTML content to python objects using Beautiful soup HTML parser. 

We are currently working on improving and modifying the python script to search for the vulnerabilities of two different vendors, to draw the timeline for the vulnerabilities, and to figure out the common timeframe for vulnerabilities of two different products. In addition, we have to create the web front end using Django to search for the vulnerabilities to produce results in a timeline format showing the attack window of overlapping vulnerabilities to the user. In addition, it is important to note, that this python script will be doing real time searches to produce the result.  We originally wrote the python script to scrap the database once to hold the data in our own database for doing the queries.  We decided against this because the data would get old and you would have to manually run the script to re add the data.  Originally, we thought that we would use  mathematical probabilities to create a bell curve, which will depict the most likely window for an attacker to exploit both vulnerabilities leading to a successful breach into a network. After discussing and lookin at the available research on the subject, it was decided to forgo this route and give the user the ability to determine how long it will take to patch the vulnerability giving them guidance, based on the available research, on how long it takes the industry to patch vulnerabilities. 



## Outcomes

  Up to this point, we have completed our research into vulnerbilites, VPNs, and and the vulnerbility databases. We have also completed the python script to scrape the US cert vulnerability database and convert the results into objects that we intend to pass to our web application. Based on available research, we have determined the best approach to determining patch dates is to let the user decide and give guidance on the app on patch windows based on the availbale research. 
  
  Efforts made (please add to list as needed)
  
  1. Completed research
  2. Completed [python script](https://github.com/MLHale/insure-layered-solutions/blob/master/python/layeredSolutionsClasses.py) to scrape cert.org vulnerability database
  3. Determined approach to deal with unknown patch dates

## Hinderances

* Coming up with an accepted approach to dealing with unknown patch dates
* Learning BeautifulSoup to help scrape the database and parsing the results obtained to receive relevant data from the python script

## Ongoing Risks

| Risk Name (value) | Impact | Likelihood | Description |
|-------------------------------------------------------|--------|------------|:---------------------------------------------------------------------------------------------------------------------------------------:|
| Programming issues (21) | 7 | 3 | Any programming issues with the HTML webpage or the Python program will slow progress. |
|    Unable to find exploit and patch dates (32)        | 8| 4 | If exploit and patch dates cannot be found or incorrect, the final results in the timeline will be off. |
| No vulnerability overlaps in timeline (24) | 8 | 3 | Problems could arise if the vulnerability timeline is not showing overlaps properly.    |
| Problems gathering data (12) | 6 | 2 | Any major issues scraping databases for information will not allow for the rest of the project to continue until data can be retrieved. |
| Team member availability (36) | 9 | 4 | Team members must be able to coordinate appropriate times to meet otherwise progress will be slowed. |
| CVEs not found (12) | 6 | 2 | The project will not work if relevant CVEs cannot be found for the Enterprise VPN solutions that have been chosen |
