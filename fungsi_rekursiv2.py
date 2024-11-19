def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        return base * power(base, exp - 1)

base = int(input("Masukan angka dasar(base):"))
exp = int(input("Masukan pangkat (exponent):"))

hasil = power(base, exp)
print(f"Hasil {base} pangkat {exp} adalah {hasil}")