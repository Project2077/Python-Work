# 修改、添加和删除元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改
# 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
motorcycles[0]='ducati'
print(motorcycles)

# 添加
# 在列表末尾添加元素 append()
motorcycles.append('ducati')
print(motorcycles)
# 在列表中插入元素  insert() 需注意insert需要两个参数 需要指定新元素的索引和值。
motorcycles.insert(0, 'honda')
print(motorcycles)

# 删除
# 使用del 语句删除元素
del motorcycles[0]
print(motorcycles)
# 使用del 可删除任意位置处的列表元素，条件是知道其索引。 
# 使用del 语句将值从列表中删除后，你就无法再访问它了


# 使用方法pop() 删除元素
# 方法pop() 删除列表末尾的元素，并让你能够接着使用它。术语弹出 （pop）源自
# 这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# 输出表明，列表末尾的值'suzuki' 已删除，它现在被赋给了变量popped_motorcycle 
# 也就是没完全消失     类似于放进了windows垃圾桶 不过需要声明一个变量接受被弹出的元素
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcle I owned was a {last_owned.title()}")

# 弹出列表中任何位置处的元素
# 实际上，可以使用pop() 来删除列表中任意位置的元素，只需在圆括号中指定要删
# 除元素的索引即可。
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


# 根据值删除元素
# 有时候，你不知道要从列表中删除的值所处的位置。如果只知道要删除的元素的
# 值，可使用方法remove() 
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# 使用remove() 从列表中删除元素时，也可接着使用它的值。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"{too_expensive} is too expensive for me")
# 注意 　方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中
# 出现多次，就需要使用循环来确保将每个值都删除。这将在第7章中介绍。
