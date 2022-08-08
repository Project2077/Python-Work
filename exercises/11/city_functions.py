# 练习11-1：城市和国家 　编写一个函数，它接受两个形参：一个城市名和一个
# 国家名。这个函数返回一个格式为 City , Country 的字符串，如
# Santiago, Chile 。将这个函数存储在一个名为city_functions.py的模块中。
def city_country(city, country, population=0):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    # 0在计算机中视为false



