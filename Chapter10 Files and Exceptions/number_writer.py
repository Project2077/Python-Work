# 存储数据
# 很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数
# 据。不管关注点是什么，程序都把用户提供的信息存储在列表和字典等数据结构
# 中。用户关闭程序时，几乎总是要保存他们提供的信息。一种简单的方式是使用模
# 块json 来存储数据。

# 模块json 让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时
# 加载该文件中的数据。你还可以使用json 在Python程序之间分享数据。更重要的
# 是，JSON数据格式并非Python专用的，这让你能够将以JSON格式存储的数据与使用
# 其他编程语言的人分享。这是一种轻便而有用的格式，也易于学习。

# 注意 　JSON（JavaScript Object Notation）格式最初是为JavaScript开发
# 的，但随后成了一种常见格式，被包括Python在内的众多语言采用。

# 使用json.dump() 和json.load()

# 我们来编写一个存储一组数的简短程序，再编写一个将这些数读取到内存中的程
# 序。第一个程序将使用json.dump() 来存储这组数，而第二个程序将使用json.load()

# 函数json.dump() 接受两个实参：要存储的数据，以及可用于存储数据的文件对象。
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
# 使用json需要先导入json模块
# json.dump() 前面的是存放存储数据的文件-容器 后面的是我们想存储的数据-存储物
