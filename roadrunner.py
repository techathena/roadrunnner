import sys
def main():
    #a=len(sys.argv)
    #if ( a < 3 ):
      #  sys.stderr.write("E: usage :"+sys.argv[0]+"<argument variable>")
      #  sys.stderr.flush()
      #  exit(2)
    #else:
        scriptnam = sys.argv[1]
        exec(open("./"+scriptnam +".py").read())
if (__name__ == "__main__"):
    main()
