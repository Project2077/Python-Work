# 练习8-1：消息 　编写一个名为display_message() 的函数，它打印一个句
# 子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。

def display_message():
    """显示一条消息，指出你在本章学的是什么。"""
    msg = "I'm learning to store code in functions."
    print(msg)


display_message()


# 练习8-2：喜欢的图书 　编写一个名为favorite_book() 的函数，其中包含
# 一个名为title 的形参。这个函数打印一条消息，下面是一个例子。
# One of my favorite books is Alice in Wonderland.
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("Alice in Wonderland")
