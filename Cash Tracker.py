def moneynote ():
  saldo = 0
  tanggal_pemasukan = []
  jumlah_pemasukan = []
  tanggal_pengeluaran = []
  jumlah_pengeluaran = []
  barang_pengeluaran = []
  def pemasukan(tanggal, jumlah):
      tanggal_pemasukan.append(tanggal)
      jumlah_pemasukan.append(jumlah)
  def pengeluaran(tanggal, jumlah, barang):
      tanggal_pengeluaran.append(tanggal)
      jumlah_pengeluaran.append(jumlah)
      barang_pengeluaran.append(barang)
    
  while True:
    print("1.Catat pemasukan")
    print("2.Catat pengeluaran")
    print("3.Lihat info anda")
    pilihan = input("Masukkan pilihan anda: ")
      
    if pilihan == "1":
      while True:
        tanggal = input("masukkan tanggal pemasukan: ")
        jumlah = int(input("masukkan jumlah pemasukan: "))
        pemasukan(tanggal, jumlah)
        print("1. lagi")
        print("2. kembali")
        pilihan = input("masukkan pilihan anda: ")
        if pilihan == "2":
          break
  
    elif pilihan == "2":
      while True:
        tanggal = input("masukkan tanggal pengeluaran: ")
        jumlah = int(input("masukkan jumlah pengeluaran: "))
        barang = input("masukkan nama barang: ")
        pengeluaran(tanggal, jumlah, barang)
        print("1. lagi")
        print("2. kembali")
        pilihan = input("masukkan pilihan anda: ")
        if pilihan == "2":
          break
  
    elif pilihan == "3":
      print("info anda:")
      print("•pemasukan")
      for i in range(len(tanggal_pemasukan)):
        print(f"{tanggal_pemasukan[i]} {jumlah_pemasukan[i]}")
      total_pemasukan = sum(jumlah_pemasukan)
      print(f"total pemasukan = {total_pemasukan}")
      
      print("•pengeluaran")
      for i in range(len(tanggal_pengeluaran)):
        print(f"{tanggal_pengeluaran[i]} {jumlah_pengeluaran[i]} {barang_pengeluaran[i]}")
      total_pengeluaran = sum(jumlah_pengeluaran)
      print(f"total pengeluaran = {total_pengeluaran}")
      
      print("•saldo anda sekarang")
      saldo = total_pemasukan - total_pengeluaran
      print(saldo)
      
      break
moneynote()