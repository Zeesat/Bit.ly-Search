import webbrowser
import subprocess
import requests
import random
import string
from itertools import product
from concurrent.futures import ThreadPoolExecutor

link = input("Input short link (Default: https://bit.ly/* ): " )

if link == "":
    link = "https://bit.ly/"

target = input("Input target link (Default: https://drive.google.com/drive/* ): ")

if target == "":
    target = "https://drive.google.com/drive/"

panjang_target = len(target)

print('''Pilih metode pencarian : 
      1. Urut dari A-ZZZ
      2. Spesifik character lenght (Random)
      3. Spesifik character lenght (A-Z)
      4. Berdasarkan word disimpan
      5. Algoritma vokal''')

ditemukan = []
charset = string.ascii_uppercase + "0123456789"
def gen_all(max_lenght=6):
    for lenght in range (1, max_lenght + 1):
        for p in product(charset, repeat=lenght):
            yield ''.join(p)

# def skipping():
#     g = gen_all(99)
#     start = int(input("Mulai dari itirasi ke - "))
#     for _ in range(start):
#         next(g)
#         print(f"Skipping {_} / {start}", end="\r")

#     print("")
#     print("-----")

session = requests.Session()
def cari_urut(code):
    url = link + code
    r = session.head(url, allow_redirects=False)
    if r.status_code in (301, 302):
        location = r.headers.get("Location", "")
        if location.startswith(target):
            found = location
            with open ("found.txt", "a", encoding="utf-8") as f:
                f.write(found + "\n")
                
    print(url, location)
    return r.status_code    




pilihan = input("Pilihan Anda : ")

if pilihan == "1":
    with ThreadPoolExecutor(max_workers=10) as exe:
        for status_code in exe.map(cari_urut, gen_all()):
            print(gen_all())
            pass
