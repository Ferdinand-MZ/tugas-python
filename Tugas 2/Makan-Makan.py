print('By Ferdinand Maulana Za Fauzi')

# Harga menu
menu_items = {
    "martabak": {"keju": 25000, "cokelat": 20000, "kismis": 15000},
    "pukis": {"keju": 20000, "cokelat": 15000, "kismis": 15000}
}

# Jumlah pembelian
jumlah_pesanan = {
    "martabak": {"keju": 0, "cokelat": 0, "kismis": 0},
    "pukis": {"keju": 0, "cokelat": 0, "kismis": 0}
}

total_akhir = 0


def tampilkan_menu_utama():
    print("\nPilih Item yang ingin dipilih:")
    print("1. Martabak - RP 15000-25000")
    print("2. Pukis - RP 15000-20000")
    print("3. Selesai dan Tampilkan Total")


def pilih_rasa(item):
    print(f"\nPilih Rasa {item.capitalize()} yang ingin dipilih:")
    rasa = list(menu_items[item].keys())
    for i, r in enumerate(rasa, 1):
        print(f"{i}. {r.capitalize()} - RP {menu_items[item][r]}")
    print(f"{len(rasa) + 1}. Kembali ke menu utama")
    return rasa


def masukkan_jumlah(rasa):
    while True:
        try:
            return int(input(f"Masukkan jumlah {rasa.capitalize()} yang ingin dibeli: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")


def proses_pesanan(item):
    global total_akhir
    rasa_list = pilih_rasa(item)
    while True:
        try:
            pilihan_rasa = int(input(f"Masukkan pilihan rasa (1-{len(rasa_list) + 1}): "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue

        if pilihan_rasa == len(rasa_list) + 1:
            break
        elif 1 <= pilihan_rasa <= len(rasa_list):
            rasa = rasa_list[pilihan_rasa - 1]
            jumlah = masukkan_jumlah(rasa)
            harga = menu_items[item][rasa]
            jumlah_pesanan[item][rasa] += jumlah
            subtotal = harga * jumlah
            total_akhir += subtotal
            print(f"\nSubtotal untuk {jumlah} {item.capitalize()} {rasa.capitalize()}: Rp {subtotal}")
            print(f"Total sementara: Rp {total_akhir}")
        else:
            print("Pilihan tidak valid, ulangi lagi.")


def tampilkan_total():
    print("\nJumlah Pembelian:")
    for item, rasa_dict in jumlah_pesanan.items():
        for rasa, jumlah in rasa_dict.items():
            if jumlah > 0:
                print(f"{item.capitalize()} {rasa.capitalize()}: {jumlah} item")
    print(f"\nTerima kasih! Total belanja Anda adalah Rp {total_akhir}.")


# Program utama
while True:
    tampilkan_menu_utama()
    try:
        pilihan = int(input("Masukkan pilihan item (1/2/3): "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka 1, 2, atau 3.")
        continue

    if pilihan == 1:
        proses_pesanan("martabak")
    elif pilihan == 2:
        proses_pesanan("pukis")
    elif pilihan == 3:
        tampilkan_total()
        break
    else:
        print("Pilihan tidak valid, ulangi lagi.")
