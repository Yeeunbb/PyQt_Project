import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


# setting page 1
class SettingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setting_stack = QStackedWidget(self)

    def initUI(self):
        self.setWindowTitle("Setting Page")
        self.resize(720, 480)


        self.back_to_main = QPushButton(self)
        self.back_to_main.setIcon(QIcon('icons/go-back.jpg'))
        self.back_to_main.setIconSize(QSize(40, 40))
        self.back_to_main.setMaximumHeight(700)
        self.back_to_main.setMaximumWidth(950)
        self.back_to_main.setStyleSheet(
            "QPushButton { color: black; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )


        self.instrument_btn = QPushButton(flat=True)
        self.instrument_btn.setIcon(QIcon('icons/instrument-panel.png'))
        self.instrument_btn.setIconSize(QSize(70, 70))
        self.instrument_btn.setMaximumHeight(700)
        self.instrument_btn.setMaximumWidth(950)
        self.instrument_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        self.sendData_btn = QPushButton(flat=True)
        self.sendData_btn.setIcon(QIcon('icons/send-data.png'))
        self.sendData_btn.setIconSize(QSize(70, 70))
        self.sendData_btn.setMaximumHeight(700)
        self.sendData_btn.setMaximumWidth(950)
        self.sendData_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        self.informaintion_btn = QPushButton(flat=True)
        self.informaintion_btn.setIcon(QIcon('icons/info.png'))
        self.informaintion_btn.setIconSize(QSize(70, 70))
        self.informaintion_btn.setMaximumHeight(700)
        self.informaintion_btn.setMaximumWidth(950)
        self.informaintion_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        self.saveSetting_btn = QPushButton(flat=True)
        self.saveSetting_btn.setIcon(QIcon('icons/save-setting.png'))
        self.saveSetting_btn.setIconSize(QSize(70, 70))
        self.saveSetting_btn.setMaximumHeight(700)
        self.saveSetting_btn.setMaximumWidth(950)
        self.saveSetting_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        self.setProfile_btn = QPushButton(flat=True)
        self.setProfile_btn.setIcon(QIcon('icons/profile-setting.png'))
        self.setProfile_btn.setIconSize(QSize(70, 70))
        self.setProfile_btn.setMaximumHeight(700)
        self.setProfile_btn.setMaximumWidth(950)
        self.setProfile_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        self.trigger_btn = QPushButton(flat=True)
        self.trigger_btn.setIcon(QIcon('icons/no-icon.png'))
        self.trigger_btn.setIconSize(QSize(70, 70))
        self.trigger_btn.setMaximumHeight(700)
        self.trigger_btn.setMaximumWidth(950)
        self.trigger_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        self.language_btn = QPushButton(flat=True)
        self.language_btn.setIcon(QIcon('icons/language.png'))
        self.language_btn.setIconSize(QSize(70, 70))
        self.language_btn.setMaximumHeight(700)
        self.language_btn.setMaximumWidth(950)
        self.language_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        main_box = QGridLayout(self)
        main_box.addWidget(self.back_to_main, 0, 28)
        main_box.addWidget(self.instrument_btn, 1, 0, 5, 4)
        main_box.addWidget(self.sendData_btn, 1, 5, 5, 4)
        main_box.addWidget(self.informaintion_btn, 1, 10, 5, 4)
        main_box.addWidget(self.saveSetting_btn, 1, 15, 5, 4)
        main_box.addWidget(self.setProfile_btn, 1, 20, 5, 4)
        main_box.addWidget(self.trigger_btn, 1, 25, 5, 4)
        main_box.addWidget(self.language_btn, 6, 0, 5, 4)
