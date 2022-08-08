# 练习9-4：就餐人数 　在为完成练习9-1而编写的程序中，添加一个名为
# number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为
# restaurant 的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。

# 添加一个名为set_number_served() 的方法，让你能够设置就餐人数。调
# 用这个方法并向它传递一个值，然后再次打印这个值。

# 添加一个名为increment_number_served() 的方法，让你能够将就餐人数
# 递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

class Restaurant:
    def __init__(self, name, cuisine_type, number_served=0):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number):
        """设置就餐人数 调用这个方法并向它传递一个值"""
        self.number_served = number

    def increment_number_served(self, number):
        """就餐人数递增"""
        self.number_served += number

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

# restaurant.number_served = 10
restaurant.set_number_served(16)
print(f"The restaurant has served {restaurant.number_served} people.")
restaurant.increment_number_served(26)
print(f"The restaurant has served {restaurant.number_served} people.")

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 练习9-5：尝试登录次数 　在为完成练习9-3而编写的User 类中，添加一个名
# 为login_attempts 的属性。编写一个名为increment_login_attempts() 的方法，将属性login_attempts 的值
# 加1。再编写一个名为reset_login_attempts() 的方法，将属性login_attempts 的值重置为0。

# 根据User 类创建一个实例，再调用方法increment_login_attempts()
# 多次。打印属性login_attempts 的值，确认它被正确地递增。然后，调用
# 方法reset_login_attempts() ，并再次打印属性login_attempts 的
# 值，确认它被重置为0。
class User:
    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户。"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """显示用户信息摘要。"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """向用户发出个性化的问候。"""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()

print(willie.login_attempts)
willie.increment_login_attempts()
willie.increment_login_attempts()
willie.increment_login_attempts()
print(willie.login_attempts)
willie.reset_login_attempts()
print(willie.login_attempts)