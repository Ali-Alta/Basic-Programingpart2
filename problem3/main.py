# input
T = 20.0
r = 4.0
L = 2

# kode disini
# menghiting Tabung 
T = float(input("Tinggi(cm): "))
r = float(input("jari-jari (cm):"))
L = float (input("Luas Permukaan (cm):"))

# Menghitung luas permukaan tabung
pi = 3.14  # atau bisa menggunakan pi = 22/7
luas_permukaan = 2 * pi * r * (r + T)

# Menampilkan hasil
print(f"Luas permukaan tabung dengan tinggi {T} cm dan jari-jari {r} cm adalah {luas_permukaan:.2f} cm².")