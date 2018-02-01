import sys, os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from graham.ui.gui_ui import Ui_MainWindow


class GUIWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print('GrahamGUI init success')
