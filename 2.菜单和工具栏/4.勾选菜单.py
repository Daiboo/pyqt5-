import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction
"""
下面是一个勾选菜单的例子
本例创建了一个行为菜单。这个行为／动作能切换状态栏显示或者隐藏。
"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("ready")

        menubar = self.menuBar()

        viewMenu = menubar.addMenu("View")

        viewStatAct = QAction("View Statusbar",self,checkable=True) # 用checkable选项创建一个能选中的菜单。
        viewStatAct.setStatusTip("View statusbar")  # 默认设置为选中状态。
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')    
        self.show()
    
    def toggleMenu(self,state):  # 依据选中状态切换状态栏的显示与否
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())