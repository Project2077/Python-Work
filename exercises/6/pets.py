# 练习6-7：人们 　在为完成练习6-1而编写的程序中，再创建两个表示人的字
# 典，然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，
# 将其中每个人的所有信息都打印出来。

person = {
    'first_name': 'alen',
    'last_name': 'iverson',
    'age': '31',
    'city': 'new york'
}

person2 = {
    'first_name': 'jack',
    'last_name': 'jones',
    'age': '22',
    'city': 'london'
}

person3 = {
    'first_name': 'kaguya',
    'last_name': 'minami',
    'age': '22',
    'city': 'tokyo'
}
people = [person, person2, person3]
for p in people:
    for k, v in p.items():
        print(f"{k}:{v}")

# 练习6-8：宠物 　创建多个表示宠物的字典，每个字典都包含宠物的类型及其
# 主人的名字。将这些字典存储在一个名为pets 的列表中，再遍历该列表，并
# 将有关每个宠物的所有信息都打印出来。
pets = {
    'dog': 'jones',
    'cat': 'karen',
    'tigar': 'author',
    'lion': 'hayato',
    'bird': 'nancy',
}
for p_type, h_name in pets.items():
    print(f"{h_name} have a {p_type}")

# 练习6-9：喜欢的地方 　创建一个名为favorite_places 的字典。在这个字
# 典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。为了让这个
# 练习更有趣些，可以让一些朋友说出他们喜欢的几个地方。遍历这个字典，并
# 将其中每个人的名字及其喜欢的地方打印出来。
favorite_places = {
    'author': 'london',
    'alex': 'california',
    'jill': 'raccoon',
}
for friend, favorite_place in favorite_places.items():
    print(f"\n{friend.title()} likes the following places:")
    print(f"- {favorite_place.title()}")

# 练习6-10：喜欢的数2 　修改为完成练习6-2而编写的程序，让每个人都可以有
# 多个喜欢的数，然后将每个人的名字及其喜欢的数打印出来。
# 典中表
favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f" {number}")

# 练习6-11：城市 　创建一个名为cities 的字典，将三个城市名用作键。对于
# 每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及
# 一个有关该城市的事实。在表示每座城市的字典中，应包含country 、
# population 和fact 等键。将每座城市的名字以及有关信息都打印出来。
# 典中典
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        },
}

for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    mountains = info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f" It has a population of about {population}.")
    print(f" The {mountains} mounats are nearby.")


# 练习6-12：扩展 　本章的示例足够复杂，能以很多方式进行扩展。请对本章的
# 一个示例进行扩展：添加键和值、调整程序要解决的问题或改进输出的格式。
