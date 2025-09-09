# Fungsi untuk menentukan kategori BMI
def kategori(bmi):
    if bmi < 18.5:
        if bmi < 16:
            print("Category: Severe Thinness")
        elif bmi >= 16 and bmi < 17:
            print("Category: Moderate Thinness")
        else:
            print("Category: Mild Thinness")
    elif bmi >= 18.5 and bmi <= 25:
        print("Category: Normal")
    elif bmi > 25 and bmi <= 30:
        print("Category: Overweight")
    elif bmi > 30:
        if bmi <= 35:
            print("Category: Obese Class I")
        elif bmi > 35 and bmi <= 40:
            print("Category: Obese Class II")
        else:
            print("Category: Obese Class III")


# Program utama
print("Kalkulator BMI")

# Input berat badan (kg) dan tinggi badan (cm)
bb = float(input("Masukkan berat badan anda (kg)  : "))
tb = float(input("Masukkan tinggi badan anda (cm) : "))

# Rumus BMI: berat badan / (tinggi badan dalam meter)^2
bmi = bb / ((tb / 100) ** 2)

# Output hasil BMI
print(f"\nBMI Anda adalah: {bmi:.2f}")
kategori(bmi)
