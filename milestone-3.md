# Progress Report 5/3/2018
## Overview (To Do: update for milestone 3)

In milestone1, our plan was to scrape the National Vulnerability Database to collect vulnerability information using Circle API.  As we began researching the data we had been collecting, we realized that the published dates of the vulnerabilities were not accurate and standardized.  Some of the dates were very recent and did not accurately reflect when the patch was released and we could not determine the exact patch dates for the vulnerabilities. For this research project, we felt that patch dates were important to draw the timeline and to define the window of opportunities for the attacks. 

Because, we were not confident in the dates that National Vulnerability Database provided, we altered our approach.  With continued vigilance, we discovered the Carnegie Mellon University and US Cert vulnerability website, which depicted more accurate dates for the vulnerabilities.  The US Cert database contained the published date and the update date of the vulnerability, we considered update date as patch date for the vulnerability. For extracting published date, update date and other information from the US cert database we have written a python script to convert the HTML content to python objects using Beautiful soup HTML parser. 

We are currently working on improving and modifying the python script to search for the vulnerabilities of two different vendors, to draw the timeline for the vulnerabilities, and to figure out the common timeframe for vulnerabilities of two different products. In addition, we have to create the web front end using Django to search for the vulnerabilities to produce results in a timeline format showing the attack window of overlapping vulnerabilities to the user. It is important to note that this python script will be doing real time searches to produce the result.  We originally wrote the python script to scrap the database once to hold the data in our own database for doing the queries.  We decided against this because the data would get old and you would have to manually run the script to refresh the data.  Originally, we thought that we would use  mathematical probabilities to create a bell curve, which will depict the most likely window for an attacker to exploit both vulnerabilities leading to a successful breach into a network. After discussing and lookin at the available research on the subject, it was decided to forgo this route and give the user the ability to determine how long it will take to patch the vulnerability giving them guidance, based on the available research, on how long it takes the industry to patch vulnerabilities. 

## Outcomes (To Do: "document the product or other intellectual/applied outcomes that have resulted from your efforts, and bind your tasks to the outcomes and documentation you have produced so far.")

* outcome 1
* outcome 2

## Hinderances (To Do: Update/Remove hindrances as necessary; add any new ones)

* Coming up with an accepted approach to dealing with unknown patch dates
* Learning BeautifulSoup to help scrape the database and parsing the results obtained to receive relevant data from the python script
* Determining the best way to pass data between the search Python script and the web app
* Learning Django to be able to build the website and host the data obtained by the python script
