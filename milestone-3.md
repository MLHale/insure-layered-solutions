# Progress Report 5/3/2018
## Overview

In Milestone 2, we demoed the Python script that is used to pull vulnerability data from the US Cert database. During continued work in Milestone 3, it became apparent that the US Cert database did not contain enough data for our project.  At this point we began to revisit our approach from Milestone 1 and determine a way to utilize the CIRCL database, which contains the National Vulnerability database’s data. The Python script was adjusted to collect data from both databases.  Also, an assumption had to be made.  Remembering from Milestone 2 that the CIRCL database's published dates were not accurate and standardized, we needed to decide on a fair length of time in which a patch could be applied.  It was decided to use 60-90 days from the date made public, as published date the vulnerability was patched.  This timeframe was decided because this was a reasonable amount of time that an institution would take to conduct the patch, within their change window.  As results of both database were reviewed, we concluded that data being returned was not the same from both databases.  This was because the input that each database received was handled differently.  To compensate for this a legend was created, so that inputs would return proper output.  
To recap, the script receives the user input, extracts the useful fields with the Beautiful Soup HTML parser and returns the python objects. Before the information is return to the web application the Python objects are converted to json.  This data is sent into the web application to display a timeline of the vulnerabilities using d3.js. The interaction between the Python script and the web application was the main focus for milestone 3. The final product that an end user will interact with from this project is the timeline of vulnerabilities that will be displayed in our web application created with Django. The timeline will allow a user to choose two different VPN vendors and timeframes.  Submitting the inputs will return a timeline generated automatically using the information scraped from the US Cert and NVD databases. The website also allows for two dates to be selected so that the timeline is generated for only that given time period.


![UML](https://github.com/MLHale/insure-layered-solutions/blob/master/GantCharts/webpage.png)
 
The website will allow a company or individual to decide if a layered solution of two VPN products would be appropriate. A timeline can be quickly generated to compare two different vendor VPNs over a selected date range that will display any overlapping vulnerabilities between the VPNs. This overlap is called that attack window.  This comparison will aid in a company’s decision to determine what combination of VPN products to go with based on the history of vulnerabilities of the two chosen vendors as well as the likelihood that any one vulnerability will line up with another. The website supplies users a tool to be able to mix and match different VPN vendors to determine how vulnerable a layered solution may be to attackers.
Additionally, our tool can be easily built upon to include additional security solutions with vulnerabilities in the databases we search. Continuing to make improvements and  additions to the user experience such as this, will aid in the applications function as a powerful tool for risk analysis and security planning in regards to layered solutions.


## Outcomes
We ultimately achieved our end goal of creating a web application that allows a user to compare layered VPN solutions to determine if a layered solution is right for their organization. Using the Django framework and Python, we were able to create a fully functional web page that collects data from the user and two separate vulnerability databases to create timeline to visualize the attack windows for a given layered solution. With this tool, we believe organizations can make better informed decision when considering a layered solution. 

* Built the website using the Django Framework
* Completed the timeline implementation on the website
* Determined appropriate keyword searches for vulnerability databases
* Integrated the Python script with the website to return live data
* Documented the results of the project to be able to present a finished product
* Successfully built a tool that can help an organization make better informed decisions when securing their technology



## Hinderances

* Difficulty parsing data from webpages
* Compensating for differences between the vulnerability databases (Eg: Different data points, different search mechanisms)
* Problems with gathering useful data from the databases (Eg: Lack of patch dates, incorrect dates)
* Problems determining which search keywords give us the best data 
* Programming the front end of our web app to interact appropriately with our scripts
* Difficulty presenting the large amount of data we have to the user in an effective manner
