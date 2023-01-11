import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLabel
from PyQt5.QtCore import Qt
"""
事件对象是用python来描述一系列的事件自身属性的对象。
这个示例中，我们在一个组件里显示鼠标的X和Y坐标。
"""
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x:{0}, y={1}".format(x, y)

        self.label = QLabel(self.text,self)
        # X Y坐标显示在QLabel组件里

        grid.addWidget(self.label,0,0,Qt.AlignTop)

        self.setMouseTracking(True)
        # 事件追踪默认没有开启，当开启后才会追踪鼠标的点击事件。

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self,event):
        x = event.x()
        y = event.y()

        text = "x:{0}, y={1}".format(x, y)
        self.label.setText(text)
        # e代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。
        # x()和y()方法得到鼠标的x和y坐标点，然后拼成字符串输出到QLabel组件里。
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())