import sys
import requests
import socket
import json


if len(sys.argv)<2:
 print("use:"+sys.argv[0]+" <add_url>")
 sys.exit(1)

recv = requests.get("https://"+sys.argv[1])
print("\n"+str(recv.headers))

gethost = socket.gethostbyname(sys.argv[1])
print("/n the ip address of requested site is "+ gethost)
#ipinfo.io
recv2 = requests.get("https://ipinfo.io/"+gethost+"/json")
rep = json.loads(recv2.text)
print("location: "+ rep['locn'])
print("region :"+rep['region'])
print("city :"+rep["city"])
print("country :"+rep["country"])
