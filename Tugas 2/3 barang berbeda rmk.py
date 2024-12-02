print('By Ferdinand Maulana Za Fauzi')

harga_barang_a = 1000
harga_barang_b = 2000
harga_barang_c = 3000
totalAkhir = 0

jumlah_barang_a = 0
jumlah_barang_b = 0
jumlah_barang_c = 0

while True:
    print("Pilih Item yang ingin dipilih : ")
    print("1. Barang A - RP 1000 ")
    print("2. Barang B - RP 2000 ")
    print("3. Barang C - RP 3000 ")

    pilihan = input("Masukkan pilihan item (1/2/3): ")
    jumlah = int(input("Masukkan Jumlah Beli item : "))

    if pilihan == '1':
        harga = harga_barang_a
        jumlah_barang_a += jumlah
    elif pilihan == '2':
        harga = harga_barang_b
        jumlah_barang_b += jumlah
    elif pilihan == '3':
        harga = harga_barang_c
        jumlah_barang_c += jumlah
    else:
        print('Pilihan Tidak Valid, silahkan pilih 1, 2 atau 3.')

        continue

    total = harga * jumlah
    totalAkhir += total
    print(f'Total Akhir : Rp {totalAkhir}')

    lagi = input('Apa mau beli lagi ? [Y/N]: ')
    if lagi == 'N' or lagi == 'n':
        break

print(f'\nJumlah Pembelian:')
print(f'Barang A: {jumlah_barang_a} item')
print(f'Barang B: {jumlah_barang_b} item')
print(f'Barang C: {jumlah_barang_c} item')

print(f'Terima Kasih! Total belanja Anda adalah Rp {totalAkhir}.')