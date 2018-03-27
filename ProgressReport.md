# Progress Report 3/26/2018
## Overview

In milestone1, our plan was to scrape the National Vulnerability Database to collect vulnerability information using Circle API.  As we began researching the data we had been collecting, we realized that the published dates of the vulnerabilities were not accurate and standardized.  Some of the dates were very recent and did not accurately reflect when the patch was released and we could not determine the exact patch dates for the vulnerabilities. For this research project, we felt that patch dates were important to draw the timeline and to define the window of opportunities for the attacks. 

Because, we were not confident in the dates that National Vulnerability Database provided, we altered our approach.  With continued vigilance, we discovered the Carnegie Mellon University and US Cert vulnerability website, which depicted more accurate dates for the vulnerabilities.  The US Cert database contained the published date and the update date of the vulnerability, which we considered as patch date for the vulnerability. For extracting published and update date and other information from the US cert database we have written a python script to convert the HTML content to python objects using Beautiful soup HTML parser. 

We are currently working on improving and modifying the python script to search for the vulnerabilities of two different vendors, to draw the timeline for the vulnerabilities, and to figure out the common timeframe for vulnerabilities of two different products. In addition, we have to create the web front end using Django to search for the vulnerabilities to produce results in a timeline format showing the attack window of overlapping vulnerabilities to the user. It is important to note that this python script will be doing real time searches to produce the result.  We originally wrote the python script to scrap the database once to hold the data in our own database for doing the queries.  We decided against this because the data would get old and you would have to manually run the script to refresh the data.  Originally, we thought that we would use  mathematical probabilities to create a bell curve, which will depict the most likely window for an attacker to exploit both vulnerabilities leading to a successful breach into a network. After discussing and lookin at the available research on the subject, it was decided to forgo this route and give the user the ability to determine how long it will take to patch the vulnerability giving them guidance, based on the available research, on how long it takes the industry to patch vulnerabilities. 

![UML](https://github.com/MLHale/insure-layered-solutions/blob/master/GantCharts/uml3.png)

## Outcomes

  Efforts made (please add to list as needed)
  
  1. Completed research
  2. Completed [python script](https://github.com/MLHale/insure-layered-solutions/blob/master/python/layeredSolutionsClasses.py) to scrape cert.org vulnerability database
  3. Determined approach to deal with unknown patch dates

## Hinderances

* Coming up with an accepted approach to dealing with unknown patch dates
* Learning BeautifulSoup to help scrape the database and parsing the results obtained to receive relevant data from the python script
* Determining the best way to pass data between the search Python script and the web app
* Learning Django to be able to build the website and host the data obtained by the python script

## Ongoing Risks

| Risk Name (value) | Impact | Likelihood | Description |
|-------------------------------------------------------|--------|------------|:---------------------------------------------------------------------------------------------------------------------------------------:|
|    Unable to find exploit and patch dates (42) | 7| 6 | If exploit and patch dates cannot be found or incorrect, the final results in the timeline will be off. |
| Programming issues (40) | 8 | 5 | Any programming issues with the HTML webpage or the Python program will slow progress. |
| No vulnerability overlaps in timeline (40) | 8 | 5 | Problems could arise if the vulnerability timeline is not showing overlaps properly.    |
| Team member availability (28) | 7 | 4 | Team members must be able to coordinate appropriate times to meet otherwise progress will be slowed. |
| Learning curve of applications such as Django, BeautifulSoup, etc (25) | 5 | 5 | Time must be spent learning the applications that will be used to conduct the project. This doesn't have that high of an impact because other team members can help fill in the gaps. |
| Problems gathering data (24) | 6 | 4 | Any major issues scraping databases for information will not allow for the rest of the project to continue until data can be retrieved. |
| CVEs not found (12) | 6 | 2 | The project will not work if relevant CVEs cannot be found for the Enterprise VPN solutions that have been chosen |

## Helpful Diagrams
![alt text](https://i.imgur.com/qPILImM.jpg "Problem Diagram")

This first diagram is a visualization of the question we are trying to answer. The blue and red "layers" represent two different VPN solutions in use and the black hat represents the attacker attempting to weave their way into the critical systems. However, it does not address a situation where an attacker can create permanent access through the first layer.

![alt text](https://i.imgur.com/jKtN5oR.jpg "Data Diagram")
