import sys
import requests
import socket
import json
import sys
import nmap
import requests

def reconissance():
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
  #print("location: "+ rep['locn'])
    print("region :"+rep['region'])
    print("city :"+rep["city"])
    print("country :"+rep["country"])

def portscan():
    print("enter the target")
    target = input()
    ports = [21,22,80,139,443,8080]
    scan_var= nmap.PortScanner()
    print("\n scanning"+target+"for the ports 21,22,80,139,443,8080")

    for port in ports:
        portscan =scan_var.scan(target,str(port))
        print (portscan)

def subdomain_enum():
      print("enter url to check: ")
      ipt=input()
      sub_list=open("subdomains-100.txt").read()
      subs=sub_list.splitlines()
      for sub in subs:
         urltocheck= r"http://"+str(sub)+str(ipt)
         try:
             requests.get(urltocheck)
    
         except requests.ConnectionError:
              pass
         else:
             print("valid domain :"+urltocheck)


def main():
  abs=''' ############### Roadrunner ####################'''
  print(abs)
  print("enter input")
  invel = input()
  if invel=="recon":
        reconissance()
        
  elif invel=="portsc":
        portscan()
        
  elif invel=="subd":
        subdomain_enum()
        


if __name__ == "__main__":
   main()
