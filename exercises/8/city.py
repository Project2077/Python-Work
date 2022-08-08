# 练习8-5：城市 　编写一个名为describe_city() 的函数，它接受一座城市
# 的名字以及该城市所属的国家。这个函数应打印一个简单的句子，下面是一个
# 例子。 Reykjavik is in Iceland.

def describe_dity(city, country="US"):
    print(f"{city} is in {country}")


# 给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中
# 至少有一座城市不属于默认国家。
describe_dity("New York")
describe_dity(city="Hawaii", country="US" )
describe_dity("Paris", "French")

# 练习8-6：城市名 　编写一个名为city_country() 的函数，它接受城市的
# 名称及其所属的国家。这个函数应返回一个格式类似于下面的字符串：
# "Santiago, Chile"
# 至少使用三个城市国家对来调用这个函数，并打印它返回的值。


def city_country(city, country):
    message = f"{city},{country}"
    return message


print(city_country("New York", "US"))
print(city_country("Hawaii", "US"))
print(city_country("Paris", "French"))
