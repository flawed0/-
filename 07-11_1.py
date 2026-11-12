import random

nums = []
# заполнение списка случайными числами
for i in range(100_000):
    nums.append(random.randint(-10_000, 10_000))

# кол-во числек кратных 3
c = 0
for i in nums:
    if i % 3 == 0 and i % 10 == 0:
        c += 1
print(c)