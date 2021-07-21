import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

from mainSetting.Setting import *
from measurement.measurement import *

# main ui control
class SoundCam(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SoundCam')
        self.resize(720, 480)

        self.main_window = MainWindow()
        self.setting_page = SettingPage()
        self.setting_btns = SettingBtn()
        self.measurement_page = MeasurementWidget()
        # self.measurement_page = None


        widget_layout = QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.addWidget(self.setting_page)
        self.stacked_widget.addWidget(self.measurement_page)
        widget_layout.addWidget(self.stacked_widget)
        self.setLayout(widget_layout)

        self.main_window.setting_btn.clicked.connect(self.go_setting)
        self.setting_btns.back_to_main.clicked.connect(self.back_to_main)
        self.main_window.start_btn.clicked.connect(self.start)
        self.measurement_page.exit_btn.clicked.connect(self.back_to_main)

    def go_setting(self):
        self.stacked_widget.setCurrentWidget(self.setting_page)

    def back_to_main(self):
        self.stacked_widget.setCurrentWidget(self.main_window)

    def start(self):
        self.stacked_widget.setCurrentWidget(self.measurement_page)

# main page
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('SoundCam')
        self.resize(720, 480)

        # 측정 시작 버튼
        self.start_btn = QPushButton(flat=True)
        self.start_btn.setIcon(QIcon('icons/broadcast.png'))
        self.start_btn.setIconSize(QSize(200, 200))
        self.start_btn.setMaximumHeight(700)
        self.start_btn.setMaximumWidth(950)
        self.start_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 설정 버튼
        self.setting_btn = QPushButton(flat=True)
        self.setting_btn.setIcon(QIcon('icons/setting.png'))
        self.setting_btn.setIconSize(QSize(100, 100))
        self.setting_btn.setMaximumHeight(300)
        self.setting_btn.setMaximumWidth(300)
        self.setting_btn.setStyleSheet(
            'QPushButton { color: black; background-color: #55B0BC; border-radius: 5px;}'
            'QPushButton:pressed { background-color: #305F65 }'
        )

        # 전원 on/off 버튼
        self.power_btn = QPushButton(flat=True)
        self.power_btn.setIcon(QIcon('icons/power.png'))
        self.power_btn.setIconSize(QSize(100, 100))
        self.power_btn.setMaximumHeight(300)
        self.power_btn.setMaximumWidth(300)
        self.power_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #55B0BC; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65 }"
        )
        self.power_btn.clicked.connect(QCoreApplication.instance().quit)

        # 정보창 버튼
        self.info_btn = QPushButton(flat=True)
        self.info_btn.setIcon(QIcon('icons/info.png'))
        self.info_btn.setIconSize(QSize(100, 100))
        self.info_btn.setMaximumHeight(300)
        self.info_btn.setMaximumWidth(300)
        self.info_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #55B0BC; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65 }"
        )

        # 프로필 버튼
        self.profile_btn = QPushButton(flat=True)
        self.profile_btn.setIcon(QIcon('icons/profiles.png'))
        self.profile_btn.setIconSize(QSize(100, 100))
        self.profile_btn.setMaximumHeight(300)
        self.profile_btn.setMaximumWidth(300)
        self.profile_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #55B0BC; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65 }"
        )

        # 파일 불러오기 버튼
        self.file_btn = QPushButton(flat=True)
        self.file_btn.setIcon(QIcon('icons/file.png'))
        self.file_btn.setIconSize(QSize(100, 100))
        self.file_btn.setMaximumHeight(300)
        self.file_btn.setMaximumWidth(700)
        self.file_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #55B0BC; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65 }"
        )

        # 그리드 추가
        main_box = QGridLayout(self)

        main_box.addWidget(self.start_btn, 0, 0, 3, 2)
        main_box.addWidget(self.setting_btn, 0, 2, 1, 1)
        main_box.addWidget(self.power_btn, 0, 3, 1, 1)
        main_box.addWidget(self.info_btn, 1, 2, 1, 1)
        main_box.addWidget(self.profile_btn, 1, 3, 1, 1)
        main_box.addWidget(self.file_btn, 2, 2, 1, 2)


# run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SoundCam()
    ex.show()
    sys.exit(app.exec_())
