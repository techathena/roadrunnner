import sys
import requests
import socket
import json

print("enter the name of the site : ")
site=input()
if len(site)<2:
 print("use:"+sys.argv[0]+" <add_url>")
 sys.exit(1)
else:
  recv = requests.get("https://"+site)
  print("\n"+str(recv.headers))

  gethost = socket.gethostbyname(site)
  print("/n the ip address of requested site is "+ gethost)
  #ipinfo.io
  recv2 = requests.get("https://ipinfo.io/"+gethost+"/json")
  rep = json.loads(recv2.text)
  print("location: "+ rep['locn'])
  print("region :"+rep['region'])
  print("city :"+rep["city"])
  print("country :"+rep["country"])
