# 练习7-1：汽车租赁 　编写一个程序，询问用户要租赁什么样的汽车，并打印
# 一条消息，下面是一个例子。 Let me see if I can find you a Subaru.
car = input("What kind of car would you like? ")
print(f"Let me see if I can find you a {car.title()}.")

# 练习7-2：餐馆订位 　编写一个程序，询问用户有多少人用餐。如果超过8位，
# 就打印一条消息，指出没有空桌；否则指出有空桌。

party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)
if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

# 练习7-3：10的整数倍 　让用户输入一个数，并指出该数是否是10的整数倍。
number = input("please enter a number")
number = int(number)
if number % 10 == 0:
    print("这个数是10的整倍数")
else:
    print(f"{number} is not a multiple of 10.")

