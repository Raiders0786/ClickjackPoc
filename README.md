# ClickJacking Vulnerability Scanner

- This tool will help you automate finding Clickjacking Vulnerability by just passing a file containing list of Targets .
- Once the Target is Found Vulnerable It will generate the Exploit Proof of Conepet(PoC) for each Vulnerable targets.

## What is Clickjacking ?

- Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
- The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. 
- Sites can use "X-Frame-Options" in the headers to avoid clickjacking attacks by ensuring that their content is not embedded into other sites.
- [Reference](https://owasp.org/www-community/attacks/Clickjacking)

## Features
- **Target-Based Scanning:** Automatically scans all targets listed in the provided file.
- **Exploit PoC Generation:** Creates an HTML-based Proof of Concept (PoC) file for each vulnerable target, saved as TargetName.html.
- **Comprehensive Reporting:** Clearly identifies and prints "Not Vulnerable" for targets that are secure.
- **Multithreading for Speed:** Leverages multithreading to perform rapid vulnerability scanning.
- **Slack Integration:** Sends real-time Slack alerts with attached PoC files for each vulnerable target.
- **Organized Results:** Stores all generated PoC files in a dedicated results folder, each named after the corresponding target.
- **Robust Error Handling:** Includes detailed logging and error management to ensure smooth operation and easy troubleshooting.

## Installation:
````
git clone https://github.com/Raiders0786/ClickjackPoc.git
cd ClickjackPoc
pip install -r requirements.txt
````

## Example:
Example Usage of the Tool
````
python3 clickJackPoc.py -f domains.txt
````

![1](usage.png)

## Allowed Targets Format:

````
http://target.com
target.com
www.target.com
https://tartget.com/
https://IP:Port
IP:Port
http://IP:Port/login
http://www.target.com/directory
https://www.target.com/directory
````

## Reach Me :
- `Do Tag Me if you get Rewarded💸💰 , Will be Very Happy to hear that 😄 !`
- Do Give it a `Star` if you like it & `Follow` me for more such stuffs!
- Let me know if you have any Suggestion's or want to Collaborate.
- This tool is made for Learning Purpose ! 


<a href="https://www.linkedin.com/in/chirag-agrawal-770488144/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" style="height: 50px !important;width: 170px !important;" ></a>
<img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/__Raiders?style=social" width="250" height="50">
