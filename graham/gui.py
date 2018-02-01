from PyQt5.QtWidgets import QMainWindow


class GUIWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # uic.loadUi('GrahamGUI.ui', self)
        print('GrahamGUI init success')
