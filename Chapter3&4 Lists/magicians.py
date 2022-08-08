# 我们经常需要遍历列表的所有元素，对每个元素执行相同的操作。
# for循环

# 假设我们有一个魔术师名单，需要将其中每个魔术师的名字都打印出来。为此，可
# 以分别获取名单中的每个名字，但这种做法会导致多个问题。例如，如果名单很
# 长，将包含大量重复的代码。另外，每当名单的长度发生变化时，都必须修改代
# 码。通过使用for 循环，可以让Python去处理这些问题。

magicians=['alice','david','carolina']
for magician in magicians:
	print(magician)

# 循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。

# for magician in magicians:
# 这行代码让Python获取列表magicians 中的第一个值'alice' ，并将其与变量magician 相关联。
# 接下来，Python读取下一行代码 
# print(magician)
# 它让Python打印magician 的值，依然是'alice' 。鉴于该列表还包含其他值，Python返回到循环的第一行
# for magician in magicians
# Python获取列表中的下一个名字'david'，并将其与变量magician相关联，再执行下面这行代码
# print(magician)    之后反复这个流程直至没有其它值

# 刚开始使用循环时请牢记，对列表中的每个元素，都将执行循环指定的步骤，而不
# 管列表包含多少个元素。如果列表包含一百万个元素，Python就重复执行指定的步
# 骤一百万次，且通常速度非常快。    会自动停止的


for magician in magicians:
	print(f"{magician.title()},that was a great trick!")
# 在for 循环中，想包含多少行代码都可以。在代码行for magician in
# magicians 后面，每个缩进的代码行都是循环的一部分，将针对列表中的每个值
# 都执行一次。因此，可对列表中的每个值执行任意次数的操作。




for magician in magicians:
 	print(f"{magician.title()}, that was a great trick!")
 	print(f"I can't wait to see your next trick, {magician.title()}.\n")
# 在for 循环后面，没有缩进的代码都只执行一次，不会重复执行。
print("Thank you, everyone. That was a great magic show!")








