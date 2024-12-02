print('By Ferdinand Maulana Za Fauzi')

harga_barang_a = 1000
harga_barang_b = 2000
harga_barang_c = 3000
totalAkhir = 0

while True:
    print("Pilih Item yang ingin dipilih : ")
    print("1. Barang A - RP 1000 ")
    print("2. Barang B - RP 2000 ")
    print("3. Barang C - RP 3000 ")

    pilihan = input("Masukkan pilihan item (1/2/3): ")
    
    if pilihan == '1':
        harga = harga_barang_a
    elif pilihan == '2':
        harga = harga_barang_b
    elif pilihan == '3':
        harga = harga_barang_c
    else:
        print('Pilihan Tidak Valid, silahkan pilih 1, 2 atau 3.')
        continue

    beli = int(input('Masukkan jumlah beli : '))
    total = harga * beli
    totalAkhir += total
    print(f'Total Akhir : Rp {totalAkhir}')

    lagi = input('Apa mau beli lagi ? [Y/N]: ')
    if lagi == 'N' or lagi == 'n':
        break

print(f'Terima Kasih! Total belanja Anda adalah Rp {totalAkhir}.')

