# SEBUAH WARUNG MENJUAL BEBERAPA PRODUK YANG MEMILIKI HARGA YANG BERBEDA SETIAP PRODUK
# BUATLAH SEBUAH PROGRAM UNTUK MENJUAL PRODUK WARUNG 

# input barang yang akan dibeli
# jumlah barang yang akan dibeli

print()
print("==========WARUNG PUNK==========")
print()
print()
print('MIE INSTANS..........3500')
print('ROTI AOKA............2000')
print('KOPI ABC.............1500')
print('AQUA.................2500')
print('TEH..................1000')
print('TELOR................1000')
print('SAUS.................500')
print()
print('=================================')
print("SILAKAN MASUKAN NAMA PRODUK DAN JUMLAH PRODUK YANG AKAN DI BELI")
print()

barang = str(input('Nama Barang :'))
harga = int(input('harga barang :'))

jumlah = int(input('Jumlah Barang :'))

mie_instans = 3500
Roti_aoka = 2000
kopi_abc = 1500
aqua = 2500
teh = 1000
telor = 1000
saus = 500



beli = ["AYAM"]
if (barang not in beli):
    harga1 = (harga*jumlah)

barang = str(input('Nama Barang :'))
harga = int(input('harga barang :'))
jumlah = int(input('Jumlah Barang :'))

beli = ["AYAM"]
if (barang not in beli):
    harga2 = (harga*jumlah)

barang = str(input('Nama Barang :'))
harga = int(input('harga barang :'))
jumlah = int(input('Jumlah Barang :'))

beli = ["AYAM"]
if (barang not in beli):
    harga3 = (harga*jumlah)

barang = str(input('Nama Barang :'))
harga = int(input('harga barang :'))
jumlah = int(input('Jumlah Barang :'))

beli = ["AYAM"]
if (barang not in beli):
    harga4 = (harga*jumlah)

barang = str(input('Nama Barang :'))
harga = int(input('harga barang :'))
jumlah = int(input('Jumlah Barang :'))
beli = ["AYAM"]
if (barang not in beli):
    harga5 = (harga*jumlah)

print(harga1)
print(harga2)
print(harga3)
print(harga4)
print(harga5)
total = (harga1 + harga2 + harga3 + harga4 + harga5)
print('TOTAL HARGA : ',total)
# roti = ["ROTI AOKA"]
# if (barang in roti):
#     harga = (Roti_aoka*jumlah)
#     print (f'TOTAL HARGA :',harga)

# kopi = ["KOPI ABC"]
# if (barang in kopi):
#     harga = (kopi_abc*jumlah)
#     print (f'TOTAL HARGA :',harga)

# aqua = ["MIE INSTANS"]
# if (barang in mie):
#     harga = (mie_instans*jumlah)
#     print (f'TOTAL HARGA :',harga)