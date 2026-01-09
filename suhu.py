def suhu():
  print("c = celcius")
  print("f = fahrenheit")
  print("r = reamur")
  print("k = kelvin")
  suhuawal = input("masukkan suhu awal: ")
  suhutujuan = input("masukkan suhu tujuan(c, f, r, k): ")
  suhu = suhuawal.split()
  nilaisuhuawal = int(suhu[0])
  namasuhuawal = suhu[1]
  if namasuhuawal == "c" and suhutujuan == "f":
    nilaisuhutujuan = nilaisuhuawal * 9 / 5 + 32
  if namasuhuawal == "c" and suhutujuan == "r":
    nilaisuhutujuan = nilaisuhuawal * 4 / 5
  if namasuhuawal == "c" and suhutujuan == "k":
    nilaisuhutujuan = nilaisuhuawal + 273
  if namasuhuawal == "f" and suhutujuan == "c":
    nilaisuhutujuan = nilaisuhuawal - 32
    nilaisuhutujuan = nilaisuhutujuan * 5 / 9
  if namasuhuawal == "f" and suhutujuan == "r":
    nilaisuhutujuan = nilaisuhuawal - 32
    nilaisuhutujuan = nilaisuhutujuan * 4 / 9
  if namasuhuawal == "f" and suhutujuan == "k":
    nilaisuhutujuan = nilaisuhuawal - 32
    nilaisuhutujuan = nilaisuhuawal * 5 / 9 + 273
  if namasuhuawal == "r" and suhutujuan == "c":
    nilaisuhutujuan = nilaisuhuawal * 5 / 4
  if namasuhuawal == "r" and suhutujuan == "f":
    nilaisuhutujuan = nilaisuhuawal * 9 / 4 + 32
  if namasuhuawal == "r" and suhutujuan == "k":
    nilaisuhutujuan = nilaisuhuawal * 5 / 4 + 273
  if namasuhuawal == "k" and suhutujuan == "c":
    nilaisuhutujuan = nilaisuhuawal - 273
  if namasuhuawal == "k" and suhutujuan == "f":
    nilaisuhutujuan = nilaisuhuawal - 273
    nilaisuhutujuan = nilaisuhutujuan * 9 / 5 + 32
  if namasuhuawal == "k" and suhutujuan == "r":
    nilaisuhutujuan = nilaisuhuawal - 273
    nilaisuhutujuan = nilaisuhutujuan * 4 / 5
  print(nilaisuhutujuan)