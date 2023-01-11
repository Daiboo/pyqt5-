from PyQt5.QtWidgets import QWidget,QSlider,QLabel,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
"""
QSlider是个有一个小滑块的组件，这个小滑块能拖着前后滑动，这个经常用于修改一些具有范围的数值
，比文本框或者点击增加减少的文本框（spin box）方便多了。
"""
"""
本例用一个滑块和一个标签展示。标签为一个图片，滑块控制标签（的值）。
"""

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal,self)  #  创建一个水平的QSlider。
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.changeValue)  # 把valueChanged信号跟changeValue()方法关联起来。

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("6.控件1\静音_mute.svg"))  # 创建一个QLabel组件并给它设置一个静音图标。
        self.label.setGeometry(160,40,80,30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValue(self,value):
        if value == 0:
            self.label.setPixmap(QPixmap("6.控件1\静音_mute.svg"))
        elif value > 0 and value <= 50:
            self.label.setPixmap(QPixmap("6.控件1\音量减小_volume-down.svg"))
        else:
            self.label.setPixmap(QPixmap("6.控件1\音量增大_volume-up.svg"))

        # 根据音量值的大小更换标签位置的图片。这段代码是：如果音量为0，就把图片换成 mute.png。
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
