
# 复制列表
# 我们经常需要根据既有列表创建全新的列表。下面来介绍复制列表的工作原理，以
# 及复制列表可提供极大帮助的一种情形。


# 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索
# 引（[:] ）。这让Python创建一个始于第一个元素、终止于最后一个元素的切片，
# 即整个列表的副本。


# 例如，假设有一个列表包含你最喜欢的四种食品，而你想再创建一个列表，并在其
# 中包含一位朋友喜欢的所有食品。不过，你喜欢的食品，这位朋友也都喜欢，因此
# 可通过复制来创建这个列表：
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)



my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 在不使用切片的情况下复制列表的情况
# friend_foods = my_foods   这行不通

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('milk')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 结果如下 结果是都加进一个列表里了
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'milk']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'milk']

# 这种语法实际上是让Python将新变量friend_foods
# 关联到已与my_foods 相关联的列表，因此这两个变量指向同一个列表。




