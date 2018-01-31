import sys
from PyQt5.QtWidgets import QApplication
from graham.algorithm import GrahamAlgorithm

if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = GrahamAlgorithm()

    sys.exit(app.exec_())
