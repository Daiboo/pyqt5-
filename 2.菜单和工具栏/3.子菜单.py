import sys
from PyQt5.QtWidgets import QMainWindow,QAction,QMenu,QApplication
"""
子菜单是嵌套在菜单里面的二级或者三级等的菜单。
这个例子里，有两个子菜单，一个在File菜单下面，一个在File的Import下面。
"""


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")

        impMenu = QMenu("Import",self) # 使用QMenu创建一个新菜单。
        impAct = QAction("Import mail",self)  
        impMenu.addAction(impAct)  # 使用addAction()添加一个动作

        newAct = QAction("New",self)  

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu) 

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')    
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())       