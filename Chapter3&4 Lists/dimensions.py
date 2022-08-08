# 列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这
# 对处理网站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一
# 系列不可修改的元素，元组可以满足这种需求。Python将不能修改的值称为不可变
# 的 ，而不可变的列表被称为元组 

# 定义元组
# 元组看起来很像列表，但使用圆括号而非中括号来标识。定义元组后，就可使用索
# 引来访问其元素，就像访问列表元素一样。

# 例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从
# 而确保它们是不能修改的
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

## dimensions[0] = 250
# 不能修改 报错object does not support item assignment
## print(dimensions[0])

my_t = (3,)
print(my_t)
# 注意 　严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更
# 清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号
# my_t=(3) 不是元组 自己看
# 不过一般只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。



# 遍历元组中的所有值
# 同 列表
for dimension in dimensions:
	print(dimension)


# 修改元组变量
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述
# 矩形的尺寸，可重新定义整个元组    直接改整个元组而非其中某个或某些元素
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 	print(dimension)


dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 	print(dimension)
# 这次，Python不会引发任何错误，因为给元组变量重新赋值是合法的

# 相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命
# 周期内都不变，就可以使用元组




