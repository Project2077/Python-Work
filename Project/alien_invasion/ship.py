# 添加飞船图像

# 下面将飞船加入游戏中。为了在屏幕上绘制玩家的飞船，我们将加载一幅图像，再
# 使用Pygame方法blit() 绘制它。

# 为游戏选择素材时，务必要注意许可。最安全、最不费钱的方式是使用Pixabay等网
# 站提供的免费图形，无须授权许可即可使用并修改。
# 在游戏中几乎可以使用任何类型的图像文件，但使用位图（.bmp）文件最为简单，
# 因为Pygame默认加载位图。虽然可配置Pygame以使用其他文件类型，但有些文件类
# 型要求你在计算机上安装相应的图像库。大多数图像为.jpg、.png或.gif格式，但
# 可使用Photoshop、GIMP和Paint等工具将其转换为位图。

# 选择图像时，要特别注意背景色。请尽可能选择背景为透明或纯色的图像，便于使
# 用图像编辑器将其背景替换为任意颜色。图像的背景色与游戏的背景色匹配时，游
# 戏看起来最漂亮。你也可以将游戏的背景色设置成图像的背景色。

# 就游戏《外星人入侵》而言，可使用文件ship.bmp，该文件可在
# 本书主页（ituring.cn/book/2784）的“随书下载”中找到。这个文件的背景色与
# 项目使用的设置相同。请在项目文件夹（alien_invasion）中新建一个名为images
# 的文件夹，并将文件ship.bmp保存在其中。

# 创建Ship 类

import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置。"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形。
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数值。
        self.x = float(self.rect.x)
        # 通过将速度设置指定为小数值，可在后面加快游戏节奏时更细致地控制飞船的速
        # 度。然而，rect 的x 等属性只能存储整数值，因此需要对Ship 类做些修改

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    # 方法update() 将通过Ship 实例来调用，因此不是辅助方法。
    # 限制飞船的活动范围
    # 在修改self.x 的值之前检查飞船的位置。self.rect.right 返回飞船
    # 外接矩形右边缘的 坐标。如果这个值小于self.screen_rect.right 的值，就说明飞船未触及屏幕右边缘
    # 左边缘的情况与此类似：如果rect 左边缘的坐标大于零，就说明飞船未触及屏幕左边缘
    def update(self):
        """根据移动标志调整飞船的位置。"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据self.x更新rect对象。
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船。"""
        self.screen.blit(self.image, self.rect)

# Pygame之所以高效，是因为它让你能够像处理矩形（rect 对象）一样处理所有的
# 游戏元素，即便其形状并非矩形。像处理矩形一样处理游戏元素之所以高效，是因
# 为矩形是简单的几何形状。例如，通过将游戏元素视为矩形，Pygame能够更快地判
# 断出它们是否发生了碰撞。这种做法的效果通常很好，游戏玩家几乎注意不到我们
# 处理的并不是游戏元素的实际形状。在这个类中，我们将把飞船和屏幕作为矩形进行处理。

# Ship 的方法__init__() 接受两个参
# 数：引用self 和指向当前AlienInvasion 实例的引用。这让Ship 能够访问
# AlienInvasion 中定义的所有游戏资源。
# self.screen = ai_game.screen 将屏幕赋给了Ship 的一个属性，以便在这个类的所有方法中轻松访问。

# self.screen_rect = ai_game.screen.get_rect() 使用方法get_rect() 访问屏
# 幕的属性rect ，并将其赋给了self.screen_rect ，这让我们能够将飞船放到屏幕的正确位置。
# 调用pygame.image.load() 加载图像，并将飞船图像的位置传递给它
# 该函数返回一个表示飞船的surface，而我们将这个surface赋给了self.image 。
# 加载图像后，使用get_rect() 获取相应surface的属性rect ，以便后面能够使用它来指定飞船的位置。

# 处理rect 对象时，可使用矩形四角和中心的 坐标和 坐标。可通过设置这些值来
# 指定矩形的位置。要让游戏元素居中，可设置相应rect 对象的属性center 、
# centerx 或centery ；要让游戏元素与屏幕边缘对齐，可使用属性top 、
# bottom 、left 或right 。除此之外，还有一些组合属性，如midbottom 、
# midtop 、midleft 和midright 。要调整游戏元素的水平或垂直位置，可使用
# 属性x 和y ，分别是相应矩形左上角的 坐标和 坐标。这些属性让你无须做游戏
# 开发人员原本需要手工完成的计算，因此会经常用到。

# 注意 　在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将
# 增大。在1200 × 800的屏幕上，原点位于左上角，而右下角的坐标为(1200,
# 800)。这些坐标对应的是游戏窗口，而不是物理屏幕。

# 在屏幕上绘制飞船
# 更新alien_invasion.py，创建一艘飞船并调用其方法blitme()


