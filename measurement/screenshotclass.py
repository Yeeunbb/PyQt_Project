from PyQt5.QtCore import QDir, Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class Screenshot(QWidget):
    def __init__(self):
        super(Screenshot, self).__init__()

        self.shootScreen()
        self.saveScreenshot()

    def saveScreenshot(self):
        format = 'png'
        initialPath = QDir.currentPath() + "/untitled." + format

        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        if fileName:
            self.originalPixmap.save(fileName, format)

    def shootScreen(self):

        screen = QApplication.primaryScreen()
        if screen is not None:
            self.originalPixmap = screen.grabWindow(0)
        else:
            self.originalPixmap = QPixmap()