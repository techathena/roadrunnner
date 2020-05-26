import sys
import requests
print("enter url to check: ")
ipt=input()
sub_list=open("subdomains-100.txt").read()
subs=sub_list.splitlines()
for sub in subs:
   urltocheck= f"http://(sub).[ipt]"
   try:
       requests.get(urltocheck)
    
   except requests.ConnectionError:
        pass
   else:
        print("calid domain :")
