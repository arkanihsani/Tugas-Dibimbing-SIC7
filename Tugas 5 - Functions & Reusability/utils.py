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

def validasi_satuan(satuan):
    if satuan in ["c", "f", "k"]:
        return satuan
    return None

def validasi_nilai(nilai, satuan):
    if satuan == "k" and nilai < 0:
        return "TIDAK VALID"
    return nilai
