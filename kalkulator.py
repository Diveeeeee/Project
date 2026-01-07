def kalkulator():
  operasi = input("masukkan operasi: ")
  b = operasi.split()
  c = int(b[0])
  d = int(b[2])
  if b[1] == "+":
    hasil = c + d 
  if b[1] == "-":
    hasil = c - d 
  if b[1] == "×":
    hasil = c * d 
  if b[1] == "÷":
    hasil = c / d 
  print(hasil)
  
