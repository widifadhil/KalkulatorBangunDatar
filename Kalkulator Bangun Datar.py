# -*- coding: utf-8 -*-
"""TUBES MM Widi_Fadhil

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1awvOoccg8Poh7GKWchUFygoKaKgcVYWe
"""

pi = 3.14
def menu(): #menampilkan menu awal
  print()
  print("Aplikasi Hitung Rumus Geometri")
  print("Pilih Jenis")
  print("0. Exit")
  print("1. Bangun Datar")
  print("2. Bangung Ruang")

def bangundatar(): #menampilkan menu bangun datar
  print()
  print("Pilih Bangun Datar")
  print("0. Back")
  print("1. Persegi")
  print("2. Persegi Panjang")
  print("3. Lingkaran")
  print("4. Segitiga")
  print("5. Trapesium")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1: 
    persegi()
  elif pilih == 2: 
    persegipanjang()
  elif pilih == 3:
    lingkaran()
  elif pilih == 4:
    segitiga()
  elif pilih == 5:
    trapesium()
  elif pilih == 0:
    quit()
  else:
    print("Pilihan tersebut tidak ada")
    bangundatar()

def persegi(): #menampilkan menu persegi jika pada menu bangun datar memilih 1
  print()
  print("Pilih Rumus Bangun Datar")
  print("0. Back")
  print("1. Luas")
  print("2. Keliling")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    luaspersegi()
  elif pilih == 2:
    kelpersegi()
  elif pilih == 0:
    bangundatar()
  else:
    print("Pilihan tersebut tidak ada")
    persegi()

def luaspersegi(): #menampilkan menu luas persegi yang akan menghitung luas bangun persegi
  print()
  print("Rumus Luas dari Bangun Persegi")
  print("Rumusnya: sisi X sisi")
  sisi = int (input("Masukkan Sisi : "))
  i=0
  while i < 1:
    sisi*=sisi
    i+=1
  luas = sisi
  print("Luas Persegi = ", luas)

def kelpersegi(): #menampilkan menu keliling persegi yang akan menghitung keliling bangun persegi
  print()
  print("Rumus Keliling dari Bangun Persegi")
  print("Rumusnya: 4 X sisi")
  sisi = int(input("Masukkan Sisi : "))
  keliling = 4*sisi
  print("Keliling Persegi = ", keliling)

def persegipanjang(): #menampilkan menu persegi panjang jika pada menu bangun datar memilih 2
  print()
  print("Pilih Rumus Bangun Datar")
  print("0. Back")
  print("1. Luas")
  print("2. Keliling")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    luaspersegipanjang()
  elif pilih == 2:
    kelpersegipanjang() 
  elif pilih == 0:
    bangundatar()
  else:
    print("Pilihan tersebut tidak ada")
    persegiipanjang()

def luaspersegipanjang(): #menu menghitung luas persegi panjang
  print()
  print("Rumus Luas dari Persegi Panjang")
  print("Rumusnya: Panjang(P) X Lebar(L)")
  panjang = int(input("Panjang : "))
  lebar = int(input("Lebar : "))
  luas = panjang*lebar
  print("Luas : ", luas)

def kelpersegipanjang(): #menu menghitung keliling persegi panjang
  print()
  print("Rumus Keliling dari Persegi Panjang")
  print("Rumusnya: (2 X Panjang(P)) + (2 X Lebar(L))")
  panjang = int(input("Panjang : "))
  lebar = int(input("Lebar : "))
  keliling = (2*panjang) + (2*lebar)
  print("Keliling : ", keliling)

def lingkaran(): #menampilkan menu lingkaran 
  print()
  print("Pilih Rumus Bangun Datar")
  print("0. Back")
  print("1. Luas")
  print("2. Keliling")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    luaslingkaran()
  elif pilih == 2:
    kellingkaran() 
  elif pilih == 0:
    bangundatar()
  else:
    print("Pilihan tersebut tidak ada")
    lingkaran()

def luaslingkaran(): #menu menghitung luas lingkaran
  print()
  print("Rumus Luas dari Lingkaran")
  print("Rumusnya: pi X r X r") #r adalah jari-jari
  r = int (input("Jari-jari : ")) 
  i=0
  while i < 1:
    r*=r
    i+=1
  print("Luas = ", pi*r)

def kellingkaran(): #menu menghitung keliling lingkaran
  print()
  print("Rumus Luas dari Lingkaran")
  print("Rumusnya: pi X d") #d adalah diameter
  d = int(input("Diameter : "))
  print("Keliling = ", pi*d)

