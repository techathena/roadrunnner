import sys
import nmap
print("enter the target")

target = input()
ports = [21,22,80,139,443,8080]

scan_var= nmap.PortScanner()
print("\n scanning"+target+"for the ports 21,22,80,139,443,8080")

for port in ports:
    portscan =scan_var.scan(target,str(port))
    print (portscan)
