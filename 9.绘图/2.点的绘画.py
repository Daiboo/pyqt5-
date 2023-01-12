from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys,random
"""
我们在窗口里随机的画出了1000个点。
"""

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 190)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self,qp):
        qp.setPen(Qt.red)  # 设置笔的颜色为红色，使用的是预定义好的颜色。
        size = self.size()  # 每次更改窗口大小，都会产生绘画事件，从size()方法里获得当前窗口的大小，

        for i in range(1000):
            x = random.randint(1,size.width()-1)
            y = random.randint(1,size.height()-1)
            qp.drawPoint(x,y)
            # 然后把产生的点随机的分配到窗口的所有位置上。


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())