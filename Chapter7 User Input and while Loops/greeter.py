# 编写清晰的程序
# 每当使用函数input() 时，都应指定清晰易懂的提示，准确地指出希望用户提供什
# 么样的信息——指出用户应该输入何种信息的任何提示都行
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# 通过在提示末尾（这里是冒号后面）包含一个空格，可将提示与用户输入分开，让
# 用户清楚地知道其输入始于何处

# 有时候，提示可能超过一行。例如，你可能需要指出获取特定输入的原因。在这种
# 情况下，可将提示赋给一个变量，再将该变量传递给函数input() 。这样，即便提
# 示超过一行，input() 语句也会非常清晰。
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

