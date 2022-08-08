# 遍历字典
# 一个Python字典可能只包含几个键值对，也可能包含数百万个键值对。鉴于字典可
# 能包含大量数据，Python支持对字典进行遍历。字典可用于以各种方式存储信息，
# 因此有多种遍历方式：可遍历字典的所有键值对，也可仅遍历键或值。

# 遍历所有键值对
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

# 要编写遍历字典的for 循环，可声明两个变量，用于存储键值对中的键
# 和值。这两个变量可以使用任意名称。下面的代码使用了简单的变量名，这完全可行
# for k, v in user_0.items()

# for 语句的第二部分包含字典名和方法items() 
# 它返回一个键值对列表。
# 接下来，for 循环依次将每个键值对赋给指定的两个变量。

# 接favorite_languages.py

# 遍历字典中的所有键
# 在不需要使用字典中的值时，方法keys() 很有用。
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in favorite_languages.keys():
 	print(name.title())

# 遍历字典时，会默认遍历所有的键。
# for name in favorite_languages: 等同于 for name in favorite_languages.keys():
# 输出将不变
# 显式地使用方法keys() 可让代码更容易理解，你可以选择这样做，但是也可以省略它。

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
	print(f"Hi,{name.title()}")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")


# 还可使用方法keys() 确定某个人是否接受了调查。下面的代码确定Erin是否接受了调查
if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll!")


# 方法keys() 并非只能用于遍历：实际上，它返回一个列表，其中包含字典中的所有键。

# 按特定顺序遍历字典中的所有键

# 从Python 3.7起，遍历字典时将按插入的顺序返回其中的元素。不过在有些情况
# 下，你可能要按与此不同的顺序遍历字典。

# 要以特定顺序返回元素，一种办法是在for 循环中对返回的键进行排序。为此，可
# 使用函数sorted() 来获得按特定顺序排列的键列表的副本：
favorite_languages = {
 	'jen': 'python',
 	'sarah': 'c',
 	'edward': 'ruby',
 	'phil': 'python',
 	}

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()} thank you for taking the poll.")
# 这条for 语句类似于其他for 语句，不同之处是对方法dictionary.keys() 的
# 结果调用了函数sorted() 。这让Python列出字典中的所有键，并在遍历前对这个
# 列表进行排序。


# 遍历字典中的所有值
# 如果主要对字典包含的值感兴趣，可使用方法values() 来返回一个值列表，不包
# 含任何键。

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(f"{language.title()}")

# 这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不
# 是问题，但如果被调查者很多，最终的列表可能包含大量重复项。为剔除重复项，
# 可使用集合（set）。集合 中的每个元素都必须是独一无二的
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
 	print(language.title())

# set()去重