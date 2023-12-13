from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from textBox import TextBox
from mycanvas import *
from mymodel import *

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600,200,600,400)
        self.setWindowTitle("MyGLDrawer")
        self.textBox = TextBox()
        self.canvas = MyCanvas(self.textBox)
        self.setCentralWidget(self.canvas)
        # create a model object and pass to canvas
        self.model = MyModel()
        self.canvas.setModel(self.model)

        # create a Toolbar
        tb = self.addToolBar("File")

        # add insertText
        boxText = QAction("RAIO",self)
        tb.addAction(boxText)

        # add insertText
        saveJson = QAction("JSON",self)
        tb.addAction(saveJson)

        tb.actionTriggered[QAction].connect(self.tbpressed)


    def tbpressed(self,action):
        if action.text() == "RAIO":
            self.textBox.show()
        elif action.text() == "JSON":
            self.model.saveMesh(600, 7850, 210000000000.0, 0.00004)
            self.close()