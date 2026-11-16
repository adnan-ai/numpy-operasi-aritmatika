import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10] # kalau dijumlahkan akan bertambah jumlah listnya

# array numpy
amp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10]) # kalau ditambah akan bertambah nilainya

# ELEMENWISE operation

# penjumlahan
hasil = amp + bnp
# pengurangan
hasil1 = amp - bnp
# perkalian
# pembagian
# kuadrat

# multidimensi array numpy

jumlah_member = np.array(([10,5], # hari 1 jumlah yang ambil paket regular dan pt
                        [8,7])) # hari ke 2
harga_paket = np.array(([300000], # harga paket member
                        [1500000])) # harga paket pt

# perkalian matrix multipication. mengikuti aturan aljabar

pendapatan = np.matmul(jumlah_member, harga_paket)

print(pendapatan)