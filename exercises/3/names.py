# 请尝试编写一些简短的程序来完成下面的练习，以获得一些使用Python列表的第一
# 手经验。你可能需要为每章创建一个文件夹，以整洁有序的方式存储为完成各章的
# 练习而编写的程序。

# 练习3-1：姓名 　将一些朋友的姓名存储在一个列表中，并将其命名为names 。依
# 次访问该列表中的每个元素，从而将每个朋友的姓名打印出来。
names = ['mike', 'james', 'olive']
for name in names:
    print(name)
# 练习3-2：问候语 　继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每
# 人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
for name in names:
    message = f"Hello {name}, good to know you"
    print(message)
# 练习3-3：自己的列表 　想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一
# 个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，下
# 面是一个例子。
# I would like to own a Honda motorcycle.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
for bicycle in bicycles:
    message = f"\tI would like to own a {bicycle} bicycle"
    print(message)