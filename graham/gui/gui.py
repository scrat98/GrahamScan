import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from graham.algorithm import GrahamAlgorithm
from graham.visualizer import VisualizerWindow

class GUIWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # uic.loadUi('GrahamGUI.ui', self)
        print('GrahamGUI init success')
