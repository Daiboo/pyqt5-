import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication
# QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(250,250)
        self.center()
        self.setWindowTitle("Center")
        self.show()
    def center(self):
        qr = self.frameGeometry()  # 获得主窗口所在的框架
        
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        qr.moveCenter(cp)    # 然后把主窗口框架的中心点放置到屏幕的中心位置。
        self.move(qr.topLeft())  # 然后通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了。

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
