from PyQt5.QtWidgets import QPushButton,QWidget,QApplication
from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtGui import QDrag
import sys
"""
例子展示怎么拖放一个button组件。

口上有一个QPushButton组件。左键点击按钮，控制台就会输出press。右键可以点击然后拖动按钮。
"""
class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
    # 从QPushButton继承一个Button类

    # 然后重构QPushButton的两个方法:mouseMoveEvent()和mousePressEvent()
    # mouseMoveEvent()是拖拽开始的事件。
    def mouseMoveEvent(self,event): 
        if event.buttons() != Qt.RightButton:  # 我们只劫持按钮的右键事件，左键的操作还是默认行为
            return 

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        # 创建一个QDrag对象，用来传输MIME-based数据。
        
        dragAction = drag.exec_(Qt.MoveAction) # 拖放事件开始时，用到的处理函数式start().

    def mousePressEvent(self,event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            print("press")
    # 左键点击按钮，会在控制台输出“press”。
    # 注意，我们在父级上也调用了mousePressEvent()方法，不然的话，我们是看不到按钮按下的效果的。

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button("Button",self)
        self.button.move(100,65)

        self.setWindowTitle("Click or move")
        self.setGeometry(300,300,200,150)

    def dragEnterEvent(self,event):
        event.accept()

    def dropEvent(self,event):
        position = event.pos()
        self.button.move(position)
        # 我们定义了按钮按下后和释放后的行为，获得鼠标移动的位置，然后把按钮放到这个地方。
    
        event.setDropAction(Qt.MoveAction)
        event.accept()
        # 指定放下的动作类型为moveAction。

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

