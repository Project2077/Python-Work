# 练习9-1：餐馆 　创建一个名为Restaurant 的类，为其方法__init__()
# 设置属性restaurant_name 和cuisine_type 。创建一个名为
# describe_restaurant() 的方法和一个名为open_restaurant() 的方
# 法，前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。

# 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用
# 前述两个方法。
class Restaurant:
    def __init__(self, name, cuisine_type):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")


restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)


restaurant.describe_restaurant()
restaurant.open_restaurant()


# 练习9-2：三家餐馆 　根据为完成练习9-1而编写的类创建三个实例，并对每个
# 实例调用方法describe_restaurant() 。
mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()

# 练习9-3：用户 　创建一个名为User 的类，其中包含属性first_name 和
# last_name ，以及用户简介通常会存储的其他几个属性。在类User 中定义一
# 个名为describe_user() 的方法，用于打印用户信息摘要。再定义一个名为
# greet_user() 的方法，用于向用户发出个性化的问候。


class User:
    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户。"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """显示用户信息摘要。"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """向用户发出个性化的问候。"""
        print(f"\nWelcome back, {self.username}!")


# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()

