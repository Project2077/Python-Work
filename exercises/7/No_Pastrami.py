# 练习7-9：五香烟熏牛肉卖完了 　使用为完成练习7-8而创建的列表
# sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。在程序
# 开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉
# （pastrami）卖完了；再使用一个while 循环将列表sandwich_orders 中
# 的'pastrami' 都删除。确认最终的列表finished_sandwiches 未包含'pastrami' 。

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == "pastrami":
        continue
    else:
        finished_sandwiches.append(sandwich)

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)