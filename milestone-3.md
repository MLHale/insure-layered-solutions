# Progress Report 5/3/2018
## Overview (To Do: update as necessary for milestone 3)

In milestone 2, we showed the Python script that will be used to pull vulnerability data from the US Cert database. The script will take the HTML data and convert that into python objects using BeautifulSoup. These objects will be fed into the web application to display a D3 timeline of the vulnerabilities. That interaction between the Python script and the web application was the main focus for milestone 3. 

The final product that an end user will see from this project is the timeline of vulnerabilities that will be displayed in our web application created with Django. The timeline will allow a user to choose two different VPN vendors, click compare, and have a timeline generated automatically using the information scraped from the US Cert database. Some of the vendor applications are very robust in what they offer, so we have also included a line on the timeline for all vulnerabilities. This allows the user to be aware of vulnerabilities that may be present outside of just the VPN solution from that specific vendor. If any of the vulnerabilities correlate on the timeline (VPN or otherwise), it will indicate a time window for which an attacker could have gained access to the application. 

The timeline displayed by the web application allows a company or individual to decide for themselves if a layered solution will be appropriate. If a company has determined that a layered VPN solution is something they want to pursue, then the vulnerability timeline will allow for that comparison of vendors. This comparison will allow the company to make the decision as to what VPNs to go with based on the history of vulnerabilities of the two chosen vendors as well as the likelihood that any one vulnerability will line up with another.


## Outcomes (To Do: "document the product or other intellectual/applied outcomes that have resulted from your efforts, and bind your tasks to the outcomes and documentation you have produced so far.")

* outcome 1
* outcome 2

## Hinderances (To Do: Update/Remove hindrances as necessary; add any new ones)

* Coming up with an accepted approach to dealing with unknown patch dates
* Learning BeautifulSoup to help scrape the database and parsing the results obtained to receive relevant data from the python script
* Determining the best way to pass data between the search Python script and the web app
* Learning Django to be able to build the website and host the data obtained by the python script
