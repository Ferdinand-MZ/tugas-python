def cekHarga(jenis_makanan, rasa):
    harga = 0

    if jenis_makanan == "01":  # Martabak
        if rasa == "cokelat":
            harga = 20000
        elif rasa == "keju":
            harga = 25000
        elif rasa == "kismis":
            harga = 15000
        else:
            print("Rasa tidak dikenal untuk Martabak.")
            return None
        
    elif jenis_makanan == "02":  # Pukis
        if rasa == "cokelat":
            harga = 15000
        elif rasa == "keju":
            harga = 20000
        elif rasa == "kismis":
            harga = 15000
        else:
            print("Rasa tidak dikenal untuk Pukis.")
            return None

    else:
        print("Jenis makanan tidak dikenal.")
        return None

    return harga

# Inisialisasi
total_berbelanja = 0
keterangan = ""

while True:
    print("By Ferdinand MZ")
    print("\nMartabak :")
    print("1. Rasa Keju - RP 25000 (01R1XX)")
    print("2. Rasa Cokelat - RP 20000 (01R2XX)")
    print("3. Rasa Kismis - RP 15000 (01R3XX)")
    print("\nPukis")
    print("1. Rasa Keju - RP 20000 (02R1XX)")
    print("2. Rasa Cokelat - RP 15000 (02R2XX)")
    print("3. Rasa Kismis - RP 15000 (03R3XX)")
    print("\n2 digit terakhir untuk jumlah barang")

    kode = input("Masukkan 6 Karakter (contoh : 01R104) atau ketik 'exit' untuk keluar: ")

    if kode.lower() == 'exit':
        print("Terima kasih telah berbelanja!")
        break

    if len(kode) != 6:
        print("Input harus terdiri dari 6 karakter")
        continue 

    # Memisahkan bagian kode
    jenis_makanan = kode[0:2]
    pilihan_rasa = kode[2:4]
    jumlah_beli = int(kode[4:6])

    # Menentukan jenis makanan dan rasa
    if jenis_makanan == "01":
        jenis_makanan_nama = "Martabak"
        rasa = ""
        if pilihan_rasa == "R1":
            rasa = "cokelat"
        elif pilihan_rasa == "R2":
            rasa = "keju"
        elif pilihan_rasa == "R3":
            rasa = "kismis"
        else:
            rasa = "Rasa tidak dikenal"
    elif jenis_makanan == "02":
        jenis_makanan_nama = "Pukis"
        rasa = ""
        if pilihan_rasa == "R1":
            rasa = "cokelat"
        elif pilihan_rasa == "R2":
            rasa = "keju"
        elif pilihan_rasa == "R3":
            rasa = "kismis"
        else:
            rasa = "Rasa tidak dikenal"
    else:
        jenis_makanan_nama = "Jenis Makanan tidak dikenal"
        rasa = "Rasa tidak dikenal"

    harga_per_item = cekHarga(jenis_makanan, rasa)

    if harga_per_item is not None:
        total_harga = harga_per_item * jumlah_beli

        total_berbelanja += total_harga
        
        # Pengisian Keterangan
        keterangan += f"{jumlah_beli} x {jenis_makanan_nama} ({rasa.capitalize()}): Rp {total_harga}\n"
    else:
        print("Tidak dapat menghitung total harga karena input tidak valid.")
        continue

    # Menampilkan hasil
    print(f"Jenis Makanan: {jenis_makanan_nama}")
    print(f"Pilihan Rasa: {rasa.capitalize()}")
    print(f"Jumlah Beli: {jumlah_beli}")
    print(f"Total Harga: Rp {total_harga}")

    # Loop
    beli_lagi = input("Mau membeli lagi? (yes/no): ").strip().lower()
    if beli_lagi != 'yes':
        print("Terima kasih telah berbelanja!")
        
        print(f"\nTotal Belanja Anda: Rp {total_berbelanja}")
        
        print("\nDaftar Pembelian:")
        print(keterangan)
        
        break