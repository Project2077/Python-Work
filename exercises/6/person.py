# 练习6-1：人 　使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居
# 住的城市。该字典应包含键first_name 、last_name 、age 和city 。将
# 存储在该字典中的每项信息都打印出来。

person = {
    'first_name': 'alen',
    'last_name': 'iverson',
    'age': '31',
    'city': 'new york'
    }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 练习6-2：喜欢的数 　使用一个字典来存储一些人喜欢的数。请想出5个人的名
# 字，并将这些名字用作字典中的键；找出每个人喜欢的一个数，并将这些数作
# 为值存储在字典中。打印每个人的名字和喜欢的数。为了让这个程序更有趣，
# 通过询问朋友确保数据是真实的。
numbers = {
    'macgrady': '1',
    'james': '23',
    'jordan': '23',
    'oneal': '32',
    'miko': '56',
    }

for name, number in numbers.items():

    print(f"{name}'s favorite number is {number}")

# 练习6-3：词汇表 　Python字典可用于模拟现实生活中的字典。为避免混淆，
# 我们将后者称为词汇表。
# 想出你在前面学过的5个编程术语，将其用作词汇表中的键，并将它们的含
# 义作为值存储在词汇表中。
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}
# 以整洁的方式打印每个术语及其含义。为此，可先打印术语，在它后面加
# 上一个冒号，再打印其含义；也可在一行打印术语，再使用换行符（\n ）
# 插入一个空行，然后在下一行以缩进的方式打印其含义。


# 练习6-4：词汇表2 　现在你知道了如何遍历字典，可以整理为完成练习6-3而
# 编写的代码，将其中的一系列函数调用print() 替换为一个遍历字典中键和值
# 的循环。确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次
# 运行这个程序时，这些新术语及其含义将自动包含在输出中。
for name, value in glossary.items():
    print(f"{name}:{value}")

glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for name, value in glossary.items():
    print(f"\n{name}:{value}")

# 练习6-5：河流 　创建一个字典，在其中存储三条重要河流及其流经的国家。
# 例如，一个键值对可能是'nile': 'egypt' 。
rivers = {
    'nile': 'egypt',
    'yellow river': 'china',
    'fraser': 'canada',
    }
# 使用循环为每条河流打印一条消息，下面是一个例子。
# The Nile runs through Egypt.
for river, country in rivers.items():
    print(f"The {river} runs through {country}")

# 使用循环将该字典中每条河流的名字打印出来。
for river in rivers.keys():
    print(river)

# 使用循环将该字典包含的每个国家的名字打印出来。
for country in rivers.values():
    print(country)


# 练习6-6：调查 　在6.3.1节编写的程序favorite_languages.py中执行以下操作。
favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
     }
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其
# 他人未包含在字典中。
coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
# 遍历这个人员名单。对于已参与调查的人，打印一条消息表示感谢；对于
# 还未参与调查的人，打印一条消息邀请他参加。
for coder, language in favorite_languages.items():
    if coder in coders:
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")

