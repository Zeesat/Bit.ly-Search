from concurrent.futures import ThreadPoolExecutor
from functools import partial
from itertools import product
from pathlib import Path
import string

import requests

DEFAULT_SHORT_LINK = "https://bit.ly/"
DEFAULT_TARGET_LINK = "https://drive.google.com/drive/"
CHARSET = string.ascii_uppercase + string.digits
MAX_WORKERS = 10
FOUND_FILE = Path(__file__).resolve().parents[2] / "data" / "found.txt"

session = requests.Session()


def gen_all(max_length: int = 6):
    for length in range(1, max_length + 1):
        for part in product(CHARSET, repeat=length):
            yield "".join(part)


def save_found(location: str) -> None:
    FOUND_FILE.parent.mkdir(parents=True, exist_ok=True)
    with FOUND_FILE.open("a", encoding="utf-8") as file:
        file.write(location + "\n")


def cari_urut(code: str, link: str, target: str) -> int:
    url = link + code
    response = session.head(url, allow_redirects=False)
    location = response.headers.get("Location", "")

    if response.status_code in (301, 302) and location.startswith(target):
        save_found(location)

    print(url, location)
    return response.status_code


def show_menu() -> str:
    print(
        """Pilih metode pencarian :
      1. Urut dari A-ZZZ
      2. Spesifik character lenght (Random)
      3. Spesifik character lenght (A-Z)
      4. Berdasarkan word disimpan
      5. Algoritma vokal"""
    )
    return input("Pilihan Anda : ").strip()


def main() -> None:
    link = input(f"Input short link (Default: {DEFAULT_SHORT_LINK}* ): ").strip()
    if not link:
        link = DEFAULT_SHORT_LINK

    target = input(f"Input target link (Default: {DEFAULT_TARGET_LINK}* ): ").strip()
    if not target:
        target = DEFAULT_TARGET_LINK

    pilihan = show_menu()
    if pilihan != "1":
        print("Metode ini belum diimplementasikan.")
        return

    search_func = partial(cari_urut, link=link, target=target)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for _ in executor.map(search_func, gen_all()):
            pass


if __name__ == "__main__":
    main()
