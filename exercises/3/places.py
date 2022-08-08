# 练习3-8：放眼世界 　想出至少5个你渴望去旅游的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
places = ['London', 'New York', 'Tokyo', 'Paris', 'Los Angel']

# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
print(places)

# 使用sorted() 按字母顺序打印这个列表，同时不要修改它。
sorted_places = sorted(places)
print(f"This is sorted_places:\n\t{sorted_places}")
# 再次打印该列表，核实排列顺序未变。
print(f"This is original:\n\t{places}")
# 使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
sorted_places = sorted(places, reverse=True)
print(f"This is sorted_places(reverse):\n\t{sorted_places}")
# 再次打印该列表，核实排列顺序未变。
print(f"This is original:\n\t{places}")
# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
places.reverse()
print(f"This is original(reverse):\n\t{places}")
# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
places.reverse()
print(f"This is original(reverse*2):\n\t{places}")
# 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
places.sort()
print(f"This is original(sort):\n\t{places}")
# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
places.sort(reverse=True)
print(f"This is original(sort_reverse):\n\t{places}")
# 练习3-9：晚餐嘉宾 　在完成练习3-4~练习3-7时编写的程序之一中，使用
# len() 打印一条消息，指出你邀请了多少位嘉宾来共进晚餐。  见guests.py
# 练习3-10：尝试使用各个函数 　想想可存储到列表中的东西，如山川、河流、
# 国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含
# 这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
chess = ['king', 'queen', 'knight', 'rook', 'bishop', 'pawn']
chess[1] = "Queen"
chess.append("pawn")
del chess[5]
poped_chess = chess.pop()
poped_chess = chess.pop(3)
chess.insert(3, "pawn")
print(chess)
chess.insert(-1, "rook")

print(chess)

print(sorted(chess))
print(sorted(chess, reverse=True))
chess.reverse()
print(chess)
chess.sort()
print(chess)

# 练习3-11：有意引发错误 　如果你还没有在程序中遇到过索引错误，就尝试引
# 发一个这种错误。在你的一个程序中，修改其中的索引，以引发索引错误。关
# 闭程序前，务必消除这个错误。
# len_chess = len(chess)
# print(len_chess)
# print(chess[6])
