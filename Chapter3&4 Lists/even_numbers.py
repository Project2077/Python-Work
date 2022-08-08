# 使用range() 创建数字列表

# 要创建数字列表，可使用函数list() 将range() 的结果直接转换为列表。如果将
# range() 作为list() 的参数，输出将是一个数字列表。


#在前一节的示例中，只是将一系列数打印出来。要将这组数转换为列表，可使用list() 
numbers = list(range(1, 6))
print(numbers)

# 使用函数range() 时，还可指定步长。为此，可给这个函数指定第三个参数，
# Python将根据这个步长来生成数。 如下 2-11(不包括11) 步长为2 第三个参数是步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)







