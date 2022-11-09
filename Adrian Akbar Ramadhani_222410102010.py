#Game tebak-tebakan angka
#Nama : Adrian Akbar Ramadhani
#NIM  : 222410102010
#Prodi: Teknologi Informasi

import random

jumlahtebakan = 0
namauser = input("Selamat datang, silahkan ketikan nama kamu: ")
print()
angka = random.randint(0, 100)
print(namauser + "", "silahkan menebak angka secara acak (0-100), batas menebak hanya 7 kali :)")
print()

for percobaan in range(1, 8):
    print("Ayo coba tebak!")
    angkauser = int(input("Masukan angka: "))
    jumlahtebakan += 1
    if angkauser > angka:
        print("Tidak tepat, angka terlalu besar")
        print()
    elif angkauser < angka:
        print("Tidak tepat, angka terlalu kecil")
        print()
    else:
        break

if angkauser == angka:
    print()
    print("Selamat " + namauser + " tebakan anda tepat, anda menebak sebanyak", jumlahtebakan, "kali")
else:
    print()
    print("Maaf " + namauser + " anda kurang beruntung")