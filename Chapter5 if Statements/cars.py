# if 语句
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# 条件测试
# 每条if 语句的核心都是一个值为True 或False 的表达式，这种表达式称为条件
# 测试 。Python根据条件测试的值为True 还是False 来决定是否执行if 语句中的
# 代码。如果条件测试的值为True ，Python就执行紧跟在if 语句后面的代码；如果
# 为False ，Python就忽略这些代码。

# 检查是否相等
# 大多数条件测试将一个变量的当前值同特定值进行比较。最简单的条件测试检查变
# 量的值是否与特定值相等：
car = 'bmw'
car == 'bmw'
# True 这段在cmd上写会回复True

# 注:和java一样 =是赋值符 ==是相等运算符
# 这个==在两边的值相等时返回True ，否则返回False

# 检查是否相等时忽略大小写
# 在Python中检查是否相等时区分大小写。
car = 'Audi'
car == 'audi'
# 如果大小写很重要，这种行为有其优点。但如果大小写无关紧要，只想检查变量的
# 值，可将变量的值转换为小写，再进行比较
car = 'Audi'
car.lower() == 'audi'
# 无论值'Audi' 的大小写如何，上述测试都将返回True ，因为该测试不区分大小
# 写。函数lower() 不会修改最初赋给变量car 的值，因此进行这样的比较时不会
# 影响原来的变量







