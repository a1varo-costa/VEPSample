from .uigen import mainUI
from .      import rect
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore    import Qt


class MainUI(QMainWindow):
    def __init__(self, rectsinfo):
        super().__init__()

        self.ui = mainUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.rectsinfo = rectsinfo
        self._makeRects()

    def _makeRects(self):
        cnt, row, col, ff = 0, 0, 0, True
        for info in self.rectsinfo:
            r = rect.BlinkRect(label=info['label'], freq=info['freq'])
            
            col = cnt % 3
            row += 1 if (not ff) and (cnt == 0) else 0
            ff  = False
            cnt += 1

            self.ui.rectsGridlayout.addWidget(r, row, col, Qt.AlignCenter)
