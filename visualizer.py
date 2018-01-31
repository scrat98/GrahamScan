import sys
from PyQt5.QtWidgets import QApplication
from graham.visualizer import VisualizerWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    visualizer = VisualizerWindow()
    visualizer.show()

    sys.exit(app.exec_())
