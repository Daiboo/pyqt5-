from PyQt5.QtWidgets import QWidget,QCalendarWidget,QLabel,QApplication,QVBoxLayout
from PyQt5.QtCore import QDate
import sys
"""
QCalendarWidget提供了基于月份的日历插件，十分简易而且直观。
这个例子有日期组件和标签组件组成，标签显示被选中的日期。
"""
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        cal = QCalendarWidget(self) # 创建一个QCalendarWidget。
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        # 选择一个日期时，QDate的点击信号就触发了，把这个信号和我们自己定义的showDate()方法关联起来。

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self,date):
        self.lbl.setText(date.toString())
    # 用selectedDate()方法获取选中的日期，然后把日期对象转成字符串，在标签里面显示出来。

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())