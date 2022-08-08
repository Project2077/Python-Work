# 使用文件的内容

# 将文件读取到内存中后，就能以任何方式使用这些数据了。
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
# 使用一个循环将各行加入pi_string ，并删除每行末尾的换行符
# 变量pi_string 指向的字符串包含原来位于每行左边的空格，为删除这些空格，可使用strip() 而非rstrip()
# 这样就获得了一个字符串，其中包含准确到30位小数的圆周率值。这个字符串长32字符，因为它还包含整数部分的3和小数点

# 注意 　读取文本文件时，Python将其中的所有文本都解读为字符串。如果读取
# 的是数，并要将其作为数值使用，就必须使用函数int() 将其转换为整数或使
# 用函数float() 将其转换为浮点数。


# 包含一百万位的大型文件
# 前面分析的都是一个只有三行的文本文件，但这些代码示例也可处理大得多的文
# 件。如果我们有一个文本文件，其中包含精确到小数点后1 000 000位而不是30位的
# 圆周率值，也可创建一个包含所有这些数字的字符串。为此，无须对前面的程序做
# 任何修改，只要将这个文件传递给它即可。在这里，只打印到小数点后50位，以免
# 终端为显示全部1 000 000位而不断滚动

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# 对于可处理的数据量，Python没有任何限制。只要系统的内存足够多，你想处理多少数据都可以。
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")