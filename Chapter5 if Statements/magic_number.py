# 数值比较
# 简单多了
age = 18
age == 18

answer = 17
if answer != 42:
	print("that is not correct answer,please try again!")

# 条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于
age = 19
age < 21
# True
age <= 21
# True
age > 21
# false
age >= 21
# false

# 检查多个条件
# 使用and 检查多个条件 wocao 真是and
# 要检查是否两个条件都为True ，可使用关键字and 将两个条件测试合而为
# 一。如果每个测试都通过了，整个表达式就为True ；如果至少一个测试没有
# 通过，整个表达式就为False 。
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# False
age_1 = 22
age_0 >= 21 and age_1 >= 21
# True

if age_0 >=21 and age_1 >=21:
	print("True")
else:
	print("False")

# 使用or检查多个条件 真是or
# 关键字or 也能够让你检查多个条件，但只要至少一个条件满足，就能通过整个
# 测试。仅当两个测试都没有通过时，使用or 的表达式才为False 。
age_0=22
age_1=18

if age_0>=21 or age_1>=21:
	print("True")
else:
	print("False")

age_0=18

if age_0>=21 or age_1>=21:
	print("True")
else:
	print("False")








