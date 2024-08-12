# 🚨 ClickJacking Vulnerability Scanner 🚨

- This **Python-based** tool automates the detection of ClickJacking vulnerabilities by scanning a list of targets provided in a file.
- For each vulnerable target found, it generates an Exploit Proof of Concept (PoC) in the form of an HTML file.
- The tool is **completely working** and has been thoroughly **tested** for reliability and accuracy.

## What is ClickJacking? 🤔
- ClickJacking (also known as User Interface redress attack, UI redress attack, or UI redressing) is a malicious technique where a web user is tricked into clicking on something different from what they perceive, potentially revealing confidential information or taking control of their computer while interacting with seemingly harmless web pages.
- A server that doesn’t return an `X-Frame-Options header` is vulnerable to ClickJacking attacks. The `X-Frame-Options` HTTP response header is used to indicate whether a browser should be allowed to render a page within a `<frame> or <iframe>`.
- Websites can prevent ClickJacking attacks by using the `X-Frame-Options` header to ensure their content isn’t embedded in other sites.

[Learn more on OWASP](https://owasp.org/www-community/attacks/Clickjacking)

## ⚡ Features
- **🎯 Target-Based Scanning:** Automatically scans all targets listed in the provided file.
- **🛠️ Exploit PoC Generation:** Creates an HTML-based Proof of Concept (PoC) file for each vulnerable target, saved as TargetName.html.
- **✅ Comprehensive Reporting:** Clearly identifies and prints "Not Vulnerable" for targets that are secure.
- **🚀 Multithreading for Speed:** Leverages multithreading to perform rapid vulnerability scanning.
- **🔔 Slack Integration:** Sends real-time Slack alerts with attached PoC files for each vulnerable target.
- **📁 Organized Results:** Stores all generated PoC files in a dedicated results folder, each named after the corresponding target.
- **🔧 Robust Error Handling:** Includes detailed logging and error management to ensure smooth operation and easy troubleshooting.

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

## 🎯 Allowed Targets Format:

````
http://target.com
target.com
www.target.com
https://target.com/
https://IP:Port
IP:Port
http://IP:Port/login
http://www.target.com/directory
https://www.target.com/directory
````

## 🌟 Reach Me:

- **💬 Tag Me** if you get rewarded 💸💰—I’d love to hear about your success! 😄
- If you find this tool useful, please give it a **Star** ⭐ and **Follow** me for more cool projects!
- Feel free to reach out if you have any suggestions or want to collaborate.
- **⚠️ Note**: This tool is intended for **learning purposes** only.


<a href="https://www.linkedin.com/in/chirag-agrawal-770488144/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" style="height: 50px !important;width: 170px !important;" ></a>
<img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/__Raiders?style=social" width="250" height="50">
