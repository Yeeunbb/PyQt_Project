import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Instrument(QWidget):
    def __init__(self):
        super().__init__()
        self.beamText = QLabel('Beamforming 프레임 속도', self)
        self.beamforming1 = QRadioButton('기본 (50 fps)', self)
        self.beamforming1.setGeometry(50, 50, 100, 100)
        self.beamforming2 = QRadioButton('초고속 (100 fps)', self)
        self.beamforming2.setGeometry(150, 100, 150, 100)
