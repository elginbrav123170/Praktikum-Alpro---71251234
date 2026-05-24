n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input(f"\nMasukkan nama kategori ke-{i+1}: ")
    print(f"Masukkan 5 nama aplikasi di kategori {nama_kategori}:")
    
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input(f"Nama aplikasi ke-{j+1}: ")
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

print(f"\nData aplikasi per kategori:")
for kategori, daftar in data_aplikasi.items():
    print(f"{kategori}: {daftar}")

frekuensi_aplikasi = {}

for daftar in data_aplikasi.values():
    for app in daftar:
        if app in frekuensi_aplikasi:
            frekuensi_aplikasi[app] += 1
        else:
            frekuensi_aplikasi[app] = 1

hanya_satu_kategori = [app for app, count in frekuensi_aplikasi.items() if count == 1]
print(f"\nAplikasi yang hanya muncul di satu kategori:")
print(hanya_satu_kategori)

if n > 2:
    tepat_dua_kategori = [app for app, count in frekuensi_aplikasi.items() if count == 2]
    print(f"\nAplikasi yang muncul tepat di dua kategori:")
    print(tepat_dua_kategori)