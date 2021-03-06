# The Impact of Known Vulnerabilities on Layered Solutions 

## Executive Project Summary

The purpose of layered solutions is to give the ability of an institution to use layered commercial products to deliver access to their critical data while maintaining security.  Traditionally, government devices were designed and certified to be used to access their most sensitive data.  This is extremely costly and time consuming.  Recently, the government has been reviewing proposals which would utilize commercial devices to deliver the same results as the government devices.  To increase the governments assurance, the government is attempting to ascertain if the use of multiple or layered solutions will provide the level of assurance that a government device would deliver.

This task will attempt to determine the security benefit of using layered solutions in an institution and if it affords any advantages.  The two layers being investigated will be enterprise VPN solutions.  It will be prudent to research the National Vulnerability Database and the Common Vulnerabilities and Exposures database in order to create a timeline of vulnerabilities for enterprise solutions over the years at varying code levels.  It will be important to distinguish between the time the vulnerability is known and the time when the patch is released.  There is also another aspect to take into account.  It cannot be assumed that when the patch is released, that this will be the time that the institutions devices would be patched.  There will need to be a patch window, in which, an institution would review, test, and assign the patch to a change management request.  The research will need to be limited to only vulnerabilities that could possibility compromise a security layer.  The timeline will be developed to aid in displaying overlapping vulnerabilities of the layered solutions selected, if they exist.

It will be also important to ascertain the possibility of an adversaries' ability to compromise layered solutions that do not have overlapping timelines.  This would involve an adversary's ability to compromise one layer and then wait until the other solution has a new vulnerability known to it.  History has shown, in many cases adversaries will gain some access and sit and wait until another opportunity presents itself.  

Lastly, it will be important to research how long it takes an exploit to be created once the vulnerability is known.  This information will be easily identified as the timeline is created with vulnerabilities, patches and available exploits of VPN solutions. It will be important to also point out if there have been successful exploits of these vulnerabilities, not just hypothesized exploits that should be possible.

This is type of research is extremely important to all institutions to help protect sensitive data and mitigate the adversaries' ability to breach their network.  By compiling all of this data and creating a timeline to analyze this data, the hope is to provide useful information to confirms or denies the advantage of introducing layered solutions into an institutions network security posture.

**Goals and Objectives**

* Extract data from NVD and CVE databases
* Model vulnerabilities, exploits, patches, and patch windows
* Construct timeline
* Code webpage
* Build database
* Correlate data

