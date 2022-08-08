# 练习8-7：专辑 　编写一个名为make_album() 的函数，它创建一个描述音乐
# 专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信
# 息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的
# 值，以核实字典正确地存储了专辑的信息。

def make_album(artist, title):
    """描述音乐专辑的字典"""
    album_dict = {
        "artist": artist,
        "title": title,
    }
    return album_dict


album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
# 给函数make_album() 添加一个默认值为None 的可选形参，以便存储专辑包
# 含的歌曲数。如果调用这个函数时指定了歌曲数，就将该值添加到表示专辑的
# 字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。


def make_album(artist, title, tracks=0):
    """描述音乐专辑的字典"""
    album_dict = {
        "artist": artist,
        "title": title,
    }
    if tracks:
        album_dict['tracks'] = tracks

    return album_dict


album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)


# 练习8-8：用户的专辑 　在为完成练习8-7编写的程序中，编写一个while 循
# 环，让用户输入专辑的歌手和名称。获取这些信息后，使用它们来调用函数
# make_album() 并将创建的字典打印出来。在这个while 循环中，务必提供退出途径。
def make_own_album():
    while True:
        # 生成提示语。
        title_prompt = "\nWhat album are you thinking of? "
        artist_prompt = "Who's the artist? "

        artist = input(artist_prompt)
        title = input(title_prompt)

        own_album = make_album(artist, title)
        print(own_album)


make_own_album()


