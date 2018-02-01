import sys, os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from graham.ui.visualizer_ui import Ui_MainWindow


class VisualizerWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print('GrahamVisualizer init success')
