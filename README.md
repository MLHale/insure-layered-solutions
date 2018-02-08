# Insure-layered-solutions
The Impact of Known Vulnerabilities on Layered Solutions Team Project
## Executive Project Summary
**Problem Statement**

This project is geared toward determining the security benefit of provided by a layered solution - for example, two VPNs, one tunneled within the other.  

Specially:

* Select two common (widely used) products that could be used to provide the two layers - routers, firewalls, VPN products, etc.
* Investigate the timeline of known vulnerabilities for those products, distinguishing between the time the vulnerability becomes known and the time it becomes patched (realizing that in many cases vulnerabilities are not publically known until the vendor announces a patch).  Limit oneself to those vulnerabilities that could have reasonably resulted in compromise of the security of the layer.  It is not necessary to prove that assertion, but be able to defend it based upon the nature of the vulnerability.  (e.g., results in root access, could allow one to disable a key service, weakens the crypto, etc.)
* Assume one week to apply a patch in the field once a patch is released as a starting point, but it is desirable to be able to adjust this value.
* Place the vulnerability timeline for the two VPNs on a common timeline and identify those instances where two VPN layers were vulnerable at the same.
* Separately, identify opportunities the adversary may have had to compromise the solution by using vulnerabilities that don't line up in time, but that could have afforded the opportunity to gain access to a single layer and simply wait for a vulnerability to become known in the second.  Vulnerabilities which allow the attacker to install malicious code on the device would be a prime example of the manner by which an attacker could take advantage of vulnerability in one layer, gain a foothold, and then wait for a vulnerability to become known in the second.
* To simplify the task, assume no monitoring for adversarial actions - in other words, the bad guys can act without being detected.  Also assume that the adversaries do not utilize zero day vulnerabilities which they themselves have discovered and that they do not create zero-day opportunities via such avenues as supply-chain attacks.
* Another desirable trait if time allows:  publically available reports may detail the amount of time it takes from a vulnerability being known to the availability of exploit code.  This may be a particularly short timeframe for patched vulnerabilities - analysis of the patch allows the attacker a method of determining just what function in a software package is faulted.    It would be desirable to include this value into the analysis in determining the susceptibility of the layered solution.

**Goals and Objectives**

* Extract data from NVD and CVE databases
* Model vulnerabilities, exploits, patches, and patch windows
* Construct timeline
* Code webpage
* Build database
* Correlate data

The purpose of layered solutions is to give the ability of an institution to use layered commercial products to deliver access to their critical data while maintaining security.  Traditionally, government devices were designed and certified to be used to access their most sensitive data.  This is extremely costly and time consuming.  Recently, the government has been reviewing proposals which would utilize commercial devices to deliver the same results as the government devices.  To increase the governments assurance, the government is attempting to ascertain if the use of multiple or layered solutions will provide the level of assurance that a government device would deliver.

This task will attempt to determine the security benefit of using layered solutions in an institution and if it affords any advantages.  The two layers being investigated will be enterprise vpn solutions.  It will be prudent to research the National Vulnerability Database and the Common Vulnerabilities and Exposures database in order to create a timeline of vulnerabilities for enterprise solutions over the years at varying code levels.  It will be important to distinguish between the time the vulnerability is known and the time when the patch is released.  There is also another aspect to take into account.  It cannot be assumed that when the patch is released, that this will be the time that the institutions devices would be patched.  There will need to be a patch window, in which, an institution would review, test, and assign the patch to a change management request.  The research will need to be limited to only vulnerabilities that could possibility compromise a security layer.  The timeline will be developed to aid in displaying overlapping vulnerabilities of the layered solutions selected, if they exist.

It will be also important to ascertain the possibility of an adversaries' ability to compromise layered solutions that do not have overlapping timelines.  This would involve an adversary's ability to compromise one layer and then wait until the other solution has a new vulnerability known to it.  History has shown, in many cases adversaries will gain some access and sit and wait until another opportunity presents itself.  

Lastly, it will be important to research how long it takes an exploit to be created once the vulnerability is known.  This information will be easily identified as the timeline is created with vulnerabilities, patches and available exploits of vpn solutions. It will be important to also point out if there have been successful exploits of these vulnerabilities, not just hypothesized exploits that should be possible.

This is type of research is extremely important to all institutions to help protect sensitive data and mitigate the adversaries' ability to breach their network.  By compiling all of this data and creating a timeline to analyze this data, the hope is to provide useful information to confirms or denies the advantage of introducing layered solutions into an institutions network security posture.




