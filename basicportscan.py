import sys
import nmap
target = str(sys.argv[1])
ports = [21,22,80,139,443,8080]

scan_var= nmap.PortScanner()
print("\n scanning"+target+"for the ports 21,22,80,139,443,8080")

for port in ports:
    portscan =scan_var.scan(target,str(port))
    print (portscan)

