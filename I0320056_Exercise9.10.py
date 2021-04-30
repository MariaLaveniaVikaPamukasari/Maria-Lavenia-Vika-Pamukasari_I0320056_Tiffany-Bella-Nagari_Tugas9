import array
# nilai awal (sebelum dibalik)
A = array.array('i', [100, 200, 300, 400, 500])
print(A)

A[1] = -700     # mengubah elemen kedua
A[4] = 800     # mengubah elemen kelima
print(A)

# membalik urutan elemen array
A.reverse()

# nilai akhor (setelah dibalik)
print(A)