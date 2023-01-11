import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QApplication
"""
使用盒布局能让程序具有更强的适应性。这个才是布局一个应用的更合适的方式。
QHBoxLayout和QVBoxLayout是基本的布局类，分别是水平布局和垂直布局。
如果我们需要把两个按钮放在程序的右下角，创建这样的布局，我们只需要一个水平布局加一个垂直布局的盒子就可以了。
再用弹性布局增加一点间隙。
"""
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        # 这是创建了两个按钮。

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # 创建一个水平布局，并增加弹性空间和两个按钮。
        # stretch函数在两个按钮前面增加了一块弹性空间，它会将按钮挤到窗口的右边。
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        # 为了布局需要，我们把这个水平布局放到了一个垂直布局盒里面。弹性元素会把水平布局挤到窗口的下边。

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())