from app import gui
from PyQt5.QtWidgets import QApplication

from sys import exit

if __name__ == '__main__':
    app = QApplication([])

    rects = (
            {'label': 'A', 'freq': 5},
            {'label': 'B', 'freq': 30}
        )
    win = gui.MainUI(rects)
    win.show()

    exit(app.exec_())
