from PyQt5.QtWidgets import QWidget,QProgressBar,QPushButton,QApplication
from PyQt5.QtCore import QBasicTimer
import sys
"""
进度条是用来展示任务进度的.
它的滚动能让用户了解到任务的进度。
QProgressBar组件提供了水平和垂直两种进度条，进度条可以设置最大值和最小值，默认情况是0~99。

"""
"""
我们创建了一个水平的进度条和一个按钮，这个按钮控制进度条的开始和停止。
"""

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)  # 新建一个QProgressBar构造器。
        self.pbar.setGeometry(30,40,200,25)

        self.btn = QPushButton("Start",self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer() # 用时间控制进度条。
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self,event):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText("Finished")
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        # 每个QObject和又它继承而来的对象都有一个timerEvent()事件处理函数。为了触发事件，我们重载了这个方法。
    
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("Start")
        else:
            self.timer.start(100,self)
            # 调用start()方法加载一个时间事件。这个方法有两个参数：过期时间和事件接收者。
            self.btn.setText("Stop")
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())              
