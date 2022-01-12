#!/usr/bin/python3

from urllib.request import Request, urlopen
import argparse
from sys import exit
import urllib
import requests
import urllib.request
from termcolor import colored
from urllib.parse import urlparse

print('''                                                            
  ____ _     ___ ____ _  __  _            _            
 / ___| |   |_ _/ ___| |/ / (_) __ _  ___| | __  
| |   | |    | | |   | ' /  | |/ _` |/ __| |/ /  
| |___| |___ | | |___| . \  | | (_| | (__|   <   
 \____|_____|___\____|_|\_\_/ |\__,_|\___|_|\_\/       
                          |__/            
                            
                          By: Chirag Agrawal
    Reach me :-
            {+} Twitter: __Raiders
            {+} Github : Raiders0786

#################### --Starting Test's-- ####################
''')
parser = argparse.ArgumentParser(
    description='This Tool will automate & Check if the List of URLs in the file are Vulnerable to Clickjacking Attack & will make a POC for the Vulnerable URL')
parser.add_argument(
    "-f", type=str, help="Pass a list of Domains stored in a File", required=True)

content = parser.parse_args()

d = open(content.f, 'r')
hdr = {'User-Agent': 'Mozilla/5.0'}

try:
    for target in d.readlines():
        t = target.strip('\n')
        if (("http") or ("https")) not in t:
            t = "https://"+t  
        try:
            req = Request(t, headers=hdr)
            data = urlopen(req, timeout=10)
            filename = urlparse(t).netloc
            headers = data.info()
            if not (("X-Frame-Options") or ("x-frame-options")) in headers:
                vuln = True
                print(colored(f"Target: {t} is Vulnerable", "green"))
                print(colored(f"Generating {filename}.html POC File", "yellow"))
                poc = """
                    <html>
                    <head><title>Clickjack POC page</title></head>
                    <body>
                    <p>Website is vulnerable to clickjacking!</p>
                    <iframe src="{}" width="500" height="500"></iframe>
                    </body>
                    </html>
                    """.format(t)
                if ":" in filename:
                    url = filename.split(':')
                    filename=url[0]              
                with open(filename+".html", "w") as pf:
                    pf.write(poc)
                print(colored(f"Clickjacking POC file Created SuccessFully, Open {filename}.html to get the POC", "blue"))
            else:
                vuln == False
                print(colored(f"Target: {t} is not Vulnerable", "red"))
                print("Testing Other Url's in the List")
        except KeyboardInterrupt as k:
            print("No Worries , I'm here to handle your KeyBoard Interrupts \n")
        except urllib.error.URLError as e:
            # handling HTTP 403 Forbidden timeout...
            print(
                f"Target {t} has some HTTP Errors via http:// lets let https:// ", exception)
        except requests.HTTPError as exception:
            print(f"Target {t} has some HTTP Errors :--> ", exception)
        except Exception as e:
            print("Exception Occured with Description ----> ", e)
            raise("Target Didn't Responsed")
    print("All Targets Tested Successfully !!")
except:
    print("[*] Usage: python3 clickJackPoc.py -f <file_name>")
    print("[*] The Code might not worked for you , please retry & try --help option to know more")
    exit(0)
