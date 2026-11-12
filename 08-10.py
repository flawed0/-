x = int(input())
x2 = bin(x)
if x % 2 == 0:
    x2 += "01"
else:
    x2 += '00'
res = int(x2, base = 2)
print(res)