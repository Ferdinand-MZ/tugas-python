def Persegi():
    sisi = int(input('Masukkan Sisi : '))
    luas = sisi*sisi
    keliling = 4*sisi
    return luas,keliling

luas,keliling = Persegi()
print('Luas : ',luas,'Keliling : ',keliling)