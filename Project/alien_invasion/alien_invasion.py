import sys

import pygame

# 导入模块sys 和pygame 。模块pygame 包含开发游戏所需的功能。玩家退
# 出时，我们将使用模块sys 中的工具来退出游戏。
from settings import Settings

from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 在这个类的方法__init__() 中，调用函数pygame.init() 来初始化背景设
        # 置，让Pygame能够正确地工作
        # 调用pygame.display.set_mode() 来创建一个显示窗口，游戏的所有图形元素都将
        # 在其中绘制。
        # 实参(1200, 800) 是一个元组，指定了游戏窗口的尺寸——宽1200
        # 像素、高800像素（你可以根据自己的显示器尺寸调整这些值）。
        # 将这个显示窗口赋给属性self.screen ，让这个类中的所有方法都能够使用它。

        # 赋给属性self.screen 的对象是一个surface 。在Pygame中，surface是屏幕的一
        # 部分，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个
        # surface。display.set_mode() 返回的surface表示整个游戏窗口。激活游戏的
        # 动画循环后，每经过一次循环都将自动重绘这个surface，将用户输入触发的所有变化都反映出来。

        # # 设置背景色
        # self.bg_color = ((230, 230, 230))
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件。
            self._check_events()

            # 每次循环时都重绘屏幕。
            self._update_screen()

            # 让最近绘制的屏幕可见。
            pygame.display.flip()
    # 这个游戏由方法run_game() 控制。该方法包含一个不断运行的while 循环
    # 而这个循环包含一个事件循环以及管理屏幕更新的代码。
    # 事件 是用户玩游戏时执行的操作，如按键或移动鼠标。为程序响应事件，可编写一个事件循环 ，以侦
    # 听 事件并根据发生的事件类型执行合适的任务。
    # 此处for 循环就是一个事件循环。
    # 为访问Pygame检测到的事件，我们使用了函数pygame.event.get() 。这个函数
    # 返回一个列表，其中包含它在上一次被调用后发生的 所有 事件。

    # 所有键盘和鼠标事件都将导致这个for 循环运行。在这个循环中，我们将编写一系列if 语句来检测
    # 并响应特定的事件。例如，当玩家单击游戏窗口的关闭按钮时，将检测到
    # pygame.QUIT 事件，进而调用sys.exit() 来退出游戏

    # pygame.display.flip() ，命令Pygame让最近绘制的屏幕可见。在
    # 这里，它在每次执行while 循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。
    # 我们移动游戏元素时，pygame.display.flip() 将不断更新屏幕，
    # 以显示元素的新位置，并且在原来的位置隐藏元素，从而营造平滑移动的效果。    刷新画面帧

    def _check_events(self):
        """响应按键和鼠标事件。"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()

# 在这个文件末尾，创建一个游戏实例并调用run_game() 。这些代码放在一个if
# 代码块中，仅当直接运行该文件时，它们才会执行。如果此时运行
# alien_invasion.py，将看到一个空的Pygame窗口。

# 设置背景色
# Pygame默认创建一个黑色屏幕，这太乏味了。下面来将背景设置为另一种颜色，这
# 是在方法__init__() 末尾进行的

# 在Pygame中，颜色是以RGB值指定的。这种颜色由红色、绿色和蓝色值组成，其中每
# 个值的可能取值范围都是0～255。颜色值(255, 0, 0)表示红色，(0, 255, 0)表示
# 绿色，而(0, 0, 255)表示蓝色。通过组合不同的RGB值，可创建1600万种颜色。在
# 颜色值(230, 230, 230)中，红色、绿色和蓝色的量相同，它生成一种浅灰色。我们
# 将这种颜色赋给了self.bg_color
# 调用方法fill() 用这种背景色填充屏幕。方法fill() 用于处理surface，只接受一个实参：一种颜色。


# 重构：方法_check_events() 和__update_screen()
# 在大型项目中，经常需要在添加新代码前重构既有代码。重构旨在简化既有代码的
# 结构，使其更容易扩展。本节将把越来越长的方法run_game() 拆分成两个辅助方
# 法（helper method）。辅助方法 在类中执行任务，但并非是通过实例调用的。在Python中，辅助方法的名称以单个下划线打头。

# 把管理事件的代码移到一个名为_check_events() 的方法中，以简化
# run_game() 并隔离事件管理循环。通过隔离事件循环，可将事件管理与游戏的其
# 他方面（如更新屏幕）分离。

# 为进一步简化run_game() ，将更新屏幕的代码移到一个名为
# _update_screen() 的方法中

# 如果你开发过大量的游戏，可能早就开始像这样将代码放到不同的方法中了。不过
# 如果你从未开发过这样的项目，可能不知道如何组织代码。这里采用的做法是，先
# 编写可行的代码，等代码越来越复杂时再进行重构，以向你展示真正的开发过程：
# 先编写尽可能简单的代码，等项目越来越复杂后对其进行重构。  对代码进行重构使其更容易扩展后，可以开始处理游戏的动态方面了！
