import sys

import pygame

# 导入模块sys 和pygame 。模块pygame 包含开发游戏所需的功能。玩家退
# 出时，我们将使用模块sys 中的工具来退出游戏。


class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
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

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件。
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
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


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()

# 在这个文件末尾，创建一个游戏实例并调用run_game() 。这些代码放在一个if
# 代码块中，仅当直接运行该文件时，它们才会执行。如果此时运行
# alien_invasion.py，将看到一个空的Pygame窗口。
