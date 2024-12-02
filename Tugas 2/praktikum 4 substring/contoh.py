kode = input("Masukkan 6 Karakter (contoh : 01A504): ")

if len(kode) != 6:
    print("Input harus terdiri dari 6 karakter")
    exit()

jenis_buku = kode[0:2]
nomor_rak = kode[2:4]
jumlah_buku = int(kode[4:6])

if jenis_buku == "01":
    jenis_buku_nama = "Buku Sains"
elif jenis_buku == "02":
    jenis_buku_nama = "Buku Cerita"
elif jenis_buku == "03":
    jenis_buku_nama = "Buku Komputer"
else:
    jenis_buku_nama = "Jenis buku tidak dikenal"

print(f"Jenis Buku: {jenis_buku_nama}")
print(f"Nomor Rak: {nomor_rak}")
print(f"Jumlah Buku: {jumlah_buku}")