# 使用函数range() 几乎能够创建任何需要的数集。例如，如何创建一个列表，其中
# 包含前10个整数（1～10）的平方呢？在Python中，用两个星号（** ）表示乘方运
# 算。下面的代码演示了如何将前10个整数的平方加入一个列表中


squares = []
for value in range(1,11):
	square=value**2
	squares.append(square)

print(squares)

# 首先，创建一个名为squares 的空列表
# 接下来，使用函数range() 让Python遍历1～10的值
# 在循环中，计算当前值的平方，并将结果赋给变量square
# 然后，将新计算得到的平方值附加到列表squares 末尾
# 循环结束后，打印列表squares 

# 为了让代码更简洁，可不使用临时变量square ，而直接将每个计算得到的值附加
# 到列表末尾
squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)





# 对数字列表执行简单的统计计算
print(min(squares))
print(max(squares))
print(sum(squares))



# 列表解析
# 前面介绍的生成列表squares 的方式包含三四行代码，而列表解析让你只需编写一
# 行代码就能生成这样的列表。列表解析 将for 循环和创建新元素的代码合并成一
# 行，并自动附加新元素。面向初学者的书并非都会介绍列表解析，这里之所以介绍
# 列表解析，是因为等你开始阅读他人编写的代码时，很可能会遇到它。
squares = [value**2 for value in range(1, 11)]
print(squares)

# for 连接了两个句子 value**2 for value & for value in range(1,11)
# 前者中for类似英文for 后者就是for循环


# 要创建自己的列表解析，需要经过一定的练习，但能够熟练地创建常规列表后，你
# 会发现这样做是完全值得的。当你觉得编写三四行代码来生成列表有点繁复时，就
# 应考虑创建列表解析了。



