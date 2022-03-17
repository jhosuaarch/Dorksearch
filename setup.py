import os

os.system("pip install cython")
os.system("gcc `python-config --cflags --idflags` -o dork dork.c `python-config --libs'")
os.remove("dork.c")

print("[!] Done")
