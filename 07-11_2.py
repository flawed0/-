import random

nums = []
# заполнение списка случайными числами
for i in range(100_000):
    nums.append(random.randint(-10_000, 10_000))

#номер макслимального элемента в списке, кратного 3
mx = -10001
pos = []
#поиск максимального кратного
for i in range(len(nums)):
    if nums[i] % 3 == 0 and nums[i] > mx:
        mx = nums[i]
#поиск всех позиций максимального
for i in range(len(nums)):
    if nums[i]==mx:
        pos.append(i)
print(mx, pos)
print(nums.count(mx))
print(max(pos))