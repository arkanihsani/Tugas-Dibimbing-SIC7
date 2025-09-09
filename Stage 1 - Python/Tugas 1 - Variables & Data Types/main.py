nama_kopi = "Kopi Pagi"
harga_kopi = 18000.5

nama_roti = "Roti Cokelat"
harga_roti = 10000

status = True

# Informasi Produk
print(f"Nama Produk 1  : {nama_kopi}\n")
print(f"Harga Produk 1 : {harga_kopi}\n")
print(f"Nama Produk 2  : {nama_roti}\n")
print(f"Harga Produk 2 : {harga_roti}\n")
print(f"Status Ketersediaan Roti : {status}")

print("-" * 52)

# Input Jumlah Pesanan
jumlah_kopi_str = input("Masukkan Jumlah Pesanan Kopi: ")
print()
jumlah_roti_str = input("Masukkan Jumlah Pesanan Roti: ")

jumlah_kopi_int = int(jumlah_kopi_str)
jumlah_roti_int = int(jumlah_roti_str)

print("-" * 52)

# Menampilkan Input dan Tipe Data
print(f"Jumlah Pesanan Kopi : {jumlah_kopi_int}\n")
print(f"Jumlah Pesanan Roti : {jumlah_roti_int}\n")
print(f"Tipe Data Awal Jumlah Kopi : {type(jumlah_kopi_str)}\n")
print(f"Tipe Data Awal Jumlah Roti : {type(jumlah_roti_str)}\n")

if type(jumlah_roti_int) == type(jumlah_kopi_int):
    print(f"Tipe Data Setelah Konversi : {type(jumlah_kopi_int)}")

# Perhitungan Total
total_harga_kopi = harga_kopi * jumlah_kopi_int
total_harga_roti = harga_roti * jumlah_roti_int
total_belanja = total_harga_kopi + total_harga_roti
uang_bayar = 50000
kembalian = uang_bayar - total_belanja

print("-" * 52)

print(f"Total Harga Kopi           : {total_harga_kopi}\n")
print(f"Total Harga Roti           : {total_harga_roti}\n")
print(f"Total Belanja Keseluruhan  : {total_belanja}\n")
print(f"Uang yang Dibayarkan       : {uang_bayar}\n")
print(f"Kembalian                  : {kembalian}")

print("-" * 52)

# Input Nama Pelanggan
nama_pelanggan = input("Nama Pelanggan : ")

print("-" * 52)

# Pesan Terima Kasih
pesan_terima_kasih = (
    "Terima Kasih, " + nama_pelanggan + " sudah berbelanja di Coffee Shop Bahagia!"
)
print(pesan_terima_kasih)

print("-" * 52)
print(f"Total Harga {nama_kopi} adalah Rp{total_harga_kopi}")
print("-" * 52)
