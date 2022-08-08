# 删除为特定值的所有列表元素
# 我们使用函数remove() 来删除列表中的特定值。这之所以可行，是因
# 为要删除的值只在列表中出现一次。如果要删除列表中所有为特定值的元素，该怎
# 么办呢？

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

cat = "cat"
while cat in pets:
    pets.remove("cat")

print(pets)

