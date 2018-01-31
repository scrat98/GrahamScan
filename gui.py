import sys
from PyQt5.QtWidgets import QApplication
from graham.gui import GUIWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = GUIWindow()
    gui.show()

    sys.exit(app.exec_())
