# The Impact of Known Vulnerabilities on Layered Solutions

## Executive Summary
(overview of project, reuse from milestone 1, update if scope changed)

The purpose of layered solutions is to give the ability of an institution to use layered commercial products to deliver access to their critical data while maintaining security.  Traditionally, government devices were designed and certified to be used to access their most sensitive data.  This is extremely costly and time consuming.  Recently, the government has been reviewing proposals which would utilize commercial devices to deliver the same results as the government devices.  To increase the governments assurance, the government is attempting to ascertain if the use of multiple or layered solutions will provide the level of assurance that a government device would deliver.

This task will attempt to determine the security benefit of using layered solutions in an institution and if it affords any advantages.  The two layers being investigated will be enterprise VPN solutions.  It will be prudent to research the National Vulnerability Database and the Common Vulnerabilities and Exposures database in order to create a timeline of vulnerabilities for enterprise solutions over the years at varying code levels.  It will be important to distinguish between the time the vulnerability is known and the time when the patch is released.  There is also another aspect to take into account.  It cannot be assumed that when the patch is released, that this will be the time that the institutions devices would be patched.  There will need to be a patch window, in which, an institution would review, test, and assign the patch to a change management request.  The research will need to be limited to only vulnerabilities that could possibility compromise a security layer.  The timeline will be developed to aid in displaying overlapping vulnerabilities of the layered solutions selected, if they exist.

It will be also important to ascertain the possibility of an adversaries' ability to compromise layered solutions that do not have overlapping timelines.  This would involve an adversary's ability to compromise one layer and then wait until the other solution has a new vulnerability known to it.  History has shown, in many cases adversaries will gain some access and sit and wait until another opportunity presents itself.  

Lastly, it will be important to research how long it takes an exploit to be created once the vulnerability is known.  This information will be easily identified as the timeline is created with vulnerabilities, patches and available exploits of VPN solutions. It will be important to also point out if there have been successful exploits of these vulnerabilities, not just hypothesized exploits that should be possible.

This is type of research is extremely important to all institutions to help protect sensitive data and mitigate the adversaries' ability to breach their network.  By compiling all of this data and creating a timeline to analyze this data, the hope is to provide useful information to confirms or denies the advantage of introducing layered solutions into an institutions network security posture.

## Project Goals

* Extract data from NVD and CERT database
* Construct timeline using the vulnerability data
* Create webpage to serve this data to a user
* Develop a web application that can aid users when they are deciding if a layered solution is right for them


## Project Methodology
(specific methodology followed in the project, reuse from milestone 1/2, update if scope changed)

R. Haverkos and D. Sokoler have done research on layered solutions as part of the INSuRE project. They considered the vulnerabilities of the two VPNs (Cisco AnyConnect and Juniper) and estimated a time window for the patches to those vulnerabilities. In this method, they have collected the data from the National Vulnerability Database and estimated the patch availabilities dates and then measured the windows of opportunities. The result was the development of a simulation considering the two security mechanisms as layered solutions. [14]

National Vulnerability Database(NVD) [7] contains the information of vulnerabilities on a wide range of products. This database contains the detailed information like the Common Vulnerabilities and Exposures(CVE) [4] identifier which is a unique identifier given to the vulnerability of the product.  Also, this database contains the published date of the vulnerability, references to advisories, and solutions and tools to vulnerability entry.  Each CVE has a rating from Common Vulnerability Scoring System(CVSS) which gives the severity level of the vulnerability.  Lastly, the Common Weakness Enumeration(CWE) [5] identifier which provides a method to qualitatively categorize these vulnerabilities and the summary description of the vulnerability. The base metric used to classify the severity and the outcomes of the vulnerabilities is based on the CVSS.

A. Arora, R. Krishnan, A. Handkumar, R. Telang, Y. Yang, made an attempt to empirically test the vulnerabilities disclosure and availability of how patches affect vendors and attackers. In their work they came to conclusion that at first, vendors are quick in disclosing the vulnerabilities which made it easier for the attacker to attack the product, but latter on the process of disclosing the vulnerabilities reduces the attacks. They gathered the vulnerabilities from the public domains like NVD, CERT, Bugtraq etc. [8]

In the RSA Conference [10] they talked about the layering security solutions. In data transmission highly, sensitive data requires a high level of assurance, this can be possible by several layers of authorization from different agencies. Traditionally, government devices were designed and certified in order to handle the most sensitive data. The adoption GOTS(Government-Off-The-Shelf) solutions provide high level of assurance but this has made high operating cost for developing the high assurance devices. National Security Agency(NSA) Central Security Service(CSS) has come up with a program known as Commercial Solutions for Classified (CSfC) program [3] to leverage the cost and to provide the same assurance as GOTS solutions. The principle of CSfC is that properly configured and layered solutions can provide sufficient protection for the classified data. Composition of the security mechanisms(layering) provides a high level of assurance then the individual mechanisms.

##Update methodology to better suit our project?

