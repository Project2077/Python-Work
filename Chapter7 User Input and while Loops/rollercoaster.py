# 使用int() 来获取数值输入

# 使用函数input() 时，Python将用户输入解读为字符串。请看下面让用户输入年龄
# 的解释器会话：

# >>>age = input("How old are you? ")
# How old are you? 21
# >>> age
# '21'

# 如果只想打印输入，这一点问题都没有；但如果试图将
# 输入作为数来使用，就会引发错误

# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age >= 18 

# 试图将输入用于数值比较时（见❶），Python会引发错误，因为它无法将字符串和整
# 数进行比较：不能将赋给age 的字符串'21' 与数值18 进行比较

# 为解决这个问题，可使用函数int() ，它让Python将输入视为数值。函数int()
# 将数的字符串表示转换为数值表示

# age = input("How old are you? ")
# How old are you? 21
# age = int(age)   
# age >= 18
# True

# 如何在实际程序中使用函数int() 呢？请看下面的程序，它判断一个人是否满足坐过山车的身高要求
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
	print("\nyou are tall enough to ride.")
else:
	print("\nyou will be able to ride when you're a little older.")



