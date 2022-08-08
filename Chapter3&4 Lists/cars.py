# 组织列表 即排序

# 使用方法sort() 对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# 现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序
# 还可以按与字母顺序相反的顺序排列列表元素，只需向sort() 方法传递参数
# reverse=True 即可     也是永久的
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


# 使用函数sorted() 对列表临时排序
# 函数sorted() 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars,reverse=True))

print("\nHere is the original list again:")
print(cars)
# 如果要按与字母顺序相反的顺序显示列表，也可向函数sorted() 传递参数reverse=True

# 注意 　在并非所有的值都是小写时，按字母顺序排列列表要复杂些。决定排列
# 顺序时，有多种解读大写字母的方式，要指定准确的排列顺序，可能比我们这
# 里所做的要复杂。然而，大多数排序方式是以本节介绍的知识为基础的。


# 反转
# 要反转列表元素的排列顺序，可使用方法reverse()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
# 注意，reverse() 不是按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序
# 方法reverse() 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列
# 顺序，只需对列表再次调用reverse() 即可


# 确定列表的长度 
# 使用函数len() 可快速获悉列表的长度
cars_length=len(cars)
print(cars_length)

# index out of range 索引错误
# 假设你有一个包含三个元素的列表，却要求获取第四个元素
# 这个错误新手很常见 因为索引是从0开始的 而人喜欢从1开始
# 索引错误意味着Python在指定索引处找不到元素。程序发生索引错误时，请尝试将
# 指定的索引减1，然后再次运行程序，看看结果是否正确

# 当需要访问最后一个列表元素时，都可使用索引-1 。这在任何情况下都
# 行之有效，即便你最后一次访问列表后，其长度发生了变化
# 仅当列表为空时，这种访问最后一个元素的方式才会导致错误
motorcycles = []
## print(motorcycles[-1])

# 注意 　发生索引错误却找不到解决办法时，请尝试将列表或其长度打印出来。
# 列表可能与你以为的截然不同，在程序对其进行了动态处理时尤其如此。通过
# 查看列表或其包含的元素数，可帮助你找出这种逻辑错误