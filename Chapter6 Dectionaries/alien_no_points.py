# 使用get() 来访问值

# 使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：如果指定的
# 键不存在就会出错。   如 
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# 这将导致Python显示traceback，指出存在键值错误（KeyError ）

# 第10章将详细介绍如何处理类似的错误，但就字典而言，可使用方法get() 在指定
# 的键不存在时返回一个默认值，从而避免这样的错误。

# 方法get() 的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存
# 在时要返回的值，是可选的： 第二个值不写会返回None
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)





# 如果字典中有键'points' ，将获得与之相关联的值；如果没有，将获得指定的默
# 认值。虽然这里没有键'points' ，但将获得一条清晰的消息，不会引发错误
# 如果指定的键有可能不存在，应考虑使用方法get() ，而不要使用方括号表示法。

# 注意 　调用get() 时，如果没有指定第二个参数且指定的键不存在，Python
# 将返回值None 。这个特殊值表示没有相应的值。None 并非错误，而是一个表
# 示所需值不存在的特殊值，第8章将介绍它的其他用途。

