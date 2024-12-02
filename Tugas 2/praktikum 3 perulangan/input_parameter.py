def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi

    print(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} : {luas}")

alas = float(input("Masukkan panjang alas segitiga : "))
tinggi = float(input("Masukkan tinggi segitiga : "))

hitung_luas_segitiga(alas,tinggi)