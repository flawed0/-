# for n in range(1, 300):
#     n2 = bin(n)[2:]
#     ost = n2.count('1')%2
#     n2 = n2 + str(ost)
#     ost = n2.count('1') % 2
#     r2 = n2 + str(ost)
#     r = int(r2,2)
#     if r > 43:
#         print(r)
#         break
#
# for n in range(2,10000):
#     n2 = bin(n)[2:-1]
#     if n%2 == 1:
#         r2 = n2 + "10"
#     else:
#         r2 = n2 +"01"
#     if int(r2, 2) == 2018:
#         print(n)
#         break

for n in range(1, 100):
    n2 = bin(n)[2 : 0]
    if n2.count('1') > n2.count('0'):
        n2 += '1'
    else:
        n2 += '0'
    r = int(n2, base=2)
    if r>80:
        print(r)
        break

d gjkmpjdfntkt








