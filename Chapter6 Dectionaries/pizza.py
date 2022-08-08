# 在字典中存储列表
# 有时候，需要将列表存储在字典中，而不是将字典存储在列表中。

# 存储所点比萨的信息。
pizza = {
	'crust':'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
	# 概述所点的比萨。
print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
 	print(topping)
 	
# 注意 　列表和字典的嵌套层级不应太多。如果嵌套层级比前面的示例多得多，
# 很可能有更简单的解决方案。