def segitiga(): #menampilkan menu segitiga
  print()
  print("Pilih Rumus Bangun Datar")
  print("0. Back")
  print("1. Luas")
  print("2. Keliling")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    luassegitiga()
  elif pilih == 2:
    kelsegitiga() 
  elif pilih == 0:
    bangundatar()
  else:
    print("Pilihan tersebut tidak ada")
    segitiga()

def luassegitiga(): #menu menghitung luas segitiga
  print()
  print("Rumus Luas dari Segitiga")
  print("Rumusnya: (alas X tinggi)2") 
  alas = int(input("Alas : "))
  tinggi = int(input("Tinggi : "))
  luas = (alas*tinggi)/2
  print("Luas Segitiga Adalah : ", luas)

def kelsegitiga(): #menu menghitung keliling segitiga
  print()
  print("Rumus Keliling dari Segitiga")
  print("Rumusnya: sisi 1 + sisi 2 + sisi 3")
  sisi1 = int(input("Sisi 1 : "))
  sisi2 = int(input("Sisi 2 : "))
  sisi3 = int(input("Sisi 3 : "))
  keliling = sisi1+sisi2+sisi3
  print("Keliling Segitiga Adalah : ", keliling)

def trapesium(): #menampilkan menu trapesium
  print()
  print("Pilih Rumus Bangun Datar")
  print("0. Back")
  print("1. Luas")
  print("2. Keliling")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    luastrapesium()
  elif pilih == 2:
    keltrapesium()
  elif pilih == 0:
    bangundatar()
  else:
    print("Pilihan tersebut tidak ada")
    trapesium()

def luastrapesium(): #menu menghitung luas trapesium
  print()
  print("Rumus Luas dari Trapesium")
  print("Rumusnya: ((atas+bawah)tinggi)/2")
  atas = int(input("Atas : "))
  bawah = int(input("Bawah : "))
  tinggi = int(input("Tinggi : "))
  luas = (atas+bawah) * tinggi / 2
  print("Luas = ", luas)

def keltrapesium(): #menu menghitung keliling trapesium
  print()
  print("Rumus Luas dari Trapesium")
  print("Rumusnya: AB + BC + CD + DA")
  ab = int(input("Sisi AB : "))
  bc = int(input("Sisi BC : "))
  cd = int(input("Sisi CD : "))
  da = int(input("Sisi DA : "))
  keliling = ab+bc+cd+da
  print("Keliling =", keliling)

def bangunruang(): #menampilkan menu bangun ruang
  print()
  print("Pilih Bangun Ruang")
  print("0. Back")
  print("1. Kubus")
  print("2. Balok")
  print("3. Bola")
  print("4. Kerucut")
  print("5. Tabung")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    kubus()
  elif pilih == 2:
    balok()
  elif pilih == 3:
    bola()
  elif pilih == 4:
    kerucut()
  elif pilih == 5:
    tabung()
  elif pilih == 0:
    quit()
  else:
    print()
    print("Pilihan tersebut tidak ada")
    bangunruang()

def kubus(): #menampilkan menu kubus
  print()
  print("Pilih Rumus Bangun Ruang")
  print("0. Back")
  print("1. Volume")
  print("2. Luas Permukaan")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    volumekubus()
  elif pilih == 2:
    luaspermukaankubus()
  elif pilih == 0:
    bangunruang()
  else:
    print("Pilihan tersebut tidak ada")
    kubus()

def volumekubus(): #menu menghitung
  print()
  print("Rumus Volume dari Kubus")
  print("Rumusnya: sisi x sisi x sisi")
  sisi = int (input("sisi: "))
  i=0
  s=1
  while i < 3:
    s=s*sisi
    i=i+1
  volume =s
  print("Volume = ", volume)

def luaspermukaankubus(): #menu menghitung luas permukaan kubus
  print()
  print("Rumus Luas Permukaan dari Kubus")
  print("Rumusnya: 6 X sisi^2")
  sisi = int(input("sisi: "))
  i=0
  while i < 1:
    sisi*=sisi
    i+=1
  luasp = 6*(sisi)
  print("Luas Permukaan = ", luasp)

def balok(): #menampilkan menu balok
  print()
  print("Pilih Rumus Bangun Ruang")
  print("0. Back")
  print("1. Volume")
  print("2. Luas Permukaan")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    volumebalok()
  elif pilih == 2:
    luaspermukaanbalok()
  elif pilih == 0:
    bangunruang()
  else:
    print("Pilihan tersebut tidak ada")
    balok()

def volumebalok(): #menu menghitung volume balok
  print()
  print("Rumus Volume dari Balok")
  print("Rumusnya: Panjang X Lebar X Tinggi")
  p = int (input("Panjang: "))
  l = int (input("Lebar:  "))
  t = int (input("Tinggi: "))
  volume = p*l*t
  print("Volume = ", volume)

