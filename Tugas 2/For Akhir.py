print('By Ferdinand Maulana Za Fauzi')

akhir = int(input('Masukkan Angka Akhir : '))
jumlah = 0
x = 1

for x in range(1, akhir + 1):
    if x % 2 == 1:
        jumlah += x

print(f'Jumlah Bilangan ganjil adalah {jumlah}')