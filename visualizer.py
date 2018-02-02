import sys
from PyQt5.QtWidgets import QApplication
from graham.visualizer import VisualizerWindow
from graham.algorithm import GrahamAlgorithm
from random import randint
from matplotlib import pyplot as plt


def create_points(count, min=-50, max=50):
    return [[randint(min, max), randint(min, max)] for _ in range(count)]


def scatter_plot(coords, convex_hull=None):
    xs, ys = zip(*coords)
    plt.scatter(xs, ys)

    if convex_hull != None:
        for i in range(1, len(convex_hull) + 1):
            if i == len(convex_hull): i = 0
            c0 = convex_hull[i - 1]
            c1 = convex_hull[i]
            plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'r')
    plt.show()


if __name__ == '__main__':
    # app = QApplication(sys.argv)

    # visualizer = VisualizerWindow()
    # visualizer.show()

    algo = GrahamAlgorithm()
    points = create_points(100)
    # points = [[3, 9], [5, 5], [2, 2], [1, 1], [8, 5], [11, 1], [1, 0], [19, -1], [1, -1], [20, -1], [-5, 0], [-4, 0], [-5, 1]]
    scatter_plot(points, algo.get_convex_points(points))

    # sys.exit(app.exec_())
