#name = input('введи имя файла: ')
# myfile = open(name+'.txt', 'ab' )
# myfile.write('')
# myfile.close()

data = []

myfile = open("file.txt")
for line in myfile:
    data.append(line.strip())

for i in range(len(data)):
    if data[i] == "Алексей":
        data[i] = "Александр"
print(data)