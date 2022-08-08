# 练习8-9：消息 　创建一个列表，其中包含一系列简短的文本消息。将该列表
# 传递给一个名为show_messages() 的函数，这个函数会打印列表中的每条文本消息。
message = ["Yes,I am", "Here you are", "What are you talking about?", "Next time", "WTF"]


def show_messages(texts):
    """打印列表中的每条文本消息"""
    for text in texts:
        print(text)


show_messages(message)


# 练习8-10：发送消息 　在你为完成练习8-9而编写的程序中，编写一个名为
# send_messages() 的函数，将每条消息都打印出来并移到一个名为
# sent_messages 的列表中。调用函数send_messages() ，再将两个列表都
# 打印出来，确认正确地移动了消息。


def send_messages(texts, sent_messages):
    """将每条消息都打印出来并移到一个名为sent_messages 的列表中"""
    while texts:
        poped_message = texts.pop()
        print(poped_message)

        sent_messages.append(poped_message)


sent_messages = []

# send_messages(message)
# print(sent_messages)
# print(message)


# 练习8-11：消息归档 　修改你为完成练习8-10而编写的程序，在调用函数
# send_messages() 时，向它传递消息列表的副本。调用函数
# send_messages() 后，将两个列表都打印出来，确认保留了原始列表中的消息。
send_messages(message[:], sent_messages)
print(sent_messages)
print(message)

