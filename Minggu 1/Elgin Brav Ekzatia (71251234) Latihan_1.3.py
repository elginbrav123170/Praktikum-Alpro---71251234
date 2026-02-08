import math
modal_awal = 200000000 
bunga_per_tahun = 0.10 
target_uang = 400000000  
waktu_tahun = (math.log(target_uang / modal_awal) / math.log(1 + bunga_per_tahun))
print(f"Saldo mencapai Rp{target_uang:,} dalam {math.ceil(waktu_tahun)} tahun.")