# utils.py

# Fungsi untuk konversi suhu antar satuan (Celsius, Fahrenheit, Kelvin)
def konversi_suhu(nilai, dari, ke):
    if dari == "c" and ke == "f":
        return (nilai * 9 / 5) + 32
    elif dari == "c" and ke == "k":
        return nilai + 273.15
    elif dari == "f" and ke == "c":
        return (nilai - 32) * 5 / 9
    elif dari == "f" and ke == "k":
        return (nilai - 32) * (5 / 9) + 273.15
    elif dari == "k" and ke == "c":
        return nilai - 273.15
    elif dari == "k" and ke == "f":
        return (nilai - 273.15) * (9 / 5) + 32
    else:
        return "TIDAK VALID"


# Fungsi untuk validasi input satuan suhu
def validasi_satuan(satuan):
    if satuan in ["c", "f", "k"]:
        return satuan
    return None


# Fungsi untuk validasi nilai suhu sesuai satuannya
def validasi_nilai(nilai, satuan):
    # Kelvin tidak boleh bernilai negatif
    if satuan == "k" and nilai < 0:
        return "TIDAK VALID"
    return nilai
