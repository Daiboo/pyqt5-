from PyQt5.QtWidgets import QPushButton,QWidget,QApplication
from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtGui import QDrag
import sys

class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)



    def mouseMoveEvent(self,event):
        if event.buttons() != Qt.RightButton:
            return 

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        
        dragAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self,event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            print("press")

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

        event.setDropAction(Qt.MoveAction)
        event.accept()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

