"""处理FileNotFoundError 异常"""
# 处理FileNotFoundError 异常
# 使用文件时，一种常见的问题是找不到文件：查找的文件可能在其他地方，文件名
# 可能不正确，或者这个文件根本就不存在。对于所有这些情形，都可使用tryexcept 代码块以直观的方式处理。

# filename = 'alice.txt'
# with open(filename, encoding='utf-8') as f:
#     contents = f.read()

# 相比于本章前面的文件打开方式，这里有两个不同之处。一是使用变量f 来表示文件对象，这是一种常见的做法。
# 二是给参数encoding 指定了值，在系统的默认编码与要读取文件使用的编码不一致时，必须这样做

# traceback的最后一行报告了FileNotFoundError 异常，这是Python找不到要打开的文件时创建的异常。

# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist.")
# 如果文件不存在，这个程序就什么都做不了，错误处理代码也意义不大。下面来扩
# 展这个示例，看看在你使用多个文件时，异常处理可提供什么样的帮助

# 分析文本
title = "Alice in Wonderland"
print(title.split())

# 提取童话《爱丽丝漫游奇境记》（Alice in Wonderland ）的文本，并尝试
# 计算它包含多少个单词。我们将使用方法split() ，它能根据一个字符串创建一个单词列表。

# 方法split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一
# 个列表中。结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # 计算该文件大致包含多少个单词。
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
