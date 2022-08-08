# 嵌套

# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为
# 嵌套 。  俄罗斯套娃

# 字典列表

# 字典alien_0 包含一个外星人的各种信息，但无法存储第二个外星人的信息，更别
# 说屏幕上全部外星人的信息了。如何管理成群结队的外星人呢？一种办法是创建一
# 个外星人列表，其中每个外星人都是一个字典，包含有关该外星人的各种信息。例
# 如，下面的代码创建一个包含三个外星人的列表：

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
# 上边3是字典 下边这个是列表
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# 更符合现实的情形是，外星人不止三个，且每个外星人都是使用代码自动生成的。
# 创建一个用于存储外星人的空列表。
aliens = []

#创建30个绿色的外星人。
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# 显示前5个外星人。
for alien in aliens[:5]:
	print(alien)
print("...")

# 显示创建了多少个外星人。
print(f"Total number of aliens: {len(aliens)}")


# 要修改前三个外星人，我们遍历一个只包含这些外星人的切片。
# 当前，所有外星人都是绿色的，但情况并非总是如此，因此编写一条if 语句来确保只修改绿色外
# 星人。如果外星人是绿色的，就将其颜色改为'yellow' ，将其速度改
# 为'medium' ，并将其分数改为10

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15