def luaspermukaanbalok(): #menu menghitung luas permukaan
  print()
  print("Rumus Luas Permukaan dari Balok")
  print(" Rumusnya: 2 X (P.L + P.T + L.T)")
  p = int (input("Panjang: "))
  l = int (input("Lebar:  "))
  t = int (input("Tinggi: "))
  lpbalok = 2*((p*l)+(p*t)+(l*t))
  print("Luas Permukaan = ", lpbalok)

def bola(): #menampilkan menu bola
  print()
  print("Pilih Rumus Bangun Ruang")
  print("0. Back")
  print("1. Volume")
  print("2. Luas Permukaan")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    volumebola()
  elif pilih == 2:
    luaspermukaanbola()
  elif pilih == 0:
    bangunruang()
  else:
    print("Pilihan tersebut tidak ada")
    bola()

def volumebola(): #menu menghitung volume bola
  print()
  print("Rumus Volume dari Bola")
  print("Rumusnya: 4/3 x pi x r^3")
  r = int (input("Jari-jari: "))
  i=0
  jari=1
  while i < r:
    jari=jari*r
    i=i+1
  volume = (4*pi*jari)/3
  print("Volume Bola = ", round(volume,2))

def luaspermukaanbola(): #menu menghitung luas permukaan bola
  print()
  print("Rumus Luas Permukaan dari Bola")
  print("Rumusnya: 4 X pi X r^2")
  r = int (input("Jari-jari: "))
  i=0
  while i < 1:
    r*=r
    i+=1
  lpbola = 4*pi*r
  print("Volume Bola = ", round(lpbola,2))

def kerucut(): #menampilkan menu kerucut
  print()
  print("Pilih Rumus Bangun Ruang")
  print("0. Back")
  print("1. Volume")
  print("2. Luas Permukaan")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    volumekerucut()
  elif pilih == 2:
    luaspermukaankerucut()
  elif pilih == 0:
    bangunruang()
  else:
    print("Pilihan tersebut tidak ada")
    kerucut()

def volumekerucut(): #menghitung volume kerucut
  print()
  print("Rumus Volume dari Kerucut")
  print("Rumus: 1/3 X 3,14 X r^2 X t")  
  r = int (input("Jari-jari: "))
  t = int (input("Tinggi: "))
  i=0
  while i < 1:
    r*=r
    i+=1
  volume = (1/3)*pi*r*t
  print("Volume Kerucut = ", round(volume,2))

def luaspermukaankerucut(): #menghitung luas permukaan kerucut
  print()
  print("Rumus Luas Permukaan dari Kerucut")
  print("Rumus: 3.14 x r x (r+s) ")
  r = int (input("Jari-jari: "))
  s = int (input("Garis Apotema: "))
  lpkerucut = pi*r*(r+s)
  print("Luas Permukaan Kerucut = ", round(lpkerucut,2))

def tabung(): #menampilkan menu tabung
  print()
  print("Pilih Rumus Bangun Ruang")
  print("0. Back")
  print("1. Volume")
  print("2. Luas Permukaan")
  pilih = int (input("Masukkan Pilihan: "))
  if pilih == 1:
    volumetabung()
  elif pilih == 2:
    luaspermukaantabung()
  elif pilih == 0:
    bangunruang()
  else:
    print("Pilihan tersebut tidak ada")
    tabung()

def volumetabung(): #menghitung volume tabung
  print()
  print("Rumus Volume dari Tabung")
  print("Rumus: phi x r^2 x t")
  r = int (input("Jari-jari: "))
  t = int (input("Tinggi: "))
  i=0
  i=0
  while i < 1:
    r*=r
    i+=1
  volume = pi*r*t
  print("Volume Tabung = ", round(volume,2))

def luaspermukaantabung(): #menghitung luas permukaan tabung
  print()
  print("Rumus Luas Permukaan dari Tabung")
  print("Rumus: 2 x pi x r x (r + t)")
  r = int (input("Jari-jari: "))
  t = int (input("Tinggi: "))
  lptabung = 2*pi*r*(r+t)
  print("Luas Permukaan ", round(lptabung,2))

loop = 1
while loop != 0:
  menu()
  opsi = int (input("Masukkan Pilihan: "))
  if opsi == 1:
    bangundatar()
  elif opsi== 2:
    bangunruang()
  elif opsi == 0:
    loop = 0
  else:
    print("Invalid Input")

print("Terima Kasih Telah Menggunakan Aplikasi ini:)")