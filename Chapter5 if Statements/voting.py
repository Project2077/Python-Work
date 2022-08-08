# if 语句

# 简单的if 语句
# 最简单的if 语句只有一个测试和一个操作
# if conditional_test:
#   	do something

# 假设有一个表示某人年龄的变量，而你想知道这个人是否符合投票的年龄，可使用如下代码
age = 19
if age >= 18:
	print("You are old enough to vote!")

# if-else
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
# 上述代码之所以可行，是因为只存在两种情形：要么符合投票年龄，要么不符合。
# if-else 结构非常适合用于让Python执行两种操作之一的情形。


















