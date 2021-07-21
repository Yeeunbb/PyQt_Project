import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mainSetting.SettingDetails import *

# setting page 1
class SettingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setting_stack = QStackedWidget(self)
        # SettingBtn().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SoundCam')
        self.resize(720, 480)

        self.setting_btns = SettingBtn()
        self.instrumentClass = Instrument()

        widget_layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setting_stack.addWidget(self.setting_btns)
        self.setting_stack.addWidget(self.instrumentClass)
        widget_layout.addWidget(self.setting_stack)
        self.setLayout(widget_layout)

        self.setting_btns.instrument_btn.clicked.connect(self.instrument)

    def instrument(self):
        self.setting_stack.setCurrentWidget(self.instrumentClass)


class SettingBtn(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setting Page")
        self.resize(720, 480)
        self.theme_flag = 0  # 0 for light, 1 for dark

        # main 화면으로 돌아가기
        self.back_to_main = QPushButton(self)
        self.back_to_main.setIcon(QIcon('icons/go-back.jpg'))
        self.back_to_main.setIconSize(QSize(40, 40))
        self.back_to_main.setMaximumHeight(150)
        self.back_to_main.setMaximumWidth(150)
        self.back_to_main.setStyleSheet(
            "QPushButton { color: black; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #D9D9D9; }"
        )

        # 카메라 해상도 및 beamforming 프레임 속도 설정
        self.instrument_btn = QPushButton(flat=True)
        self.instrument_btn.setIcon(QIcon('icons/instrument-panel.png'))
        self.instrument_btn.setIconSize(QSize(70, 70))
        self.instrument_btn.setMaximumHeight(150)
        self.instrument_btn.setMaximumWidth(150)
        self.instrument_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 데이터 전송
        self.sendData_btn = QPushButton(flat=True)
        self.sendData_btn.setIcon(QIcon('icons/send-data.png'))
        self.sendData_btn.setIconSize(QSize(70, 70))
        self.sendData_btn.setMaximumHeight(150)
        self.sendData_btn.setMaximumWidth(150)
        self.sendData_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 정보 및 업데이트
        self.informaintion_btn = QPushButton(flat=True)
        self.informaintion_btn.setIcon(QIcon('icons/info.png'))
        self.informaintion_btn.setIconSize(QSize(70, 70))
        self.informaintion_btn.setMaximumHeight(150)
        self.informaintion_btn.setMaximumWidth(150)
        self.informaintion_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 데이터 저장 경로 설정
        self.saveSetting_btn = QPushButton(flat=True)
        self.saveSetting_btn.setIcon(QIcon('icons/save-setting.png'))
        self.saveSetting_btn.setIconSize(QSize(70, 70))
        self.saveSetting_btn.setMaximumHeight(150)
        self.saveSetting_btn.setMaximumWidth(150)
        self.saveSetting_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 프로필 설정
        self.setProfile_btn = QPushButton(flat=True)
        self.setProfile_btn.setIcon(QIcon('icons/profile-setting.png'))
        self.setProfile_btn.setIconSize(QSize(70, 70))
        self.setProfile_btn.setMaximumHeight(150)
        self.setProfile_btn.setMaximumWidth(150)
        self.setProfile_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 트리거 설정
        self.trigger_btn = QPushButton(flat=True)
        self.trigger_btn.setIcon(QIcon('icons/no-icon.png'))
        self.trigger_btn.setIconSize(QSize(70, 70))
        self.trigger_btn.setMaximumHeight(150)
        self.trigger_btn.setMaximumWidth(150)
        self.trigger_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 트리거 설정
        self.machine_btn = QPushButton(flat=True)
        self.machine_btn.setIcon(QIcon('icons/machinebtn.png'))
        self.machine_btn.setIconSize(QSize(70, 70))
        self.machine_btn.setMaximumHeight(150)
        self.machine_btn.setMaximumWidth(150)
        self.machine_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 언어 선택 및 단말기&키보드 설정
        self.language_btn = QPushButton(flat=True)
        self.language_btn.setIcon(QIcon('icons/language.png'))
        self.language_btn.setIconSize(QSize(70, 70))
        self.language_btn.setMaximumHeight(150)
        self.language_btn.setMaximumWidth(150)
        self.language_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 화면 테마 설정
        self.theme_btn = QPushButton(flat=True)
        self.theme_btn.setIcon(QIcon('icons/darkmode.png'))
        self.theme_btn.setIconSize(QSize(70, 70))
        self.theme_btn.setMaximumHeight(150)
        self.theme_btn.setMaximumWidth(150)
        self.theme_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )
        self.theme_btn.clicked.connect(self.changeMode)

        # LTM 설정
        self.ltm_btn = QPushButton(flat=True)
        self.ltm_btn.setIcon(QIcon('icons/no-icon.png'))
        self.ltm_btn.setIconSize(QSize(70, 70))
        self.ltm_btn.setMaximumHeight(150)
        self.ltm_btn.setMaximumWidth(150)
        self.ltm_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 비밀번호 설정
        self.pw_btn = QPushButton(flat=True)
        self.pw_btn.setIcon(QIcon('icons/password.png'))
        self.pw_btn.setIconSize(QSize(70, 70))
        self.pw_btn.setMaximumHeight(150)
        self.pw_btn.setMaximumWidth(150)
        self.pw_btn.setStyleSheet(
            "QPushButton { color: black; background-color: #519AA4; border-radius: 5px;}"
            "QPushButton:pressed { background-color: #305F65; }"
        )

        # 그리드 적용
        main_box = QGridLayout(self)
        main_box.addWidget(self.back_to_main, 0, 27)
        main_box.addWidget(self.instrument_btn, 1, 0, 5, 4)
        main_box.addWidget(self.sendData_btn, 1, 5, 5, 4)
        main_box.addWidget(self.informaintion_btn, 1, 10, 5, 4)
        main_box.addWidget(self.saveSetting_btn, 1, 15, 5, 4)
        main_box.addWidget(self.setProfile_btn, 1, 20, 5, 4)
        main_box.addWidget(self.trigger_btn, 1, 25, 5, 4)
        main_box.addWidget(self.machine_btn, 6, 0, 5, 4)
        main_box.addWidget(self.language_btn, 6, 5, 5, 4)
        main_box.addWidget(self.theme_btn, 6, 10, 5, 4)
        main_box.addWidget(self.ltm_btn, 6, 15, 5, 4)
        main_box.addWidget(self.pw_btn, 6, 20, 5, 4)

    def changeMode(self):
        if self.theme_flag == 0:
            self.theme_flag = 1
            self.theme_btn.setIcon(QIcon('icons/lightmode.png'))
        else:
            self.theme_flag = 0
            self.theme_btn.setIcon(QIcon('icons/darkmode.png'))