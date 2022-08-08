
# if-elif-else
# 超过两个的情形，为此可使用Python提供的if-elif-else 结
# 构。Python只执行if-elif-else 结构中的一个代码块。它依次检查每个条件测
# 试，直到遇到通过了的条件测试。测试通过后，Python将执行紧跟在它后面的代
# 码，并跳过余下的测试。
# elef就是 else if 的缩写



# 在现实世界中，很多情况下需要考虑的情形超过两个。例如，来看一个根据年龄段
# 收费的游乐场：
# 	4岁以下免费；
# 	4～18岁收费25美元；
# 	18岁（含）以上收费40美元。
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25")
else:
	print("Your admission cost is $40")

# 先执行第一个if 没通过就说明age一定大于等于4了

# 为了让代码更简洁，可不在if-elif-else 代码块中打印门票价格，而只在其中设
# 置门票价格，并在它后面添加一个简单的函数调用print() ：
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}.")

# 使用多个elif 代码块
# 可根据需要使用任意数量的elif 代码块。

# 例如，假设前述游乐场要给老年人打
# 折，可再添加一个条件测试，判断顾客是否符合打折条件。下面假设对于65岁
# （含）以上的老人，可半价（即20美元）购买门票：

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"You admission cost is ${price}")

# 省略else 代码块
# Python并不要求if-elif 结构后面必须有else 代码块。在有些情况下，else 代
# 码块很有用；而在其他一些情况下，使用一条elif 语句来处理特定的情形更清晰：

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >=65:
	price = 20

print(f"You admission cost is ${price}")


# else 是一条包罗万象的语句，只要不满足任何if 或elif 中的条件测试，其中的
# 代码就会执行。这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应
# 考虑使用一个elif 代码块来代替else 代码块。这样就可以肯定，仅当满足相应的
# 条件时，代码才会执行。    
# !!!   这就是为什么优先使用elif而非else

# 测试多个条件 见toppings.py