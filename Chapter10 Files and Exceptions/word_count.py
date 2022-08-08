# 使用多个文件

# 下面多分析几本书。这此之前，先将这个程序的大部分代码移到一个名为
# count_words() 的函数中。这样，对多本书进行分析时将更容易

def count_words(filename):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'alice.txt'
count_words(filename)


# 将尝试计算《爱丽丝漫游奇境记》《悉达多》
# （Siddhartha ）、《白鲸》（Moby Dick ）和《小妇人》（Little Women ）分别包含多少个单词
# 这里可以直接使用已经打包的方法 这样避免了重复写一段相同代码
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
# 文件siddhartha.txt不存在，但这丝毫不影响该程序处理其他文件
# 故意没有将siddhartha.txt放到
# word_count.py所在的目录中，从而展示该程序在文件不存在时应对得有多出色 我放的是moby dick

# 静默失败
# 在前一个示例中，我们告诉用户有一个文件找不到。但并非每次捕获到异常都需要
# 告诉用户，有时候你希望程序在发生异常时保持静默，就像什么都没有发生一样继
# 续运行。要让程序静默失败，可像通常那样编写try 代码块，但在except 代码块
# 中明确地告诉Python什么都不要做。Python有一个pass 语句，可用于让Python在代码块中什么都不要做


def count_words_p(filename_p):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename_p, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename_p} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words_p(filename)
# 现在，出现
# FileNotFoundError 异常时，将执行except 代码块中的代码，但什么都不会发
# 生。这种错误发生时，不会出现traceback，也没有任何输出。用户将看到存在的每
# 个文件包含多少个单词，但没有任何迹象表明有一个文件未找到

# pass 语句还充当了占位符，提醒你在程序的某个地方什么都没有做，并且以后也
# 许要在这里做些什么。例如，在这个程序中，我们可能决定将找不到的文件的名称
# 写入文件missing_files.txt中。用户看不到这个文件，但我们可以读取它，进而处
# 理所有找不到文件的问题。


"""
                    决定报告哪些错误
该在什么情况下向用户报告错误？又该在什么情况下静默失败呢？如果用户知道要
分析哪些文件，他们可能希望在有文件却没有分析时出现一条消息来告知原因。如
果用户只想看到结果，并不知道要分析哪些文件，可能就无须在有些文件不存在时
告知他们。向用户显示他不想看到的信息可能会降低程序的可用性。Python的错误
处理结构让你能够细致地控制与用户分享错误信息的程度，要分享多少信息由你决
定。

编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，但只
要程序依赖于外部因素，如用户输入、存在指定的文件、有网络链接，就有可能出
现异常。凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该
向用户提供多少相关的信息。
"""