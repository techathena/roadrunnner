import argparse
from subprocess import call

def main():
    
    #parser initialisation
    parser = argparse.ArgumentParser()
    
    #adding arguments
    parser.add_argument("-r","--reconissance",help="rus the reconissance script")
    parser.add_argument("-p","--portscan",help="runs the portscanner")

    #parsing args
    args= parser.parse_args()
     
    if args.reconissance:
         call("basicportscan.py")
    elif args.portscan:
        call("reconissance.py")
    else:
        pass

if __name__ == "__main__":
   main()
