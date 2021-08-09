import sys
import pyqtgraph as pg
import FinanceDataReader as fdr
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt


# import sip

class Triggers:
    rec_trig = 0# 0 for not selected, 1 for select
    rec_mode = 0# 0 for normal, 1 for ultra

    led_mode = 0# 0 for on, 1 for off

    db_scaling_trig = 0# 0 for not selected, 1 for select
    db_scaling_mode = 0# 0 for auto, 1 for smart, -1 for off

    sound_trig = 0#주파수 0 for not selected, 1 for select

    play_trig = 0# -1 for not working, 0 for not selected, 1 for select
    play_mode = 0# 0 for normal, 1 for 0.5, 2 for 0.25
    time_nv_flag = 0
    time_val = 0


class MeasurementWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.sound_flag = 0
        self.time_nv_flag = 0
        self.time_val = 0

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.rec_btn = QPushButton('',self)
        self.rec_btn.setMinimumHeight(65)
        self.rec_btn.setMaximumWidth(85)
        self.rec_btn.setIcon(QIcon('./icons/rec.png'))
        self.rec_btn.setIconSize(QSize(60, 60))
        self.rec_btn.setStyleSheet("background-color: #55B0BC;")
        self.rec_btn.clicked.connect(self.rec_start_event)

        self.capture_btn = QPushButton('',self)
        self.capture_btn.setMinimumHeight(65)
        self.capture_btn.setMaximumWidth(85)
        self.capture_btn.setIcon(QIcon('./icons/capture.png'))
        self.capture_btn.setIconSize(QSize(60, 60))
        self.capture_btn.setStyleSheet("background-color: #55B0BC;")

        self.time_marker_btn = QPushButton('',self)
        self.time_marker_btn.setMinimumHeight(65)
        self.time_marker_btn.setMaximumWidth(85)
        self.time_marker_btn.setIcon(QIcon('./icons/time-marker.png'))
        self.time_marker_btn.setIconSize(QSize(60, 60))
        self.time_marker_btn.setStyleSheet("background-color: #55B0BC;")

        # color = rgb()
        self.file_open_btn = QPushButton('',self)
        self.file_open_btn.setMinimumHeight(65)
        self.file_open_btn.setMaximumWidth(85)
        self.file_open_btn.setIcon(QIcon('./icons/file-open.png'))
        self.file_open_btn.setIconSize(QSize(60, 60))
        self.file_open_btn.setStyleSheet("background-color: #55B0BC;")
        self.file_open_btn.clicked.connect(self.fileOpen)

        self.file_save_btn = QPushButton('',self)
        self.file_save_btn.setMinimumHeight(65)
        self.file_save_btn.setMaximumWidth(85)
        self.file_save_btn.setIcon(QIcon('./icons/file-save.png'))
        self.file_save_btn.setIconSize(QSize(60, 60))
        self.file_save_btn.setStyleSheet("background-color: #55B0BC;")

        self.led_btn = QPushButton('',self)
        self.led_btn.setMinimumHeight(65)
        self.led_btn.setMaximumWidth(85)
        self.led_btn.setIcon(QIcon('./icons/led.png'))
        self.led_btn.setIconSize(QSize(60, 60))
        self.led_btn.setStyleSheet("background-color: #55B0BC;")
        self.led_btn.clicked.connect(self.led_control)

        self.play_btn = QPushButton('',self)
        self.play_btn.setMinimumHeight(65)
        self.play_btn.setMaximumWidth(85)
        self.play_btn.setIcon(QIcon('./icons/play.png'))
        self.play_btn.setIconSize(QSize(60, 60))
        self.play_btn.setStyleSheet("background-color: #55B0BC;")
        self.play_btn.clicked.connect(self.play_setting_event)

        self.exit_btn = QPushButton('',self)
        self.exit_btn.setMinimumHeight(65)
        self.exit_btn.setMaximumWidth(85)
        self.exit_btn.setIcon(QIcon('./icons/exit.png'))
        self.exit_btn.setIconSize(QSize(60, 60))
        self.exit_btn.setStyleSheet("background-color: #55B0BC;")

        self.video_btn = QPushButton('',self)
        self.video_btn.setMinimumHeight(65)
        self.video_btn.setMaximumWidth(85)
        self.video_btn.setIcon(QIcon('./icons/video.png'))
        self.video_btn.setIconSize(QSize(60, 60))
        self.video_btn.setStyleSheet("background-color: #55B0BC;")

        self.db_scaling_btn = QPushButton('',self)
        self.db_scaling_btn.setMinimumHeight(65)
        self.db_scaling_btn.setMaximumWidth(85)
        self.db_scaling_btn.setIcon(QIcon('./icons/db-scaling.png'))
        self.db_scaling_btn.setIconSize(QSize(60, 60))
        self.db_scaling_btn.setStyleSheet("background-color: #55B0BC;")
        self.db_scaling_btn.clicked.connect(self.db_scaling_event)

        self.time_marker_move_btn = QPushButton('',self)
        self.time_marker_move_btn.setMinimumHeight(65)
        self.time_marker_move_btn.setMaximumWidth(85)
        self.time_marker_move_btn.setIcon(QIcon('./icons/time-marker.png'))
        self.time_marker_move_btn.setIconSize(QSize(60, 60))
        self.time_marker_move_btn.setStyleSheet("background-color: #55B0BC;")

        self.sound_btn = QPushButton('',self)
        self.sound_btn.setMinimumHeight(65)
        self.sound_btn.setMaximumWidth(85)
        self.sound_btn.setIcon(QIcon('./icons/sound.png'))
        self.sound_btn.setIconSize(QSize(60, 60))
        self.sound_btn.setStyleSheet("background-color: #55B0BC;")
        self.sound_btn.clicked.connect(self.sound_control)

        self.time_setting_btn = QPushButton('',self)
        self.time_setting_btn.setMinimumHeight(65)
        self.time_setting_btn.setMaximumWidth(85)
        self.time_setting_btn.setIcon(QIcon('./icons/time-setting.png'))
        self.time_setting_btn.setIconSize(QSize(60, 60))
        self.time_setting_btn.setStyleSheet("background-color: #55B0BC;")

        self.time_navigation_btn = QPushButton('',self)
        self.time_navigation_btn.setMinimumHeight(65)
        self.time_navigation_btn.setMaximumWidth(85)
        self.time_navigation_btn.setIcon(QIcon('./icons/time-navigator.png'))
        self.time_navigation_btn.setIconSize(QSize(60, 60))
        self.time_navigation_btn.setStyleSheet("background-color: #55B0BC;")
        self.time_navigation_btn.clicked.connect(self.time_navigation_event)


        lbl_video = QLabel('Video')
        lbl_video.setMaximumWidth(1000)

        # lbl_graph1 = QLabel('Graph1')
        lbl_graph1 = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        df = fdr.DataReader("005930")
        unix_ts = [x.timestamp() for x in df.index]
        lbl_graph1.plot(x=unix_ts, y=df['Close'])
        lbl_graph1.setMaximumWidth(1000)

        # lbl_graph2 = QLabel('Graph2')
        lbl_graph2 = pg.PlotWidget(title="line chart")
        x = [1, 2, 3]
        y = [4, 5, 6]
        lbl_graph2.plot(x, y)
        lbl_graph2.setMaximumWidth(250)

        lbl_bar1 = QLabel('Bar1')
        lbl_bar1.setMaximumWidth(50)

        lbl_bar2 = QLabel('Bar2')
        lbl_bar2.setMaximumWidth(50)

        lbl_setting = QLabel('')
        lbl_setting.setMaximumWidth(100)

        lbl_video.setStyleSheet("border-style: solid;"
                                "border-width: 1px;")
        lbl_graph1.setStyleSheet("border-style: solid;"
                                 "border-width: 1px;")
        lbl_graph2.setStyleSheet("border-style: solid;"
                                 "border-width: 1px;")
        lbl_bar1.setStyleSheet("border-style: solid;"
                               "border-width: 1px;")
        lbl_bar2.setStyleSheet("border-style: solid;"
                               "border-width: 1px;")
        lbl_setting.setStyleSheet("border-style: solid;"
                                  "border-width: 1px;")

        self.grid.addWidget(self.rec_btn, 0, 0)
        self.grid.addWidget(self.capture_btn, 1, 0)
        self.grid.addWidget(self.time_marker_btn, 2, 0)
        self.grid.addWidget(self.file_open_btn, 3, 0)
        self.grid.addWidget(self.file_save_btn, 4, 0)
        self.grid.addWidget(self.led_btn, 5, 0)
        self.grid.addWidget(self.play_btn, 6, 0)

        self.grid.addWidget(lbl_video, 0, 1, 4, 5)
        self.grid.addWidget(lbl_graph1, 4, 1, 2, 5)
        self.grid.addWidget(lbl_bar1, 0, 6, 4, 1)
        self.grid.addWidget(lbl_bar2, 4, 6, 2, 1)
        self.grid.addWidget(lbl_graph2, 4, 7, 2, 1)
        self.grid.addWidget(lbl_setting, 0, 8, 7, 1)

        self.grid.addWidget(self.exit_btn, 0, 9)
        self.grid.addWidget(self.video_btn, 1, 9)
        self.grid.addWidget(self.db_scaling_btn, 2, 9)
        self.grid.addWidget(self.time_marker_move_btn, 3, 9)
        self.grid.addWidget(self.sound_btn, 4, 9)
        self.grid.addWidget(self.time_setting_btn, 5, 9)
        self.grid.addWidget(self.time_navigation_btn, 6, 9)

    # normal mode측정 설정
    def rec_start_event(self):
        if Triggers.rec_trig == 0:#대기상태라면 위젯 추가
            Triggers.rec_trig += 1
            self.rec_ultra = QPushButton('',self)
            self.rec_ultra.setMinimumHeight(65)
            self.rec_ultra.setMaximumWidth(85)
            self.rec_ultra.setIcon(QIcon('./icons/rec.png'))
            self.rec_ultra.setIconSize(QSize(60, 60))
            self.rec_ultra.setStyleSheet("background-color: #55B0BC;")
            self.rec_ultra.clicked.connect(self.rec_ultra_event)

            self.grid.addWidget(self.rec_ultra, 0, 1)

        elif Triggers.rec_trig > 0: # 모드 선택 상태라면
            self.reformat_btns()
            Triggers.rec_trig = 0
            Triggers.rec_num = 0
