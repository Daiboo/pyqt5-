from PyQt5.QtWidgets import QWidget,QPushButton,QFrame,QColorDialog,QApplication
import sys
from PyQt5.QtGui import QColor
"""
QColorDialog提供颜色的选择。

例子里有一个按钮和一个QFrame，默认的背景颜色为黑色，我们可以使用QColorDialog改变背景颜色。
"""


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        col = QColor(0,0,0)  # 初始化QtGui.QFrame的背景颜色。
        self.btn = QPushButton("Dialog",self)
        self.move(20,20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-color:%s}" % col.name())
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()


    def showDialog(self):
        col = QColorDialog.getColor()  # 弹出一个QColorDialog对话框。

        if col.isValid():
            self.frm.setStyleSheet("QWidget {background-color:%s}" % col.name())
        # 我们可以预览颜色，如果点击取消按钮，没有颜色值返回，如果颜色是我们想要的，就从取色框里选择这个颜色。
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())