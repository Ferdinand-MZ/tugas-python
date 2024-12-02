def hitungLuasdanKelilingPersegiPanjang(panjang,lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

n = int(input("Masukkan jumlah persegi yang ingin dihitung : "))

for i in range(n):
    print(f"\nPersegi Panjang ke-{i + 1}:")
    panjang = float(input("Masukkan Panjang : "))
    lebar = float(input("Masukkan Lebar : "))

    luas, keliling = hitungLuasdanKelilingPersegiPanjang(panjang,lebar)

    print(f"Luas Persegi Panjang : {luas}")
    print(f"Keliling Persegi Panjang : {keliling}")