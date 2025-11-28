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

def gen_all(max_lenght=6):
    charset = string.ascii_uppercase + "0123456789"
    for lenght in range (1, max_lenght + 1):
        for p in product(charset, repeat=lenght):
            yield ''.join(p)

def cari_urut():
    g = gen_all(99)
    start = int(input("Mulai dari itirasi ke - "))

    for _ in range(start):
        next(g)
        print(f"Skipping {_} / {start}", end="\r")
    print("")
    print("-----")
    session = requests.Session()
    for i in range(start, 999999999):
        url = link + (next(g))
        r = session.head(url, allow_redirects=False)
        tujuan = r.headers.get("Location")
        print(f"Processing {i}", end="\r")
        if tujuan and tujuan[0:panjang_target] == target:
            try:
                print(f"({i}) - {tujuan} /// {url}")
            except:
                continue


pilihan = input("Pilihan Anda : ")

if pilihan == "1":
    with ThreadPoolExecutor(max_workers=50) as exe:
        results = list(exe.map(cari_urut))