# print(Triggers.rec_num, "normal mode")

    # ultra mode측정 설정
    def rec_ultra_event(self):
        if Triggers.rec_trig > 0:
            self.reformat_btns()
            Triggers.rec_trig = 0
            Triggers.rec_num = 1
            # print(Triggers.rec_num, "ultra mode")

    #측정 시작 후 버튼 변경
    def reformat_btns(self):
        self.grid.removeWidget(self.rec_ultra)
        self.grid.removeWidget(self.rec_btn)
        self.grid.removeWidget(self.time_marker_move_btn)
        self.rec_ultra.deleteLater()
        self.rec_ultra = None

        Triggers.play_trig = -1

        self.measurement_distance = QPushButton('',self)
        self.measurement_distance.setMinimumHeight(65)
        self.measurement_distance.setMaximumWidth(85)
        self.measurement_distance.setIcon(QIcon('./icons/measure-distance.png'))
        self.measurement_distance.setIconSize(QSize(60, 60))
        self.measurement_distance.setStyleSheet("background-color: #55B0BC;")
        self.grid.addWidget(self.measurement_distance, 1, 9)

        self.stop_btn = QPushButton('',self)
        self.stop_btn.setMinimumHeight(65)
        self.stop_btn.setMaximumWidth(85)
        self.stop_btn.setIcon(QIcon('./icons/stop.png'))
        self.stop_btn.setIconSize(QSize(60, 60))
        self.stop_btn.setStyleSheet("background-color: #55B0BC;")
        self.grid.addWidget(self.stop_btn, 0, 0)
        self.stop_btn.clicked.connect(self.stop_measure)

        self.frequency_btn = QPushButton('',self)
        self.frequency_btn.setMinimumHeight(65)
        self.frequency_btn.setMaximumWidth(85)
        self.frequency_btn.setIcon(QIcon('./icons/frequency.png'))
        self.frequency_btn.setIconSize(QSize(60, 60))
        self.frequency_btn.setStyleSheet("background-color: #55B0BC;")
        self.grid.addWidget(self.frequency_btn, 3, 9)

        self.file_save_btn.setStyleSheet("background-color: #5E777A")
        self.play_btn.setStyleSheet("background-color: #5E777A")
        self.time_navigation_btn.setStyleSheet("background-color: #5E777A")

    # 측정 종료 후 복귀
    def stop_measure(self):
        self.grid.removeWidget(self.stop_btn)
        self.grid.removeWidget(self.frequency_btn)
        self.grid.removeWidget(self.measurement_distance)
        self.stop_btn.deleteLater()
        self.frequency_btn.deleteLater()
        self.measurement_distance.deleteLater()

        self.grid.addWidget(self.rec_btn, 0, 0)
        self.grid.addWidget(self.time_marker_move_btn, 3, 9)
        self.grid.addWidget(self.video_btn, 1, 9)

        Triggers.rec_trig = 0
        Triggers.rec_mode = 0
        Triggers.play_trig = 0

        self.file_save_btn.setStyleSheet("background-color: #55B0BC")
        self.play_btn.setStyleSheet("background-color: #55B0BC")
        self.time_navigation_btn.setStyleSheet("background-color: #55B0BC")

    #파일 재생 속도 설정
    def play_setting_event(self):
        if Triggers.play_trig == -1:
            return
        elif Triggers.play_trig == 0:
            Triggers.play_trig += 1

            self.play_05 = QPushButton('',self)
            self.play_05.setMinimumHeight(65)
            self.play_05.setMaximumWidth(85)
            self.play_05.setIcon(QIcon('./icons/play.png'))
            self.play_05.setIconSize(QSize(60, 60))
            self.play_05.setStyleSheet("background-color: #55B0BC;")
            self.play_05.clicked.connect(self.play05_setting_event)

            self.play_025 = QPushButton('',self)
            self.play_025.setMinimumHeight(65)
            self.play_025.setMaximumWidth(85)
            self.play_025.setIcon(QIcon('./icons/play.png'))
            self.play_025.setIconSize(QSize(60, 60))
            self.play_025.setStyleSheet("background-color: #55B0BC;")
            self.play_025.clicked.connect(self.play025_setting_event)

            self.grid.addWidget(self.play_05, 6, 1)
            self.grid.addWidget(self.play_025, 6, 2)
        elif Triggers.play_trig > 0:
            self.grid.removeWidget(self.play_025)
            self.grid.removeWidget(self.play_05)
            self.play_025.deleteLater()
            self.play_05.deleteLater()

            Triggers.play_trig = 0
            Triggers.play_mode = 0

    def play05_setting_event(self):
        if Triggers.play_trig > 0:
            self.grid.removeWidget(self.play_025)
            self.grid.removeWidget(self.play_05)
            self.play_025.deleteLater()
            self.play_05.deleteLater()

            Triggers.play_trig = 0
            Triggers.play_mode = 1
            print(Triggers.play_mode, 'play 0.5')

    def play025_setting_event(self):
        if Triggers.play_trig > 0:
            self.grid.removeWidget(self.play_025)
            self.grid.removeWidget(self.play_05)
            self.play_025.deleteLater()
            self.play_05.deleteLater()

            Triggers.play_trig = 0
            Triggers.play_mode = 2
            print(Triggers.play_mode, 'play 0.25')

