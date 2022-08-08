# 练习7-10：梦想的度假胜地 　编写一个程序，调查用户梦想的度假胜地。使用
# 类似于下面的提示，并编写一个打印调查结果的代码块。
# If you could visit one place in the world, where would you go?
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

v = {}
while True:
    name = input(name_prompt)
    place = input(place_prompt)

    v[name] = place

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break


# # 显示调查结果。
for name, place in v.items():
    print(f"{name}:{place}")


