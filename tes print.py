import time

for i in range(101):
    print(f"Loading {i}%", end="\r")
    time.sleep(0.05)

print()  # setelah selesai, pindah baris
