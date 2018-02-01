import sys, os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

this_dir, this_filename = os.path.split(__file__)
ui_path = os.path.join(this_dir, "ui", "visualizer.ui")


class VisualizerWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(ui_path, self)
        print('GrahamVisualizer init success')
