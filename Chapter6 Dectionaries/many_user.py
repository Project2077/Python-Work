# 在字典中存储字典

# 可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。例如，如果有多个网
# 站用户，每个都有独特的用户名，可在字典中将用户名作为键，然后将每位用户的
# 信息存储在一个字典中，并将该字典作为与用户名相关联的值。在下面的程序中，
# 存储了每位用户的三项信息：名、姓和居住地。为访问这些信息，我们遍历所有的
# 用户名，并访问与每个用户名相关联的信息字典
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
    
    # 用变量把字典的值接出来
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")



# 请注意，表示每位用户的字典都具有相同的结构。虽然Python并没有这样的要求，
# 但这使得嵌套的字典处理起来更容易。倘若表示每位用户的字典都包含不同的键，
# for 循环内部的代码将更复杂。





