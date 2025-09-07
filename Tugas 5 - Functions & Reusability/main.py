import utils
import importlib

# Reload the utils module to ensure the latest version is used
importlib.reload(utils)

# Input satuan asal (C, F, atau K)
asal = input("Dari satuan (C/F/K): ").lower()
asal = utils.validasi_satuan(asal)
if not asal:
    print("ASAL TIDAK VALID")
    exit()

# Input satuan tujuan (C, F, atau K)
tujuan = input("Ke satuan (C/F/K): ").lower()
tujuan = utils.validasi_satuan(tujuan)
if not tujuan:
    print("TUJUAN TIDAK VALID")
    exit()

# Input nilai suhu
nilai = int(input("Masukkan nilai suhu: "))
nilai_valid = utils.validasi_nilai(nilai, asal)

# Validasi nilai suhu
if nilai_valid == "TIDAK VALID":
    print("NILAI TIDAK VALID")
    exit()

print()
print("=== KONVERSI SUHU ===")
print("Masukkan nilai suhu: ", nilai)
print("Dari satuan (C/F/K): ", asal.upper())
print("Ke satuan (C/F/K): ", tujuan.upper())

# Lakukan konversi suhu
hasil = utils.konversi_suhu(nilai, asal, tujuan)

# Cek kembali validitas nilai sebelum menampilkan hasil
if nilai_valid == "TIDAK VALID":
    print("NILAI ASAL TIDAK VALID")
else:
    print(f"Hasil: {nilai}°{asal.upper()} = {hasil:.2f}°{tujuan.upper()}")
