import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import  QIcon
"""
窗口图标通常是显示在窗口的左上角，标题栏的最左边。下面的例子就是怎么用PyQt5创建一个这样的窗口。
"""


class Example(QWidget):
    def __init__(self):
        super().__init__()   # super()构造器方法返回父级的对象。
       
        self.initUI()  #  使用initUI()方法创建一个GUI。
        
    def initUI(self):
        self.setGeometry(1000,300,300,220)  # setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小
        # 参数分别代表屏幕坐标的x、y和窗口大小的宽、高。
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("E:\PythonProject\pyqt5教程\hello world\图层1.png"))
        # 最后一个方法是添加了图标。先创建一个QIcon对象，然后接受一个路径作为参数显示图标。
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

