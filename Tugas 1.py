# by Ferdinand Maulana Za Fauzi

def hitung_angsuran(harga_motor, lama_angsuran):
    # Menentukan persentase bunga berdasarkan lama angsuran
    if 0 < lama_angsuran <= 6:
        bunga = 0.05
    elif 7 <= lama_angsuran <= 12:
        bunga = 0.10
    elif 13 <= lama_angsuran <= 24:
        bunga = 0.15
    elif 24 < lama_angsuran <= 48:
        bunga = 0.20
    else:
        return "Lama angsuran tidak valid."

    # Menghitung total bunga
    total_bunga = int(harga_motor * bunga)

    # Menghitung total pembayaran
    total_pembayaran = int(harga_motor + total_bunga)

    # Menghitung angsuran per bulan
    angsuran_per_bulan = int(total_pembayaran / lama_angsuran)

    return angsuran_per_bulan

# Fungsi untuk memastikan input adalah angka
def input_angka(prompt):
    while True:
        try:
            # Mencoba mengubah input menjadi float, lalu dibulatkan ke int
            nilai = int(float(input(prompt)))
            return nilai
        except ValueError:
            # Jika input bukan angka, cetak pesan dan minta input ulang
            print("Hanya Boleh Memasukkan Angka !!!")

# Input user untuk harga motor dan lama angsuran dengan validasi
harga_motor = input_angka("Masukkan harga motor (juta) : ")
lama_angsuran = input_angka("Masukkan lama angsuran (bulan) : ")

# Menghitung dan menampilkan angsuran per bulan
angsuran = hitung_angsuran(harga_motor, lama_angsuran)
print(f"Angsuran per bulan: Rp {angsuran} juta")
