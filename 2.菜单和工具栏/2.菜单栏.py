import sys
from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
"""
菜单栏是非常常用的。是一组命令的集合
在上面的示例中，我们创建了只有一个命令的菜单栏，这个命令就是终止应用。
同时也创建了一个状态栏。而且还能使用快捷键Ctrl+Q退出应用。
"""

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        exitAct = QAction(QIcon("exit.png"),"&Exit",self)
        # QAction是菜单栏、工具栏或者快捷键的动作的组合。
        exitAct.setShortcut("Ctrl+Q")
        # 创建了一个图标、一个exit的标签和一个快捷键组合，都执行了一个动作；
        exitAct.setStatusTip("Exit application")
        # 创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。
        exitAct.triggered.connect(QCoreApplication.instance().quit)
        # 当执行这个指定的动作时，就触发了一个事件。
        # 这个事件跟QApplication的quit()行为相关联，所以这个动作就能终止这个应用。

        self.statusBar()

        menubar = self.menuBar()  # menuBar()创建菜单栏。这里创建了一个菜单栏

        fileMenu = menubar.addMenu("&File")  # 并用addMenu()在上面添加了一个file菜单，
        fileMenu.addAction(exitAct) # 用addAction()关联了点击退出应用的事件。

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("simple menu")
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
