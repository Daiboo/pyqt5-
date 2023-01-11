from PyQt5.QtWidgets import QPushButton,QWidget,QLineEdit,QApplication
import sys
"""
在GUI里，拖放是指用户点击一个虚拟的对象，拖动，然后放置到另外一个对象上面的动作。
一般情况下，需要调用很多动作和方法，创建很多变量。
拖放能让用户很直观的操作很复杂的逻辑。

一般情况下，我们可以拖放两种东西：数据和图形界面。
把一个图像从一个应用拖放到另外一个应用上的实质是操作二进制数据。
把一个表格从Firefox上拖放到另外一个位置 的实质是操作一个图形组。
"""

"""
本例使用了QLineEdit和QPushButton。把一个文本从编辑框里拖到按钮上，更新按钮上的标签（文字）。
"""

class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)

        self.setAcceptDrops(True)  # 激活组件的拖拽事件。


    def dragEnterEvent(self,event):
        if event.mimeData().hasFormat("text/plain"):
            event.accept()
        else:
            event.ignore()
    # 首先，我们重构了dragEnterEvent()方法。设定好接受拖拽的数据类型（plain text）。
    
    def dropEvent(self,event):
        self.setText(event.mimeData().text())
    # 然后重构dropEvent()方法，更改按钮接受鼠标的释放事件的默认行为。

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        edit = QLineEdit(" ",self)
        edit.setDragEnabled(True)  # QLineEdit默认支持拖拽操作，所以我们只要调用setDragEnabled()方法使用就行了。
        edit.move(30,65)

        button = Button("Button",self)
        button.move(230,65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
