import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
"""
QMainWindow提供了主窗口的功能，使用它能创建一些简单的状态栏、工具栏和菜单栏。
"""
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.statusBar().showMessage("ready")
        # 调用QtGui.QMainWindow类的statusBar()方法，创建状态栏。
        # 第一次调用会创建一个状态栏，而再次调用会返回一个状态栏对象。
        # showMessage()方法在状态栏上显示一条信息。
        self.setGeometry(300,300,250,150)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