![UML](https://github.com/MLHale/insure-layered-solutions/blob/master/GantCharts/uml3.png)

## Proposed project timeline
![screenshot](https://github.com/MLHale/insure-layered-solutions/blob/master/GantCharts/NewImprovedGant.png)
## Risk list
| Risk Name (value) | Impact | Likelihood | Description |
|-------------------------------------------------------|--------|------------|:---------------------------------------------------------------------------------------------------------------------------------------:|
| Programming issues (64) | 8 | 8 | Any programming issues with the HTML webpage or the Python program will slow progress. |
|    Unable to find exploit and patch dates (63)        | 9 | 7 | If exploit and patch dates cannot be found or incorrect, the final results in the timeline will be off. |
| No vulnerability overlaps in timeline (56) | 8 | 7 | Problems could arise if the vulnerability timeline is not showing overlaps properly.    |
| Problems gathering data (18) | 6 | 3 | Any major issues scraping databases for information will not allow for the rest of the project to continue until data can be retrieved. |
| Team member availability (15) | 5 | 3 | Team members must be able to coordinate appropriate times to meet otherwise progress will be slowed. |
| CVEs not found (12) | 6 | 2 | The project will not work if relevant CVEs cannot be found for the Enterprise VPN solutions that have been chosen |

## Project Methodology
### Literature Review

R. Haverkos and D. Sokoler have done research on layered solutions as part of the INSuRE project. They considered the vulnerabilities of the two VPNs (Cisco AnyConnect and Juniper) and estimated a time window for the patches to those vulnerabilities. In this method, they have collected the data from the National Vulnerability Database and estimated the patch availabilities dates and then measured the windows of opportunities. The result was the development of a simulation considering the two security mechanisms as layered solutions. [14]

National Vulnerability Database(NVD) [7] contains the information of vulnerabilities on a wide range of products. This database contains the detailed information like the Common Vulnerabilities and Exposures(CVE) [4] identifier which is a unique identifier given to the vulnerability of the product.  Also, this database contains the published date of the vulnerability, references to advisories, and solutions and tools to vulnerability entry.  Each CVE has a rating from Common Vulnerability Scoring System(CVSS) which gives the severity level of the vulnerability.  Lastly, the Common Weakness Enumeration(CWE) [5] identifier which provides a method to qualitatively categorize these vulnerabilities and the summary description of the vulnerability. The base metric used to classify the severity and the outcomes of the vulnerabilities is based on the CVSS.

A. Arora, R. Krishnan, A. Handkumar, R. Telang, Y. Yang, made an attempt to empirically test the vulnerabilities disclosure and availability of how patches affect vendors and attackers. In their work they came to conclusion that at first, vendors are quick in disclosing the vulnerabilities which made it easier for the attacker to attack the product, but latter on the process of disclosing the vulnerabilities reduces the attacks. They gathered the vulnerabilities from the public domains like NVD, CERT, Bugtraq etc. [8]

In the RSA Conference [10] they talked about the layering security solutions. In data transmission highly, sensitive data requires a high level of assurance, this can be possible by several layers of authorization from different agencies. Traditionally, government devices were designed and certified in order to handle the most sensitive data. The adoption GOTS(Government-Off-The-Shelf) solutions provide high level of assurance but this has made high operating cost for developing the high assurance devices. National Security Agency(NSA) Central Security Service(CSS) has come up with a program known as Commercial Solutions for Classified (CSfC) program [3] to leverage the cost and to provide the same assurance as GOTS solutions. The principle of CSfC is that properly configured and layered solutions can provide sufficient protection for the classified data. Composition of the security mechanisms(layering) provides a high level of assurance then the individual mechanisms.


### Technical Plan
First vital step to this research project will be to define a set of enterprise VPN solutions.  Once the VPN solutions have been defined, a review of the National Vulnerability database and Common vulnerabilities and exposes database can be conducted.  In order to effectively extract data from the database the CIRCL CVE Search API will be utilized to collect as much data as possible about our VPN solutions and their vulnerabilities. A python script written by Matt Erasmus found on the CIRCL website appears to be the best option for collecting vulnerabilities separated by vendor. The data will need to be translated out of the JSON formatted output and another python script will be used in order to begin evaluating the vulnerabilities gathered and determine if they are relevant to this project. This evaluation will include searching for confirmed exploits, determining the impact on the layered solution, and collecting patch dates (if available). One definite possibility will be that one or more of our selected VPN providers may not have enough data available for inclusion in this project. This would result in removal from the vendor list.  Once the data set has been assembled and confident in the results, manual construction can begin by plotting the vulnerabilities on a timeline for each vendor and then compiling those timelines into a master. While compiling the timeline, programming will begin for our webpage which will be used it to display a vulnerability timeline based upon the selected vendors and search parameters.  Python and the Django web framework will be used for this site, barring any limitations found in the Django framework. The data will be held by a SQL database.  The final step is to write documentation on the results and the webpage. Additionally, analysis of the overall exploitability of a layered VPN solution will be done and compared it to the vendor solutions. 


## Resources/Technology needed
|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|-------------------|---------|---------------------------|-------------|
|Web server | No | Joe White | A Web server with an appropriate software stack will be needed to host the website. |
|Database server | No | Joe White | A database server will be needed to store the data that is being collected from the NVD and CVE databases. |
|Virtual machines | No | Brian Mellon | Virtual environments will be needed to test VPNs and develop the web server. |
|Building Web App | Yes | David Phillips, Sai Guru Karthik | Coding the web application that will integrate with the database. |
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

## Helpful Diagrams
![alt text](https://i.imgur.com/qPILImM.jpg "Problem Diagram")

This first diagram is a visualization of the question we are trying to answer. The blue and red "layers" represent two different VPN solutions in use and the black hat represents the attacker attempting to weave their way into the critical systems. However, it does not address a situation where an attacker can create permanent access through the first layer.

![alt text](https://i.imgur.com/oTHPUQs.jpg "Data Diagram")

This second diagram shows the life cycle of the data we are using to generate the vulnerabilty timelines for given vendors. The data starts at the CERT website and, through the use of some clever python scripts, ends in a web application database ready to be displayed on a timeline for the user to peruse. 