## Proposed project timeline
![screenshot](https://github.com/MLHale/insure-layered-solutions/blob/master/GantCharts/NewGeneralGant.png)
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
Arora, A., Krishnan, R., Telang, R., & Yang, Y. (2006). An empirical analysis of software vendors' patching behavior: Impact of vulnerability disclosure. ICIS 2006 Proceedings, 22.

Cohen, F. (1999). Simulating cyber attacks, defences, and consequences. Computers & Security, 18(6), 479-518.

“Commercial Solutions for Classified Program” National Security Agency, Information Assurance. 2012 https://www.nsa.gov/ia/programs/csfc_program/

“Common Vulnerabilities and Exposures”. MITRE. 2014. Available https://cve.mitre.org/

“Common Weakness Enumeration”. MITRE. 2015. Available https://cwe.mitre.org/

“cve-search Common Vulnerabilities and Exposures”. CIRCL. 2016. 

“National Vulnerability Database”. NIST. 2002. Available http://nvd.nist.gov

A. Arora, R. Krishnan, A. Handkumar, R. Telang, Y. Yang, "Impact of VUlnerability Disclosure and Patch Avalability – An Empirical Analysis" H. John Heinz III School of Public Policy and Management, Canregie Mellon University, April 2004.

Behannon, J. (2017, December 09). Cyberwar Surprise Attacks Get a Mathematical Treatment. Retrieved February 08, 2018, from http://www.sciencemag.org/news/2014/01/cyberwar-surprise-attacks-get-mathematical-treatment

C. Farrington, D. Hlavacek, E. Rodine, C. Spear. “Commercial Solutions for Classified Layering Costs” Iowa State University as part of the INSuRE Project. 2014.

C. Martinez, R. Haverkos. “CSfC Risk Analysis” Purdue University as part of the INSuRE Project. 2014

F. Roeper, N. Ziring “Building Robust Security Solutions Using Layering and Independence” RSA Conference 2012.

J. Zage, R. Wells, M. Farnam "Risk Analysis of a Layered Solution", Purdue University as part of the INSuRE Project. May 1 2015.

R. Haverkos, D. Sokoler “The Impact of Known Vulnerabilities on Layered Solutions: A Timeline of Layered Solution Vulnerabilty”, Purdue University as part of the INSuRE Project. May 6 2016.

Saini, D. K. (2012). Cyber defense: mathematical modeling and simulation. International Journal of Applied Physics and Mathematics, 2(5), 312.

W. A. Arbaugh, W. L. Fithen and J. McHugh, "Windows of vulnerability: a case study analysis," in Computer, vol. 33, no. 12, pp. 52-59, Dec 2000.

Wen, S., Zhou, W., Zhang, J., Xiang, Y., Zhou, W., Jia, W., & Zou, C. C. (2014). Modeling and analysis on the propagation dynamics of modern email malware. IEEE transactions on dependable and secure computing, 11(4), 361-374.

### Technical Plan
First vital step to this research project will be to define a set of enterprise vpn solutions.  Once the vpn solutions have been defined, a review of the National Vulnerability database and Common vulnerabilities and exposes database can be conducted.  In order to effectively extract data from the database the CIRCL CVE Search API will be utilized to collect as much data as possible about our VPN solutions and their vulnerabilities. A python script written by Matt Erasmus found on the CIRCL website appears to be the best option for collecting vulnerabilities separated by vendor. The data will need to be translated out of the JSON formatted output and another python script will be used in order to begin evaluating the vulnerabilities gathered and determine if they are relevant to this project. This evaluation will include searching for confirmed exploits, determining the impact on the layered solution, and collecting patch dates (if available). One definite possibility will be that one or more of our selected VPN providers may not have enough data available for inclusion in this project. This would result in removal from the vendor list.  Once the data set has been assembled and confident in the results, manual construction can begin by plotting the vulnerabilities on a timeline for each vendor and then compiling those timelines into a master. While compiling the timeline, programming will begin for our webpage which will be used it to display a vulnerability timeline based upon the selected vendors and search parameters.  Python and the Django web framework will be used for this site, barring any limitations found in the Django framework. The data will be held by a sql database.  The final step is to write documentation on the results and the webpage. Additionally, analysis of the overall exploitability of a layered VPN solution will be done and compared it to the vendor solutions. 


## Resources/Technology needed
|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|-------------------|---------|---------------------------|-------------|
|Web server | No | Joe White | A Web server with an appropriate software stack will be needed to host the website. |
|Database server | No | Joe White | A database server will be needed to store the data that is being collected from the NVD and CVE databases. |
|Virtual machines | No | Brian Mellon | Virtual environments will be needed to test VPNs and develop the web server. |
|Building Web App | YES | David Phillips | Coding the web application that will integrate with the database. |
## First Sprint Plan
![screenshot](https://github.com/MLHale/insure-layered-solutions/blob/master/GantCharts/ProposedProjectTimeline.png)
