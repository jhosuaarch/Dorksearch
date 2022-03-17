import os
import re
try:
     import requests
     from googlesearch import search as cari
     from enum import Enum
except ImportError:
     os.system("pip install requests")
     os.system("pip install google")


#color
r = "\033[1;91m"
g = "\033[1;32m"
w = "\033[1;97m"

banner = "a"

def main():
     try:
          dork = input("Enter Dork : ")
          limit = int(input("Page       : "))
          timer = (input("Time       : "))
          domain = input("Domain    : ")
          i = 0
          for url in cari(dork,tld=domain,lang="en",num=int(limit),start=0,stop=None,pause=int(timer),verify_ssl=False):
               i += 1
               print("{-{}({}{}{}) - {}".format(w,g,i,w,url))
               if i >= int(limit):
                    break

     except ValueError:
          print("{}[{}!{}] Must be a number".format(w,r,w))

if __name__ == '__main__':
     main()
