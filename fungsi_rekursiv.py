def rekursif(jumlah):
    if jumlah <= 0:
        return 0
    angka = int(input(f"Masukan angka ke-{jumlah}:"))
    return angka + rekursif(jumlah - 1)

jumlah = int(input("Masukan jumlah:"))
hasil = rekursif(jumlah)
print(f"Hasil:{hasil}")
