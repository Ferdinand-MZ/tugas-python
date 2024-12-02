def HitungSPP(angkatan,sks):
    biaya = 0

    if angkatan == 2021:
        biaya = 100000
    elif angkatan == 2020:
        biaya = 80000
    elif angkatan == 2019:
        biaya = 60000
    else:
        print("Pilihan anda tidak valid !!!")

    return sks*biaya

nama = input("Masukkan Nama anda : ")
print("\nPilih Angkatan yang ingin dipilih:")
print("2021")
print("2020")
print("2019")
angkatan = int(input("Masukkan pilihan Angkatan : "))
sks = int(input("Masukkan Berapa banyak SKS : "))

spp = HitungSPP(angkatan, sks)

print(f"Nama : {nama}")
print(f"Tahun Angkatan : {angkatan}")
print(f"Total Biaya SPP : {spp}")