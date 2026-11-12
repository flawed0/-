# from math import log2, ceil
# a = 0
# N = 80
# i = ceil(log2(N))
# V = 24 * 1024 * 1024 #24 Мб -> байт
# while V % 1234567 != 0:
#     a = a + 1
#     V = 24 * 1024 * 1024 + a
# V1 = V // 1234567
# length = V1 // ceil(i / 8)
# print(length)

# from math import log2, ceil
# length = 20 #длина
# N = 5 #кол-во символов
# n = 50 #кол-во
#
# i = ceil(log2(N))
# V1 = ceil(length * i / 8)ceil(length * ic / 8)
# print(V1 * n)

from math import log2, ceil
length = 20 #длина
Nc = 10 #кол-во символов
Nb = 18
n = 50 #кол-во
ic = ceil(log2(Nc))
ib = ceil(log2(Nb))
print(25 * (ceil(2 * ic + 8 * ib)/ 8))





