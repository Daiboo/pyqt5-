from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush
import sys

"""
我们画出了三个颜色的矩形。
"""
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangle(qp)
        qp.end()

    def drawRectangle(self,qp):
        col = QColor(0,0,0)  
        col.setNamedColor("#d4d4d4")
        # 使用16进制的方式定义一个颜色。
        qp.setPen(col)
        
        qp.setBrush(QColor(200,0,0))
        qp.drawRect(10,15,90,60)
        # 定义了一个笔刷，并画出了一个矩形。笔刷是用来画一个物体的背景。
        # drawRect()有四个参数，分别是矩形的x、y、w、h。 然后用笔刷和矩形进行绘画。

        qp.setBrush(QColor(255,80,0,160))
        qp.drawRect(130,15,90,60)

        qp.setBrush(QColor(25,0,90,200))
        qp.drawRect(250,15,90,60)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
