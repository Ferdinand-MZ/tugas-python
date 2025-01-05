def hitungTunjangan(golongan, jumlahAnak):
    
    if golongan == 1:
        gaji_pokok = 1000000
    elif golongan == 2:
        gaji_pokok = 1500000
    elif golongan == 3:
        gaji_pokok = 2000000
    else:
        print("Pilihan anda tidak valid !!!")

    if jumlahAnak >= 2:
        tunjanganAnak = 0.05 * gaji_pokok * 2
    elif jumlahAnak == 1:
        tunjanganAnak = 0.05 * gaji_pokok
    else:
        tunjanganAnak = 0

    total_gaji = gaji_pokok + tunjanganAnak

    return total_gaji

print("\nPilih Golongan Anda :")
print("Golongan 1")
print("Golongan 2")
print("Golongan 3")
golongan = int(input("\nMasukkan golongan Anda : "))
jumlahAnak = int(input("Masukkan Jumlah Anak yang dimiliki : "))

total_gaji = hitungTunjangan(golongan, jumlahAnak)

print(f"Total Gaji yang Anda Miliki adalah : ",total_gaji)
