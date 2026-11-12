import random

nums = []
# заполнение списка случайными числами
for i in range(100_000):
    nums.append(random.randint(-10_000, 10_000))

#сортировка списка

#1 сортировка по возрастанию
nums_sorted = sorted(nums, reverse=True)
print(nums_sorted)



