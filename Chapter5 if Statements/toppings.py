# 检查是否不相等
# 要判断两个值是否不等，可结合使用惊叹号和等号（!= ），其中的惊叹号表示不，其他很多编程语言中也是如此。
# != 不等运算符
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")


# 测试多个条件

# if-elif-else 结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过
# 了的测试后，Python就跳过余下的测试。这种行为很好，效率很高，让你能够测试
# 一个特定的条件。

# 然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含
# elif 和else 代码块的简单if 语句。在可能有多个条件为True 且需要在每个条
# 件为True 时都采取相应措施时，适合使用这种方法。

# 下面再来看看前面的比萨店示例。如果顾客点了两种配料，就需要确保在其比萨中
# 包含这些配料：
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
 	print("Adding extra cheese.")
print("\nFinished making your pizza!")

# 多个if从句并列
# 不管前一个if从句结果如何 都会执行下个if从句的判断
# 不管前两个测试的结果如何，都会执行这些代码。每当这个程序运行时，都会执行这三个独立的测试。
# 而if else(包括elif) 有一个满足条件，其它的就pass了







# if elif else 错误实例  这个缩进也可以 但最好统一缩进 避免不必要的错误
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")
print("\nFinished making your pizza!")
# 只有第一句Adding mushrooms 而第二句Adding extra cheese被跳了


# 使用if 语句处理列表
# 通过结合使用if 语句和列表，可完成一些有趣的任务：对列表中特定的值做特殊处
# 理；高效地管理不断变化的情形，如餐馆是否还有特定的食材；证明代码在各种情
# 形下都将按预期那样运行。

# 其实就是for+if

# 检查特殊元素

# 继续使用前面的比萨店示例。这家比萨店在制作比萨时，每添加一种配料都打印一
# 条消息。通过创建一个列表，在其中包含顾客点的配料，并使用一个循环来指出添
# 加到比萨中的配料，能以极高的效率编写这样的代码
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print((f"Adding {requested_topping}."))

print("\nFinished making your pizza!")

# 然而，如果比萨店的青椒用完了，该如何处理呢？为妥善地处理这种情况，可在for
# 循环中包含一条if 语句：

for requested_topping in requested_toppings:
	if  requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print((f"Adding {requested_topping}."))


print("\nFinished making your pizza!")


# 确定列表不是空的
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

# 在if 语句中将列表名用作条件表达式时，Python将在列表至
# 少包含一个元素时返回True ，并在列表为空时返回False 。如果
# requested_toppings 不为空，就运行与前一个示例相同的for 循环；否则，就
# 打印一条消息，询问顾客是否确实要点不加任何配料的原味比萨

# 使用多个列表

# 顾客的要求往往五花八门，在比萨配料方面尤其如此。如果顾客要在比萨中添加炸
# 薯条，该怎么办呢？可使用列表和if 语句来确定能否满足顾客的要求。

# 来看看在制作比萨前如何拒绝怪异的配料要求。
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry,We don't have {requested_topping}.")

print("\nFinished making your pizza!")




