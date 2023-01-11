import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QToolTip,QPushButton)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        QToolTip.setFont(QFont("SansSerif",10))  # setFont()这个静态方法设置了提示框的字体，我们使用了10px的SansSerif字体
        self.setToolTip("This is a <b>QWidget</b> widget") # 调用setToolTip()创建提示框可以使用富文本格式的内容。
        self.setWindowTitle("example")
        btn = QPushButton("Button",self)  # 创建一个按钮，并且为按钮添加了一个提示框。
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())  # 调整按钮大小，并让按钮在屏幕上显示出来，sizeHint()方法提供了一个默认的按钮大小。
        btn.move(50,50)

        self.setGeometry(300,300,300,500)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())