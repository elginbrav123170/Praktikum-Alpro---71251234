harga_beli1 = 650000
jumlah_gram1 = 25
harga_jual1 = 685000
harga_beli2 = 685000
harga_jual2 = 715000
jumlah_gram2 = 15

keuntungan1 = (harga_jual1 * jumlah_gram1) -( harga_beli1 * jumlah_gram1)
persentase_keuntungan1 = (keuntungan1 / (harga_beli1 * jumlah_gram1) ) * 100
total_gram = jumlah_gram1 + jumlah_gram2
keuntungankedua1 = (harga_jual2 - harga_beli1) * jumlah_gram1

keuntungankedua2 = (harga_jual2 - harga_beli2) * jumlah_gram2
total_keuntungan = keuntungankedua1 + keuntungankedua2

total_modal = (jumlah_gram1 * harga_beli1) + (jumlah_gram2 * harga_beli2)
persentase_keuntungan_total = (total_keuntungan / total_modal) * 100

print(f"Keuntungan tahap 1: Rp {keuntungan1:,} ({persentase_keuntungan1:.2f}%)")
print(f"Keuntungan tahap 2: Rp {total_keuntungan:,} ({persentase_keuntungan_total:.2f}%)")