# led on/off
    def led_control(self):
        if Triggers.led_mode == 0:
            Triggers.led_mode = 1
            self.led_btn.setIcon(QIcon('icons/led.png'))
        else:
            Triggers.led_mode = 0
            self.led_btn.setIcon(QIcon('icons/led-off.png'))

    def db_scaling_event(self):
        if Triggers.db_scaling_trig == 0: # 슬라이더 열기
            Triggers.db_scaling_trig += 1
            self.mode_lbl = QLabel('Auto',self)
            self.db_mode = QComboBox(self)
            self.db_mode.addItem('Auto')
            self.db_mode.addItem('Smart')
            self.db_mode.addItem('Off')
            self.db_mode.activated[str].connect(self.db_mode_change_event)
            self.grid.addWidget(self.db_mode, 0, 8)

            self.dynamic_lbl = QLabel('Dynamic',self)
            self.grid.addWidget(self.dynamic_lbl, 1, 8)

            self.slider = QSlider(Qt.Vertical,self)
            self.slider.setRange(0.5, 50)
            self.slider.setSingleStep(2)
            self.grid.addWidget(self.slider, 3, 8, 4, 1)

        elif Triggers.db_scaling_trig > 0: # 슬라이더 닫기
            Triggers.db_scaling_trig = 0
            self.grid.removeWidget(self.db_mode)
            self.db_mode.deleteLater()
            self.db_mode = None

            self.grid.removeWidget(self.dynamic_lbl)
            self.dynamic_lbl.deleteLater()
            self.dynamic_lbl = None

            self.grid.removeWidget(self.slider)
            self.slider.deleteLater()
            self.slider = None


    def db_mode_change_event(self, text):
        if Triggers.db_scaling_mode < 0:
            self.grid.removeWidget(self.db_mode)
            self.db_mode.deleteLater()
            self.db_mode = None
            self.grid.addWidget(self.db_mode, 0, 8)

            self.mode_lbl.setText(text)
            self.mode_lbl.adjustSize()

        if text == 'Smart':
            Triggers.db_scaling_mode = 1
            self.crest_lbl = QLabel('Crest',self)
            self.grid.addWidget(self.crest_lbl, 2, 8)

        elif text == 'Off':
            Triggers.db_scaling_mode = 2
            self.crest_lbl = QLabel('최고 dB',self)
            self.grid.addWidget(self.crest_lbl, 2, 8)
        else:
            Triggers.db_scaling_mode = 0
            pass

    def sound_control(self):
        if self.sound_flag == 0:  # init or sound off -> sound on
            self.sound_flag = 1  # on
            self.sound_btn.setIcon(QIcon('icons/sound.png'))

            self.no_signal_btn = QPushButton('',self)
            self.no_signal_btn.setMinimumHeight(65)
            self.no_signal_btn.setMaximumWidth(85)
            self.no_signal_btn.setIcon(QIcon('./icons/no-signal.png'))
            self.no_signal_btn.setIconSize(QSize(60, 60))
            self.no_signal_btn.setStyleSheet("background-color: #55B0BC;")
            self.grid.addWidget(self.no_signal_btn, 0, 8)
            self.no_signal_btn.clicked.connect(self.sound_event)

            self.slider = QSlider(Qt.Vertical,self)
            self.slider.setRange(0, 50)
            self.slider.setSingleStep(2)
            self.grid.addWidget(self.slider, 1, 8, 6, 1)

        else: # sound on -> sound off
            self.sound_flag = 0 # off
            self.sound_btn.setIcon(QIcon('icons/sound-off.png'))
            self.grid.removeWidget(self.no_signal_btn)
            self.no_signal_btn.deleteLater()
            self.no_signal_btn = None

            self.grid.removeWidget(self.slider)
            self.slider.deleteLater()
            self.slider = None

    def sound_event(self):
        if Triggers.sound_trig == 0:#전영역 주파수
            Triggers.sound_trig += 1
            self.no_signal_btn.setIcon(QIcon('icons/no-signal.png'))

        elif Triggers.sound_trig > 0:#선택 영역 주파수
            Triggers.sound_trig = 0
            self.no_signal_btn.setIcon(QIcon('icons/signal.png'))

    def time_navigation_event(self):
        if self.time_nv_flag == 0: # init or time_navigation on
            self.time_nv_flag = 1 # on

            self.time_lbl = QLabel('0')
            self.grid.addWidget(self.time_lbl, 0, 8)
            self.time_lbl.setStyleSheet("margin-left: 2em;")

            self.time_up_btn = QPushButton('', self)
            self.time_up_btn.setMinimumHeight(65)
            self.time_up_btn.setMaximumWidth(85)
            self.time_up_btn.setIcon(QIcon('./icons/up-arrow.png'))
            self.time_up_btn.setIconSize(QSize(60, 60))
            self.time_up_btn.setStyleSheet("background-color: #55B0BC;")
            self.grid.addWidget(self.time_up_btn, 1, 8)

            self.slider = QSlider(Qt.Vertical, self)
            self.slider.setRange(0, 50)
            self.slider.setSingleStep(2)
            self.slider.valueChanged.connect(self.slider_value_changed)
            self.slider.setStyleSheet("margin-left: 3.5em; margin-bottom: 30px")
            self.grid.addWidget(self.slider, 2, 8, 4, 2)

            self.time_down_btn = QPushButton('', self)
            self.time_down_btn.setMinimumHeight(65)
            self.time_down_btn.setMaximumWidth(85)
            self.time_down_btn.setIcon(QIcon('./icons/down-arrow.png'))
            self.time_down_btn.setIconSize(QSize(60, 60))
            self.time_down_btn.setStyleSheet("background-color: #55B0BC;")
            self.grid.addWidget(self.time_down_btn, 6, 8)


        else: # time_navigation off
            self.time_nv_flag = 0 # off

            self.grid.removeWidget(self.time_lbl)
            self.time_lbl.deleteLater()
            self.time_lbl = None

            self.grid.removeWidget(self.time_up_btn)
            self.grid.removeWidget(self.time_down_btn)
            self.time_up_btn.deleteLater()
            self.time_down_btn.deleteLater()
            self.time_up_btn = None
            self.time_down_btn = None

            self.grid.removeWidget(self.slider)
            self.slider.deleteLater()
            self.slider = None

    def slider_value_changed(self):
        self.time_val = self.slider.value()
        self.time_lbl.setText(str(self.time_val))




        # if pre_mode == 'None':
        #     pass
        #
        # elif pre_mode == 'Smart':
        #     self.grid.removeWidget(self.crest_lbl)
        #     self.crest_lbl.deleteLater()
        #     self.crest_lbl = None
        #
        # elif pre_mode == 'Off':
        #     self.grid.removeWidget(self.high_db_lbl)
        #     self.high_db_lbl.deleteLater()
        #     self.high_db_lbl = None

    # file open
    def fileOpen(self):
            fileName = QFileDialog.getOpenFileName(self,self.tr("Open Data Files"), './',self.tr(
                "Data Files (*.csv *.xls *.xlsx *.tdms);; Images (*.png *.xpm *.jpg *.gif);; All Files(*.*)"))
            print("load file : ", fileName[0])
            return fileName


class MeasurementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction('Exit',self)
        exitAction.setShortcut('Ctrl+Q')#단축키
        exitAction.setStatusTip('Exit application')#상태팁
        exitAction.triggered.connect(qApp.quit)#어플리케이션 종료

        self.statusBar()

        menubar =self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        filemenu = menubar.addMenu('&Edit')
        filemenu.addAction(exitAction)

        wg = MeasurementWidget()
        self.setCentralWidget(wg)

        self.setWindowTitle('Sound Cam')
        self.resize(720, 480)
        self.show()

