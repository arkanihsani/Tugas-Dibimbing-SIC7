# Buat list nama siswa
list_siswa = ["Budi", "Sri", "Agus", "Dewi", "Andi", "Rina", "Yani"]

# Buat dictionary nilai siswa (key = nama siswa, value = nilai ujian)
nilai_siswa = {
    "Budi": 90,
    "Sri": 80,
    "Agus": 87,
    "Dewi": 67,
    "Andi": 98,
    "Rina": 80,
    "Yani": 100,
}

# Tambahkan satu nama siswa baru ke akhir list
list_siswa.append("Fadil")

# Hapus satu siswa tertentu dari list
list_siswa.remove("Agus")

# Cetak daftar siswa setelah perubahan
print("=== Daftar Siswa Setelah Append dan Remove ===")
print(list_siswa)
print()

# Cetak nama siswa pertama dan terakhir
print("=== Siswa Pertama dan Terakhir ===")
print(f"Pertama  : {list_siswa[0]}")
print(f"Terakhir : {list_siswa[-1]}")
print()

# Cetak 3 siswa terakhir menggunakan slicing
print("=== 3 Siswa Terakhir ===")
print(list_siswa[-3:])
print()

# Cetak daftar siswa dengan index menggunakan enumerate
print("=== Daftar Siswa dengan Index ===")
for i, siswa in enumerate(list_siswa):
    print(f"{i}: {siswa}")
print()

# Ubah nilai salah satu siswa
nilai_siswa["Sri"] = 84

# Hapus data nilai siswa lain menggunakan pop()
nilai_siswa.pop("Dewi")

# Cetak dictionary setelah update dan pop
print("=== Dictionary Nilai Siswa Setelah Update dan Pop ===")
print(nilai_siswa)
print()

# Ganti key nama siswa tertentu di dictionary nilai_siswa
nilai_siswa["Sultan"] = nilai_siswa.pop("Budi")

# Cetak dictionary setelah ganti key
print("=== Dictionary Nilai Siswa Setelah Ganti Key ===")
print(nilai_siswa)
