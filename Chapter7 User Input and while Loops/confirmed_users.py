# 使用while 循环处理列表和字典
# 到目前为止，我们每次都只处理了一项用户信息：获取用户的输入，再将输入打印
# 出来或做出应答；循环再次运行时，获悉另一个输入值并做出响应。然而，要记录
# 大量的用户和信息，需要在while 循环中使用列表和字典。

# for 循环是一种遍历列表的有效方式，但不应在for 循环中修改列表，否则将导致
# Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while 循
# 环。通过将while 循环同列表和字典结合起来使用，可收集、存储并组织大量输
# 入，供以后查看和显示。

# 在列表之间移动元素

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表。
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止。
# 将每个经过验证的用户都移到已验证用户列表中。
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
# while 循环将不断运行，直到列表unconfirmed_users 变成空的
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已验证的用户。
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
