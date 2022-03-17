import os

os.system("pip3 install cython")
os.system("gcc `python-config --cflags --ldflags` -o dork dork.c `python-config --libs`")
os.remove("dork.c")

print("[!] Done")
