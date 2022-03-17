import os

os.system("pip install cython")
os.system("gcc `python-config --cflags --ldflags` -o dork dork.c `python-config --libs`")
os.remove("dork.c")

print("[!] Done")
