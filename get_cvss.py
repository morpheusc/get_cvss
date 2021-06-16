import sys
import requests
import json
import time
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print('Enter File Name (E.g. python3 bulk_cve_lookup.py cve.txt)')
    exit()

with open(sys.argv[1], "r") as cve_file:
       lines = cve_file.readlines()

       cve_list = []
       
       for l in lines:
                 as_list = l.split(", ")
                 cve_list.append(as_list[0].replace("\n", ""))
      
       
       
print("CVE-ID,","CVSS 3 Base Score,","CVSS 2 Base Score")

for CVEs in cve_list:
    response = requests.get('https://nvd.nist.gov/vuln/detail/'+str(CVEs))
    soup = BeautifulSoup(response.content, 'html.parser')
    
    try:
        test1 = (soup.find_all('a')[41].get_text())
       
        
        if  any (c.isdigit() for c in test1):
            print(CVEs,",",soup.find_all('a')[40].get_text(),",",soup.find_all('a')[41].get_text())
        else:
            print(CVEs,",","N/A",",","N/A")
    
    except:
        None
