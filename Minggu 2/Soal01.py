tinggi = float(input("Masukkan Tinggi Badan: "))
bmi =  float(input("Masukkan BMI yang diharapkan: "))
berat = bmi * (tinggi ** 2)

print(f"Berat Badan Yang diperlukan untuk mencapai BMI {bmi} dengan tinggi {tinggi} m adalah :  {berat:.2f}  kg")