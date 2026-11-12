import random

a=[random.randint(-10000, 10000) for _ in range(100_000)]


mx = -10001
for i in a:
    if i % 15 == 0 and i > mx:
        mx = i

# поиск пары
c=0
for i in range(0, len(a)-1):
    s = a[i] + a[i+1]
    if s > mx:
        c = c + 1
print(c)