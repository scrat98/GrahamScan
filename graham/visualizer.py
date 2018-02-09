import sys, os
from random import randint

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic, QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from graham.algorithm import GrahamAlgorithm
from graham.ui.visualizer_ui import Ui_MainWindow


class MplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)


class VisualizerWindow(QMainWindow, Ui_MainWindow):
    algo = GrahamAlgorithm()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        l = QtWidgets.QVBoxLayout(self.centralwidget)
        self.plot = MplCanvas(self.centralwidget, width=5, height=4, dpi=100)
        l.addWidget(self.plot)

        self.update_plot()
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_plot)
        timer.start(1000)
        print('GrahamVisualizer init success')

    def update_plot(self):
        self.plot.axes.clear()

        min_coor = randint(-1000, 1000)
        max_coor = randint(min_coor, min_coor + 1000)
        count = randint(10, 100)

        points = [[randint(min_coor, max_coor), randint(min_coor, max_coor)] for _ in range(count)]
        xs, ys = zip(*points)
        self.plot.axes.scatter(xs, ys)

        convex_hull = self.algo.get_convex_points(points)
        for i in range(1, len(convex_hull) + 1):
            if i == len(convex_hull):
                i = 0
            c0 = convex_hull[i - 1]
            c1 = convex_hull[i]
            self.plot.axes.plot((c0[0], c1[0]), (c0[1], c1[1]), 'r')

        self.plot.draw()
