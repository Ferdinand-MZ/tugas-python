def Persegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi
    return luas,keliling

sisi = int(input('Masukkan Sisi : '))
luas,keliling = Persegi(sisi)
print('Sisi : ',sisi,' Luas : ',luas, 'Keliling : ',keliling)