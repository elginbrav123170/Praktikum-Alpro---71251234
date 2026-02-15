gaji_per_jam = int(input("Masukkan Gaji Perjam yang diinginkan: " ))
banyak_jam_kerja_per_minggu = int(input("Masukkan Banyak Jam Kerja PerMinggu: "))
banyak_minggu_kerja =  5

pendapatan_sebelum_pajak = gaji_per_jam * banyak_jam_kerja_per_minggu * banyak_minggu_kerja
pendapatan_setelah_pajak = pendapatan_sebelum_pajak * 86 / 100
pakaian_aksesoris = pendapatan_setelah_pajak * 10 / 100
alat_tulis = pendapatan_setelah_pajak * 1 / 100
uang_setelah_aksesoris_alat_tulis = pendapatan_setelah_pajak - pakaian_aksesoris - alat_tulis
uang_yang_disedekahkan = uang_setelah_aksesoris_alat_tulis * 25 /100
sedekah_anak_yatim = uang_yang_disedekahkan * 30/100
sedekah_kaum_dhuafa = uang_yang_disedekahkan - sedekah_anak_yatim

print(f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak adalah {pendapatan_sebelum_pajak}")
print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak adalah {pendapatan_setelah_pajak}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris adalah {pakaian_aksesoris}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis adalah {alat_tulis}")
print(f"Jumlah uang yang akan Budi sedekahkan adalah {uang_yang_disedekahkan}")
print(f"Jumlah uang yang akan diterima anak yatim {sedekah_anak_yatim}")
print(f"Jumlah uang yang akan diterima kaum dhuafa {sedekah_kaum_dhuafa}")
