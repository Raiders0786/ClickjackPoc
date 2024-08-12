#!/usr/bin/python3

from urllib.request import Request, urlopen
import argparse
import urllib.error
from sys import exit
from termcolor import colored
from urllib.parse import urlparse
import os
import concurrent.futures
import queue
import threading
import subprocess

# Slack Bot Token and Channel ID
VW_SLACK_TOKEN = 'SLACK_BOT_TOKEN_WITH_WRITE_INCOMING_HOOK_ACCESS'
VW_SLACK_CHANNEL = 'CHANNEL_ID_HERE'

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

#################### Testing Started ####################
''')

vuln = False
parser = argparse.ArgumentParser(
    description='This Tool will automate & Check if the List of URLs in the file are Vulnerable to Clickjacking Attack & will make a POC for the Vulnerable URL')
parser.add_argument(
    "-f", type=str, help="Pass a list of Domains stored in a File", required=True)

content = parser.parse_args()

hdr = {'User-Agent': 'Mozilla/5.0'}

# Use an existing results directory or create it if it doesn't exist
results_dir = 'results'

if not os.path.exists(results_dir):
    try:
        os.makedirs(results_dir)
        log_file = open(f'{results_dir}/log.txt', 'w')
    except OSError as e:
        print(f"Error creating directory {results_dir}: {e}")
        exit(1)
else:
    log_file = open(f'{results_dir}/log.txt', 'a')  # Append to the existing log file

# Set to track domains that have been alerted on Slack
reported_domains = set()

# Thread-safe queue to hold results
result_queue = queue.Queue()

def send_to_slack_worker():
    while True:
        item = result_queue.get()
        if item is None:  # None is the signal to stop the worker
            break
        domain, poc_filename, serial_no = item
        send_to_slack(domain, poc_filename, serial_no)
        result_queue.task_done()

def send_to_slack(domain, poc_filename, serial_no):
    try:
        # Remove 'http://' or 'https://' from the domain and format the title
        clean_domain = domain.replace('http://', '').replace('https://', '')

        # Command to send the file and message to Slack using curl
        command = [
            "curl",
            "-F", f"file=@{poc_filename}",
            "-F", f"initial_comment=*ClickJacking Vulnerability Detected for {clean_domain}*\n>Exploit code file that contains the .html code is attached below.",
            "-F", f"channels={VW_SLACK_CHANNEL}",
            "-H", f"Authorization: Bearer {VW_SLACK_TOKEN}",
            "https://slack.com/api/files.upload"
        ]

        # Execute the curl command
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print(colored(f"{serial_no}. Exploit Code for {domain} sent to Slack successfully.", "blue"))
        else:
            raise ValueError(f"Curl command failed: {result.stderr}")

    except Exception as e:
        print(f"Error sending file to Slack: {e}")
        log_file.write(f"Error sending file to Slack for {domain}: {e}\n")

def check_domain(t, serial_no):
    if not t.startswith(('http://', 'https://')):
        t = "https://" + t  # Assuming https if no scheme is provided

    try:
        req = Request(t, headers=hdr)
        response = urlopen(req, timeout=10)
        status_code = response.getcode()

        if status_code == 200:
            filename = urlparse(t).netloc
            headers = response.info()

            if 'X-Frame-Options' not in headers and 'x-frame-options' not in headers:
                vuln = True
                print(colored(f"{serial_no}. Target: {t} is Vulnerable", "green"))
                print(colored(f"Generating {filename}.html Exploit Code File", "yellow"))

                poc = f"""
                <html>
                <head><title>Clickjack Exploit Code page</title></head>
                <body>
                <p>Website is vulnerable to clickjacking!</p>
                <iframe src="{t}" width="500" height="500"></iframe>
                </body>
                </html>
                """

                if ":" in filename:
                    filename = filename.split(':')[0]

                poc_filename = f"{results_dir}/{filename}.html"
                with open(poc_filename, "w") as pf:
                    pf.write(poc)

                print(colored(f"{serial_no}. Clickjacking Exploit Code file Created Successfully, Open {poc_filename} to get the Exploit Code", "blue"))

                # Add the result to the queue
                result_queue.put((t, poc_filename, serial_no))

            else:
                print(colored(f"{serial_no}. Target: {t} is not Vulnerable", "red"))
                print("Testing Other URLs in the List")
        else:
            print(colored(f"{serial_no}. Target: {t} is not active, status code: {status_code}", "red"))
            log_file.write(f"Target {t} is not active, status code: {status_code}\n")

    except KeyboardInterrupt:
        print("No Worries, I'm here to handle your Keyboard Interrupts\n")
        return
    except urllib.error.URLError as e:
        print(colored(f"{serial_no}. Target {t} is unreachable: {e.reason}", "red"))
        log_file.write(f"Target {t} is unreachable: {e.reason}\n")
    except Exception as e:
        print(f"{serial_no}. Exception Occurred with Target {t}: {e}")
        log_file.write(f"Exception Occurred with Target {t}: {e}\n")

def main():
    # Start the worker thread
    threading.Thread(target=send_to_slack_worker, daemon=True).start()

    try:
        with open(content.f, 'r') as d:
            targets = [target.strip('\n') for target in d.readlines()]

        # Process domains concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            for serial_no, target in enumerate(targets, start=1):
                executor.submit(check_domain, target, serial_no)

        # Wait for the queue to be empty before exiting
        result_queue.join()
        print("All Targets Tested Successfully !!")

    except Exception as e:
        print(f"Error: {e}")
        print("[*] Usage: python3 clickJackPoc.py -f <file_name>")
        print("[*] The Code might not have worked for you, please retry & try the --help option to know more")
    finally:
        # Stop the worker thread
        result_queue.put(None)
        log_file.close()
        exit(0)

if __name__ == "__main__":
    main()

