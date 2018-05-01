# Progress Report 5/3/2018
## Overview (To Do: update as necessary for milestone 3)

In milestone 2, we showed the Python script that will be used to pull vulnerability data from the US Cert database. The script will take the HTML data and convert that into python objects using BeautifulSoup. These objects will be fed into the web application to display a D3 timeline of the vulnerabilities. That interaction between the Python script and the web application was the main focus for milestone 3.
The final product that an end user will see from this project is the timeline of vulnerabilities that will be displayed in our web application created with Django. The timeline will allow a user to choose two different VPN vendors, click “Submit”, and have a timeline generated automatically using the information scraped from the US Cert and NVD databases. The website also allows for two dates to be selected so that the timeline is generated for only that given time period.

![UML](https://github.com/MLHale/insure-layered-solutions/blob/master/GantCharts/webpage.png)
 
The website will allow a company or individual to decide for themselves if a layered solution of two VPNs would be appropriate. A timeline can be quickly generated to compare two different vendor VPNs over a selected date range that will show any overlapping vulnerabilities between the VPNs. This comparison will allow the company to make the decision as to what VPNs to go with based on the history of vulnerabilities of the two chosen vendors as well as the likelihood that any one vulnerability will line up with another. The website gives users a tool to be able to mix and match different VPN vendors to determine how vulnerable a layered solution may be to attackers.

## Outcomes (To Do: "document the product or other intellectual/applied outcomes that have resulted from your efforts, and bind your tasks to the outcomes and documentation you have produced so far.")

* Built the website using the Django Framework
* Completed the timeline implementation on the website
* Determined appropriate keyword searches for vulnerability databases
* Integrate the Python script with the website to return live data
* Documented the results of the project to be able to present a finished product



## Hinderances (To Do: Update/Remove hindrances as necessary; add any new ones)

* Difficulty parsing data from webpages
* Compensating for differences between the vulnerability databases
* Possible lack of sufficient data points to build vulnerability/exploit model
* Programming the front end of our web app to interact appropriately with our scripts