Our methodology for this project started with our plan to scrape the NVD and CERT database to gather vulnerability data around the VPN solutions we chose to evaluate. We utilized a HTML scraping and the CIRCL API to pick out the data we wanted to display to our users. We developed a sophisticate python script that allows a user to submit two vendors and a date range in order to seek out and return vulnerability data for their selected vendors. Then, we chose to build a web application that utilizes this python script in the backend and displays the data it returns in a JavaScript timeline. We harnessed the power of the Django web framework to create a smooth and functional website. 

## Results / Findings
(brief overview of outcomes - what did you achieve?, list milestone 1/2/3 outcomes, make an effort to logically collect and organize the findings)

(bulleted lists can also be helpful to structure your results discussion)
* Successfully built a web application to allow a user to compare VPN vendors to determine past vulnerability windows
* Built the website so it can be easily expanded to other security solutions that may be layered
* Successfully built a python script to scrap vulnerability data from the NVD and CERT database

## Hinderances
There were several hinderances encountered completing the project. The first hinderance was scrapping the cert.org database. As this database does not have an API, it was necessary to search the database and then parse the html results. Once this was working, it was determined that the NVD database would need to be searched and scrapped as well as the cert.org database only included a subset of published vulnerabilities. The scrapping of this database was straightforward as there was an API to accomplish it, the difficulties lied in merging the results together and compensating for the differences between them. This was especially true with the differences in the keywords needed to search the two databases were different. To overcome this, research was done on what keyword obtained the best results. 
	Once the search results were obtained, it was necessary to determine an approach on how to obtain the patch dates for the vulnerabilities. We decided on this methodology: 
•	For the cert.org database, it was determined that the last date the page was updated correlated to the patch date for the vulnerability
•	For the NVD database, it was not as simple as selecting the last date the page was updated as that date appeared to correspond to any change that was made to the page. As there was not good mechanism to determine the patch date, it was decided to use as a standard sixty days. It was decided that sixty days was a good benchmark for an organization to patch, test, and re-deploy a system based on known research and industry experience.
Other hinderances were programming the front end of the web app and have it interact appropriately with the scripts we had written as most of the team had limited experience with JavaScript and Django. It was also difficult to determine the best approach to present the large amount of data that was obtained to the user in an effective manner until we were introduced to the d3,js framework.

## Install Instructions (if applicable)
### Requirements
(list of any software / hardware requirements necessary to run the code/app/etc)

### Installation Instructions
(list of steps to install the product/app/code/etc)

### Getting started
(list of any steps to run the code after installation and/or manage the apps over their lifecycle)

## Bibliography

1. Arora, A., Krishnan, R., Telang, R., & Yang, Y. (2006). An empirical analysis of software vendors' patching behavior: Impact of vulnerability disclosure. ICIS 2006 Proceedings, 22.

2. Cohen, F. (1999). Simulating cyber attacks, defences, and consequences. Computers & Security, 18(6), 479-518.

3. “Commercial Solutions for Classified Program” National Security Agency, Information Assurance. 2012 https://www.nsa.gov/ia/programs/csfc_program/

4. “Common Vulnerabilities and Exposures”. MITRE. 2014. Available https://cve.mitre.org/

5. “Common Weakness Enumeration”. MITRE. 2015. Available https://cwe.mitre.org/

6. “cve-search Common Vulnerabilities and Exposures”. CIRCL. 2016. 

7. “National Vulnerability Database”. NIST. 2002. Available http://nvd.nist.gov

8. A. Arora, R. Krishnan, A. Handkumar, R. Telang, Y. Yang, "Impact of Vulnerability Disclosure and Patch Avalability – An Empirical Analysis" H. John Heinz III School of Public Policy and Management, Canregie Mellon University, April 2004.

9. Behannon, J. (2017, December 09). Cyberwar Surprise Attacks Get a Mathematical Treatment. Retrieved February 08, 2018, from http://www.sciencemag.org/news/2014/01/cyberwar-surprise-attacks-get-mathematical-treatment

10. C. Farrington, D. Hlavacek, E. Rodine, C. Spear. “Commercial Solutions for Classified Layering Costs” Iowa State University as part of the INSuRE Project. 2014.

11. C. Martinez, R. Haverkos. “CSfC Risk Analysis” Purdue University as part of the INSuRE Project. 2014

12. F. Roeper, N. Ziring “Building Robust Security Solutions Using Layering and Independence” RSA Conference 2012.

13. J. Zage, R. Wells, M. Farnam "Risk Analysis of a Layered Solution", Purdue University as part of the INSuRE Project. May 1 2015.

14. R. Haverkos, D. Sokoler “The Impact of Known Vulnerabilities on Layered Solutions: A Timeline of Layered Solution Vulnerabilty”, Purdue University as part of the INSuRE Project. May 6 2016.

15. Saini, D. K. (2012). Cyber defense: mathematical modeling and simulation. International Journal of Applied Physics and Mathematics, 2(5), 312.

16. W. A. Arbaugh, W. L. Fithen and J. McHugh, "Windows of vulnerability: a case study analysis," in Computer, vol. 33, no. 12, pp. 52-59, Dec 2000.

17. Wen, S., Zhou, W., Zhang, J., Xiang, Y., Zhou, W., Jia, W., & Zou, C. C. (2014). Modeling and analysis on the propagation dynamics of modern email malware. IEEE transactions on dependable and secure computing, 11(4), 361-374.
