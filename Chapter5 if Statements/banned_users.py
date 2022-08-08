# 检查特定值是否包含在列表中

# zi 不正确做法
request_value="quick"

values=["quick","buster","art"]

for value in values:
	if value == request_value:
		print(f"The list contains the {request_value}")
	else:
		print(f"The list don't have the {request_value}")
# 改用if


# 要判断特定的值是否已包含在列表中，可使用关键字in
requested_toppings = ['mushrooms', 'onions', 'pineapple']

'mushrooms' in requested_toppings
# True
'pepperoni' in requested_toppings
# False

if 'mushrooms' in requested_toppings:
	print("True")
else:
	print("False")
# 够简单！！

# 检查特定值是否不包含在列表中
# 还有些时候，确定特定的值未包含在列表中很重要。在这种情况下，可使用关键字not in 。
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

# 布尔表达式
# 随着你对编程的了解越来越深入，将遇到术语布尔表达式 ，它不过是条件测试的别
# 名。与条件表达式一样，布尔表达式的结果要么为True ，要么为False 。

# 布尔值通常用于记录条件，如游戏是否正在运行，或者用户是否可以编辑网站的特
# 定内容： 
game_active = True
can_edit = False
# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。





