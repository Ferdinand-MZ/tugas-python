print('By Ferdinand Maulana Za Fauzi')

harga = 1000
totalAkhir = 0
while True:
    beli = int(input('Masukkan Jumlah Beli : '))
    total = harga*beli
    totalAkhir += total
    print(f'Total Akhir : {totalAkhir}')
    lagi = input('Apa mau Beli lagi ?[Y/N] ')
    if lagi == 'N' or lagi == 'n' or lagi == 'no' :
        break