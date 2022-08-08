# 练习5-1：条件测试 　编写一系列条件测试，将每个测试以及对其结果的预测
# 和实际结果打印出来。你编写的代码应类似于下面这样：
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

car = 'Honda'
print("Is car == 'Honda'? I predict True.")
print(car == 'Honda')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
# 详细研究实际结果，直到你明白它为何为True 或False 。
# 创建至少10个测试，且其中结果分别为True 和False 的测试都至少有5个。
print(3 > 10)
print(10 > 3)

# 练习5-2：更多条件测试 　你并非只能创建10个测试。如果想尝试做更多比
# 较，可再编写一些测试，并将它们加入conditional_tests.py中。对于下面列
# 出的各种情况，至少编写两个结果分别为True 和False 的测试。

# 检查两个字符串相等和不等。
a = 'A'
print(a == 'A')
print(a == 'b')
# 使用方法lower() 的测试。
print(a.lower() == 'A')
# 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。
print(10 == 3)
print(10 > 3)
print(10 < 3)
print(10 >= 3)
print(10 <= 3)
# 使用关键字and 和or 的测试。
print(3 > 2 and 3 > 1)
print(3 < 2 and 3 > 1)
print(3 > 2 or 3 > 1)
print(3 < 2 or 3 > 1)

# 测试特定的值是否包含在列表中。
letters = ['a', 'b', 'c']
b = 'b'
print(b in letters)
# 测试特定的值是否未包含在列表中。
d = 'd'
print(d not in letters)