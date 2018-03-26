# Progress Report 3/26/2018
## Overview

In milestone1, our plan was to scrape the National Vulnerability Database to collect vulnerability information using Circle API.  As we began researching the data we had been collecting, we realized that the published dates of the vulnerabilities were not accurate and standardized.  Some of the dates, were very recent and did not accurately reflect when the patch was released and we could not determine the exact patch dates for the vulnerabilities. For this research project, we felt that patch dates were important to draw the timeline and to define the window of opportunities for the attacks. 
Because, we were not confident in the dates that National Vulnerability Database provided, we altered our approach.  With continued vigilance, we discovered the Carnegie Mellon University and US Cert vulnerability website, which depicted more accurate dates for the vulnerabilities.  The US Cert database contained the published date and the update date of the vulnerability, which we considered as patch date for the vulnerability. For extracting published and update date and other information from the US cert database we have written a python script to convert the HTML content to python objects using Beautiful soup HTML parser. 
We are currently working on improving and modifying the python script to search for the vulnerabilities of two different vendors, to draw the timeline for the vulnerabilities, and to figure out the common timeframe for vulnerabilities of two different products. In addition, we have to create the web front end using Django to search for the vulnerabilities to produce results in a timeline format showing the attack window of overlapping vulnerabilities to the user. In addition, it is important to note, that this python script will be doing real time searches to produce the result.  We originally wrote the python script to scrap the database once to hold the data in our own database for doing the queries.  We decided against this because the data would get old and you would have to manually run the script to re add the data.  We are working on using some mathematical probabilities to create a bell curve, which will depict the most likely window for an attacker to exploit both vulnerabilities leading to a successful breach into a network.


## Outcomes

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
| Programming issues (64) | 8 | 8 | Any programming issues with the HTML webpage or the Python program will slow progress. |
|    Unable to find exploit and patch dates (63)        | 9 | 7 | If exploit and patch dates cannot be found or incorrect, the final results in the timeline will be off. |
| No vulnerability overlaps in timeline (56) | 8 | 7 | Problems could arise if the vulnerability timeline is not showing overlaps properly.    |
| Problems gathering data (18) | 6 | 3 | Any major issues scraping databases for information will not allow for the rest of the project to continue until data can be retrieved. |
| Team member availability (15) | 5 | 3 | Team members must be able to coordinate appropriate times to meet otherwise progress will be slowed. |
| CVEs not found (12) | 6 | 2 | The project will not work if relevant CVEs cannot be found for the Enterprise VPN solutions that have been chosen |
