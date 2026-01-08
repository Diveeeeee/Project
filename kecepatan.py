print("isi info2 ini, berikan - jika tidak ada")
jarak = input("masukkan jarak(meter): ")
waktu = input("masukkan waktu(second): ")
kecepatan = input("masukkan kecepatan(m/s): ")
  
if jarak == "-":
  hasil = int(kecepatan) * int(waktu)
if waktu == "-":
  hasil = int(jarak) / int(kecepatan)
if kecepatan == "-":
  hasil = int(jarak) / int(waktu)
print(hasil)
  
  
  