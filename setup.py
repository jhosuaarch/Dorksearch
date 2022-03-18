import os

os.system("pkg install termux-elf-cleaner");os.system("pip install cython")
os.system("gcc `python-config --cflags --ldflags` -o dork dork.c `python-config --libs`")
os.remove("dork.c");os.system("termux-elf-cleaner dork")

print("[!] Done")
