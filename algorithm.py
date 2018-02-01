import sys
from PyQt5.QtWidgets import QApplication
from graham.algorithm import GrahamAlgorithm

if __name__ == '__main__':
    app = QApplication(sys.argv)

    algo = GrahamAlgorithm()
    points = [[3, 9], [8, 5], [11, 1], [1, 0], [19, -1]]

    print(algo.get_convex_indices(points))
    print(algo.get_convex_points(points))

    sys.exit(app.exec_())
