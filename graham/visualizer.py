import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class VisualizerWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # uic.loadUi('GrahamVisualizer.ui', self)
        print('GrahamVisualizer init success')
