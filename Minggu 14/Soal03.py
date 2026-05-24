def baca_kata_dari_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi = file.read().lower()
            kata_list = isi.split()
            return set(kata_list)
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return None
    except IOError:
        print(f"Error: File '{nama_file}' tidak bisa dibaca.")
        return None

file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")

kata_file1 = baca_kata_dari_file(file1)
kata_file2 = baca_kata_dari_file(file2)

if kata_file1 is not None and kata_file2 is not None:
    kata_sama = kata_file1.intersection(kata_file2)
    print("\nKata-kata yang muncul di kedua file:")
    if kata_sama:
        for kata in sorted(kata_sama):
            print(kata)
    else:
        print("(Tidak ada kata yang sama di kedua file.)")