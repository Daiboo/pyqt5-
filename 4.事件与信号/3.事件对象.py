import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLabel
from PyQt5.QtCore import Qt

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
        grid.addWidget(self.label,0,0,Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self,event):
        x = event.x()
        y = event.y()

        text = "x:{0}, y={1}".format(x, y)
        self.label.setText(text)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())