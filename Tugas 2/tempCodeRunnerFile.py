print('By Ferdinand Maulana Za Fauzi')

harga = 0
martabak_cokelat = 20000
martabak_keju = 25000
martabak_kismis = 15000
pukis_cokelat = 15000
pukis_keju = 20000
pukis_kismis = 15000
totalAkhir = 0

jumlah_mc = 0
jumlah_mk = 0
jumlah_mks = 0
jumlah_pc = 0
jumlah_pk = 0
jumlah_pks = 0

while True:
    print("\nPilih Item yang ingin dipilih:")
    print("1. Martabak - RP 15000-25000")
    print("2. Pukis - RP 15000-20000")
    print("3. Selesai dan Tampilkan Total")

    pilihan = int(input("Masukkan pilihan item (1/2/3): "))

    if pilihan == 1:
        while True:
            print("\nPilih Rasa Martabak yang ingin dipilih:")
            print("1. Keju - RP 25000")
            print("2. Cokelat - RP 20000")
            print("3. Kismis - RP 15000")
            print("4. Kembali ke menu utama")
            pilihanm = int(input("Masukkan pilihan rasa (1/2/3/4): "))

            if pilihanm == 4:
                break
            elif pilihanm in [1, 2, 3]:
                jumlah = int(input("Masukkan jumlah item: "))
                if pilihanm == 1:
                    harga = martabak_keju
                    jumlah_mk += jumlah
                elif pilihanm == 2:
                    harga = martabak_cokelat
                    jumlah_mc += jumlah
                elif pilihanm == 3:
                    harga = martabak_kismis
                    jumlah_mks += jumlah

                total = harga * jumlah
                totalAkhir += total
                print(f'\nSubtotal untuk pesanan ini: Rp {total}')
                print(f'Total sementara: Rp {totalAkhir}')
            else:
                print("Pilihan tidak valid, ulangi lagi.")
                continue

    elif pilihan == 2:
        while True:
            print("\nPilih Rasa Pukis yang ingin dipilih:")
            print("1. Keju - RP 20000")
            print("2. Cokelat - RP 15000")
            print("3. Kismis - RP 15000")
            print("4. Kembali ke menu utama")
            pilihanp = int(input("Masukkan pilihan rasa (1/2/3/4): "))

            if pilihanp == 4:
                break
            elif pilihanp in [1, 2, 3]:
                jumlah = int(input("Masukkan jumlah item: "))
                if pilihanp == 1:
                    harga = pukis_keju
                    jumlah_pk += jumlah
                elif pilihanp == 2:
                    harga = pukis_cokelat
                    jumlah_pc += jumlah
                elif pilihanp == 3:
                    harga = pukis_kismis
                    jumlah_pks += jumlah

                total = harga * jumlah
                totalAkhir += total
                print(f'\nSubtotal untuk pesanan ini: Rp {total}')
                print(f'Total sementara: Rp {totalAkhir}')
            else:
                print("Pilihan tidak valid, ulangi lagi.")
                continue

    elif pilihan == 3:
        break

    else:
        print("Pilihan tidak valid, ulangi lagi.")
        continue

print("\nJumlah Pembelian:")
if jumlah_mc > 0:
    print(f"Martabak Cokelat: {jumlah_mc} item")
if jumlah_mk > 0:
    print(f"Martabak Keju: {jumlah_mk} item")
if jumlah_mks > 0:
    print(f"Martabak Kismis: {jumlah_mks} item")
if jumlah_pc > 0:
    print(f"Pukis Cokelat: {jumlah_pc} item")
if jumlah_pk > 0:
    print(f"Pukis Keju: {jumlah_pk} item")
if jumlah_pks > 0:
    print(f"Pukis Kismis: {jumlah_pks} item")

print(f"\nTerima kasih! Total belanja Anda adalah Rp {totalAkhir}.")
