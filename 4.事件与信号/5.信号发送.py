import sys
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QMainWindow,QApplication
"""
QObject实例能发送事件信号。下面的例子是发送自定义的信号。
"""
class Commuicate(QObject):
    closeApp = pyqtSignal()
    # Communicate类创建了一个pyqtSignal()属性的信号。

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Commuicate()
        self.c.closeApp.connect(self.close)
        # closeApp信号QMainWindow的close()方法绑定。

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()
    # 我们创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())