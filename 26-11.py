f = open("26_demo.txt")
data = []
for line in f:
    data.append(int(line))

data = sorted(data)

res = []
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        res.append((data[i], data.count(data[i])))

for i in res:
    print(i)