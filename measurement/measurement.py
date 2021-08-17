import sys
import pyqtgraph as pg
import FinanceDataReader as fdr
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from qtrangeslider import QRangeSlider
import measurement.screenshotclass as ssc


class Triggers:
    rec_trig = 0  # 0 for not selected, 1 for select
    rec_mode = 0  # 0 for normal, 1 for ultra

    led_mode = 0  # 0 for on, 1 for off

    measurement_trig = 0  # 0 for not selected,1 for select

    db_scaling_trig = 0  # 0 for not selected, 1 for select
    db_scaling_mode = 0  # 0 for auto, 1 for smart, -1 for off

    sound_trig = 0  # 주파수 0 for not selected, 1 for select

    play_trig = 0  # -1 for not working, 0 for not selected, 1 for select
    play_mode = 0  # 0 for normal, 1 for 0.5, 2 for 0.25

    time_nv_flag = 0  # 0 for not selected, 1 for select
    time_val = 0  # time navigation slider value

    time_st_flag = 0  # 0 for not selected, 1 for select
    video_flag = 0


class MeasurementWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.measure_set = 0
        self.db_set = 0
        self.sound_flag = 0
        self.time_nv_flag = 0
        self.time_val = 0
        self.time_st_flag = 0
        self.video_flag = 0
        self.frequency_flag = 0
        self.recur_flag = 0
        self.max_freq_set = 30;
        self.min_freq_set = 0

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.rec_btn = QPushButton('', self)
        self.rec_btn.setMinimumHeight(65)
        self.rec_btn.setMaximumWidth(85)
        self.rec_btn.setIcon(QIcon('./icons/rec.png'))
        self.rec_btn.setIconSize(QSize(60, 60))
        self.rec_btn.setStyleSheet("background-color: #55B0BC;")
        self.rec_btn.clicked.connect(self.rec_start_event)

        self.capture_btn = QPushButton('', self)
        self.capture_btn.setMinimumHeight(65)
        self.capture_btn.setMaximumWidth(85)
        self.capture_btn.setIcon(QIcon('./icons/capture.png'))
        self.capture_btn.setIconSize(QSize(60, 60))
        self.capture_btn.setStyleSheet("background-color: #55B0BC;")
        self.capture_btn.clicked.connect(self.capture_event)

        self.time_marker_btn = QPushButton('', self)
        self.time_marker_btn.setMinimumHeight(65)
        self.time_marker_btn.setMaximumWidth(85)
        self.time_marker_btn.setIcon(QIcon('./icons/time-marker.png'))
        self.time_marker_btn.setIconSize(QSize(60, 60))
        self.time_marker_btn.setStyleSheet("background-color: #55B0BC;")

        # color = rgb()
        self.file_open_btn = QPushButton('', self)
        self.file_open_btn.setMinimumHeight(65)
        self.file_open_btn.setMaximumWidth(85)
        self.file_open_btn.setIcon(QIcon('./icons/file-open.png'))
        self.file_open_btn.setIconSize(QSize(60, 60))
        self.file_open_btn.setStyleSheet("background-color: #55B0BC;")
        self.file_open_btn.clicked.connect(self.fileOpen)

        self.file_save_btn = QPushButton('', self)
        self.file_save_btn.setMinimumHeight(65)
        self.file_save_btn.setMaximumWidth(85)
        self.file_save_btn.setIcon(QIcon('./icons/file-save.png'))
        self.file_save_btn.setIconSize(QSize(60, 60))
        self.file_save_btn.setStyleSheet("background-color: #55B0BC;")

        self.led_btn = QPushButton('', self)
        self.led_btn.setMinimumHeight(65)
        self.led_btn.setMaximumWidth(85)
        self.led_btn.setIcon(QIcon('./icons/led.png'))
        self.led_btn.setIconSize(QSize(60, 60))
        self.led_btn.setStyleSheet("background-color: #55B0BC;")
        self.led_btn.clicked.connect(self.led_control)

        self.play_btn = QPushButton('', self)
        self.play_btn.setMinimumHeight(65)
        self.play_btn.setMaximumWidth(85)
        self.play_btn.setIcon(QIcon('./icons/play.png'))
        self.play_btn.setIconSize(QSize(60, 60))
        self.play_btn.setStyleSheet("background-color: #55B0BC;")
        self.play_btn.clicked.connect(self.play_setting_event)

        self.exit_btn = QPushButton('', self)
        self.exit_btn.setMinimumHeight(65)
        self.exit_btn.setMaximumWidth(85)
        self.exit_btn.setIcon(QIcon('./icons/exit.png'))
        self.exit_btn.setIconSize(QSize(60, 60))
        self.exit_btn.setStyleSheet("background-color: #55B0BC;")

        self.video_btn = QPushButton('', self)
        self.video_btn.setMinimumHeight(65)
        self.video_btn.setMaximumWidth(85)
        self.video_btn.setIcon(QIcon('./icons/video.png'))
        self.video_btn.setIconSize(QSize(60, 60))
        self.video_btn.setStyleSheet("background-color: #55B0BC;")
        self.video_btn.clicked.connect(self.video_event)

        self.db_scaling_btn = QPushButton('', self)
        self.db_scaling_btn.setMinimumHeight(65)
        self.db_scaling_btn.setMaximumWidth(85)
        self.db_scaling_btn.setIcon(QIcon('./icons/db-scaling.png'))
        self.db_scaling_btn.setIconSize(QSize(60, 60))
        self.db_scaling_btn.setStyleSheet("background-color: #55B0BC;")
        self.db_scaling_btn.clicked.connect(self.db_scaling_event)

        self.time_marker_move_btn = QPushButton('', self)
        self.time_marker_move_btn.setMinimumHeight(65)
        self.time_marker_move_btn.setMaximumWidth(85)
        self.time_marker_move_btn.setIcon(QIcon('./icons/time-marker.png'))
        self.time_marker_move_btn.setIconSize(QSize(60, 60))
        self.time_marker_move_btn.setStyleSheet("background-color: #55B0BC;")

        self.sound_btn = QPushButton('', self)
        self.sound_btn.setMinimumHeight(65)
        self.sound_btn.setMaximumWidth(85)
        self.sound_btn.setIcon(QIcon('./icons/sound.png'))
        self.sound_btn.setIconSize(QSize(60, 60))
        self.sound_btn.setStyleSheet("background-color: #55B0BC;")
        self.sound_btn.clicked.connect(self.sound_control)

        self.time_setting_btn = QPushButton('', self)
        self.time_setting_btn.setMinimumHeight(65)
        self.time_setting_btn.setMaximumWidth(85)
        self.time_setting_btn.setIcon(QIcon('./icons/time-setting.png'))
        self.time_setting_btn.setIconSize(QSize(60, 60))
        self.time_setting_btn.setStyleSheet("background-color: #55B0BC;")
        self.time_setting_btn.clicked.connect(self.time_setting_event)

        self.time_navigation_btn = QPushButton('', self)
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

    # screenshot event
    def capture_event(self):
        self.screenshot = ssc.Screenshot()
        self.screenshot.show()
        self.screenshot.close()

    # normal mode 측정 설정
    def rec_start_event(self):
        if Triggers.rec_trig == 0:  # 대기상태라면 위젯 추가
            Triggers.rec_trig += 1
            self.rec_ultra = QPushButton('', self)
            self.rec_ultra.setMinimumHeight(65)
            self.rec_ultra.setMaximumWidth(85)
            self.rec_ultra.setIcon(QIcon('./icons/rec.png'))
            self.rec_ultra.setIconSize(QSize(60, 60))
            self.rec_ultra.setStyleSheet("background-color: #55B0BC;")
            self.rec_ultra.clicked.connect(self.rec_ultra_event)

            self.grid.addWidget(self.rec_ultra, 0, 1)

        elif Triggers.rec_trig > 0:  # 모드 선택 상태라면
            self.reformat_btns()
            Triggers.rec_trig = 0
            Triggers.rec_num = 0

    # print(Triggers.rec_num, "normal mode")

    # ultra mode 측정 설정
    def rec_ultra_event(self):
        if Triggers.rec_trig > 0:
            self.reformat_btns()
            Triggers.rec_trig = 0
            Triggers.rec_num = 1
            # print(Triggers.rec_num, "ultra mode")

    # 측정 시작 후 버튼 변경
    def reformat_btns(self):
        self.grid.removeWidget(self.rec_ultra)
        self.grid.removeWidget(self.rec_btn)
        self.grid.removeWidget(self.time_marker_move_btn)
        self.rec_ultra.deleteLater()

        self.rec_btn.deleteLater()
        self.time_marker_move_btn.deleteLater()
        self.rec_ultra = None

        Triggers.play_trig = -1

        self.measurement_distance = QPushButton('', self)
        self.measurement_distance.setMinimumHeight(65)
        self.measurement_distance.setMaximumWidth(85)
        self.measurement_distance.setIcon(QIcon('./icons/measure-distance.png'))
        self.measurement_distance.setIconSize(QSize(60, 60))
        self.measurement_distance.setStyleSheet("background-color: #55B0BC;")
        self.grid.addWidget(self.measurement_distance, 1, 9)
        self.measurement_distance.clicked.connect(self.measurement_event)

        self.stop_btn = QPushButton('', self)
        self.stop_btn.setMinimumHeight(65)
        self.stop_btn.setMaximumWidth(85)
        self.stop_btn.setIcon(QIcon('./icons/stop.png'))
        self.stop_btn.setIconSize(QSize(60, 60))
        self.stop_btn.setStyleSheet("background-color: #55B0BC;")
        self.grid.addWidget(self.stop_btn, 0, 0)
        self.stop_btn.clicked.connect(self.stop_measure)

        self.frequency_btn = QPushButton('', self)
        self.frequency_btn.setMinimumHeight(65)
        self.frequency_btn.setMaximumWidth(85)
        self.frequency_btn.setIcon(QIcon('./icons/frequency.png'))
        self.frequency_btn.setIconSize(QSize(60, 60))
        self.frequency_btn.setStyleSheet("background-color: #55B0BC;")
        self.grid.addWidget(self.frequency_btn, 3, 9)
        self.frequency_btn.clicked.connect(self.frequency_event)

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

        # self.rec_btn = self.rec_wait
        # self.time_marker_move_btn = self.time_rec

        self.rec_btn = QPushButton('', self)
        self.rec_btn.setMinimumHeight(65)
        self.rec_btn.setMaximumWidth(85)
        self.rec_btn.setIcon(QIcon('./icons/rec.png'))
        self.rec_btn.setIconSize(QSize(60, 60))
        self.rec_btn.setStyleSheet("background-color: #55B0BC;")
        self.rec_btn.clicked.connect(self.rec_start_event)

        self.time_marker_move_btn = QPushButton('', self)
        self.time_marker_move_btn.setMinimumHeight(65)
        self.time_marker_move_btn.setMaximumWidth(85)
        self.time_marker_move_btn.setIcon(QIcon('./icons/time-marker.png'))
        self.time_marker_move_btn.setIconSize(QSize(60, 60))
        self.time_marker_move_btn.setStyleSheet("background-color: #55B0BC;")

        self.grid.addWidget(self.rec_btn, 0, 0)
        self.grid.addWidget(self.time_marker_move_btn, 3, 9)
        self.grid.addWidget(self.video_btn, 1, 9)

        Triggers.rec_trig = 0
        Triggers.rec_mode = 0
        Triggers.play_trig = 0

        self.file_save_btn.setStyleSheet("background-color: #55B0BC")
        self.play_btn.setStyleSheet("background-color: #55B0BC")
        self.time_navigation_btn.setStyleSheet("background-color: #55B0BC")

    # 파일 재생 속도 설정
    def play_setting_event(self):
        if Triggers.play_trig == -1:
            return
        elif Triggers.play_trig == 0:
            Triggers.play_trig += 1

            self.play_05 = QPushButton('', self)
            self.play_05.setMinimumHeight(65)
            self.play_05.setMaximumWidth(85)
            self.play_05.setIcon(QIcon('./icons/play.png'))
            self.play_05.setIconSize(QSize(60, 60))
            self.play_05.setStyleSheet("background-color: #55B0BC;")
            self.play_05.clicked.connect(self.play05_setting_event)

            self.play_025 = QPushButton('', self)
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

    def video_event(self):
        if self.video_flag == 0:
            self.video_flag = 1  # on

            self.video_sp_btn = QPushButton('', self)  # video start point setting button
            self.video_sp_btn.setMinimumHeight(65)
            self.video_sp_btn.setMaximumWidth(85)
            self.video_sp_btn.setIcon(QIcon('./icons/video-editing.png'))
            self.video_sp_btn.setIconSize(QSize(60, 60))
            self.video_sp_btn.setStyleSheet("background-color: #55B0BC;")
            self.grid.addWidget(self.video_sp_btn, 1, 8)

            self.video_ep_btn = QPushButton('', self)  # video end point setting button
            self.video_ep_btn.setMinimumHeight(65)
            self.video_ep_btn.setMaximumWidth(85)
            self.video_ep_btn.setIcon(QIcon('./icons/video-editing.png'))
            self.video_ep_btn.setIconSize(QSize(60, 60))
            self.video_ep_btn.setStyleSheet("background-color: #55B0BC;")
            self.grid.addWidget(self.video_ep_btn, 2, 8)

            self.video_rs_btn = QPushButton('', self)  # video remove setting button
            self.video_rs_btn.setMinimumHeight(65)
            self.video_rs_btn.setMaximumWidth(85)
            self.video_rs_btn.setIcon(QIcon('./icons/video-editing.png'))
            self.video_rs_btn.setIconSize(QSize(60, 60))
            self.video_rs_btn.setStyleSheet("background-color: #55B0BC;")
            self.grid.addWidget(self.video_rs_btn, 3, 8)

            self.video_conv_btn = QPushButton('', self)  # video conversion button
            self.video_conv_btn.setMinimumHeight(65)
            self.video_conv_btn.setMaximumWidth(85)
            self.video_conv_btn.setIcon(QIcon('./icons/video_conversion.png'))
            self.video_conv_btn.setIconSize(QSize(60, 60))
            self.video_conv_btn.setStyleSheet("background-color: #55B0BC;")
            self.grid.addWidget(self.video_conv_btn, 4, 8)
        else:
            self.video_flag = 0  # off

            self.grid.removeWidget(self.video_sp_btn)
            self.video_sp_btn.deleteLater()
            self.video_sp_btn = None

            self.grid.removeWidget(self.video_ep_btn)
            self.video_ep_btn.deleteLater()
            self.video_ep_btn = None

            self.grid.removeWidget(self.video_rs_btn)
            self.video_rs_btn.deleteLater()
            self.video_rs_btn = None

            self.grid.removeWidget(self.video_conv_btn)
            self.video_conv_btn.deleteLater()
            self.video_conv_btn = None

    def measurement_event(self):
        if Triggers.measurement_trig == 0:  # 슬라이더 열기
            Triggers.measurement_trig += 1
            self.measure_lbl = QLabel('측정거리\n' + str(self.measure_set) + 'cm', self)
            self.grid.addWidget(self.measure_lbl, 0, 8)
            self.measure_lbl.setAlignment(Qt.AlignCenter)

            self.measure_slider = QSlider(Qt.Vertical, self)
            self.measure_slider.setRange(0, 350)
            self.measure_slider.setSingleStep(2)
            self.measure_slider.setStyleSheet("margin-left: 3.5em; margin-bottom: 30px")
            self.grid.addWidget(self.measure_slider, 2, 8, 5, 1)
            self.measure_slider.valueChanged.connect(self.measure_slider_value_changed)

        elif Triggers.measurement_trig > 0:  # 슬라이더 닫기
            Triggers.measurement_trig = 0
            self.grid.removeWidget(self.measure_lbl)
            self.measure_lbl.deleteLater()
            self.measure_lbl = None

            self.grid.removeWidget(self.measure_slider)
            self.measure_slider.deleteLater()
            self.measure_slider = None

    def measure_slider_value_changed(self):
        self.measure_set = self.measure_slider.value()
        self.measure_lbl.setText('측정거리\n' + str(self.measure_set) + 'cm')


    def db_scaling_event(self):
        if Triggers.db_scaling_trig == 0:  # 슬라이더 열기
            Triggers.db_scaling_trig += 1
            self.db_set = 0
            self.db_scaling_mode = 0 # Auto
            self.auto_mode = QPushButton('Auto',self)
            self.grid.addWidget(self.auto_mode, 0, 8)
            self.auto_mode.clicked.connect(self.db_mode_change_smart)

            self.dynamic_lbl = QLabel('Dynamic',self)
            self.grid.addWidget(self.dynamic_lbl, 1, 8)
            self.dynamic_lbl.setAlignment(Qt.AlignCenter)

            self.slider = QSlider(Qt.Vertical,self)
            self.slider.setRange(0.5, 50)
            self.slider.setSingleStep(2)
            self.grid.addWidget(self.slider, 3, 8, 4, 1)

        elif Triggers.db_scaling_trig > 0:  # 슬라이더 닫기
            Triggers.db_scaling_trig = 0
            self.grid.removeWidget(self.auto_mode)
            self.auto_mode.deleteLater()
            self.auto_mode = None

            self.grid.removeWidget(self.dynamic_lbl)
            self.dynamic_lbl.deleteLater()
            self.dynamic_lbl = None

            self.grid.removeWidget(self.db_slider)
            self.db_slider.deleteLater()
            self.db_slider = None

    def db_mode_change_smart(self):
        self.db_scaling_mode += 1  # Smart
        self.grid.removeWidget(self.auto_mode)
        self.auto_mode.deleteLater()
        self.auto_mode = None

        self.grid.removeWidget(self.dynamic_lbl)
        self.dynamic_lbl.deleteLater()
        self.dynamic_lbl = None

        self.smart_mode = QPushButton('Smart', self)
        self.grid.addWidget(self.smart_mode, 0, 8)
        self.smart_mode.clicked.connect(self.db_mode_change_off)

        self.crest_lbl = QLabel('Crest\n' + str(self.db_set), self)
        self.grid.addWidget(self.crest_lbl, 1, 8)
        self.crest_lbl.setAlignment(Qt.AlignCenter)

    def db_mode_change_off(self):
        self.db_scaling_mode += 1  # Off
        self.grid.removeWidget(self.smart_mode)
        self.smart_mode.deleteLater()
        self.smart_mode = None

        self.grid.removeWidget(self.crest_lbl)
        self.crest_lbl.deleteLater()
        self.crest_lbl = None

        self.off_mode = QPushButton('Off', self)
        self.grid.addWidget(self.off_mode, 0, 8)
        self.off_mode.clicked.connect(self.db_mode_change_exit)

        self.most_db_lbl = QLabel('최고 dB\n' + str(self.db_set), self)
        self.grid.addWidget(self.most_db_lbl, 1, 8)
        self.most_db_lbl.setAlignment(Qt.AlignCenter)

    def db_mode_change_exit(self):
        Triggers.db_scaling_trig = 0
        self.grid.removeWidget(self.off_mode)
        self.off_mode.deleteLater()
        self.off_mode = None

        self.grid.removeWidget(self.most_db_lbl)
        self.most_db_lbl.deleteLater()
        self.most_db_lbl = None

        self.grid.removeWidget(self.db_slider)
        self.db_slider.deleteLater()
        self.db_slider = None

    def db_slider_value_changed(self):
        self.db_set = 0
        self.db_set = self.db_slider.value()
        if self.db_scaling_mode == 0:
            self.dynamic_lbl.setText('Dynamic\n' + str(self.db_set))
        elif self.db_scaling_mode == 1:
            self.crest_lbl.setText('Crest\n' + str(self.db_set))
        elif self.db_scaling_mode == 2:
            self.most_db_lbl.setText('최고 dB\n' + str(self.db_set))

    def frequency_event(self):

        if self.frequency_flag == 0:  # init or recur
            self.frequency_flag = 1  # on

            if self.recur_flag == 1:
                self.grid.removeWidget(self.frequency_mode)
                self.frequency_mode.deleteLater()
                self.frequency_mode = None
                self.grid.removeWidget(self.octave_lbl)
                self.octave_lbl.deleteLater()
                self.octave_lbl = None

            self.frequency_mode = QPushButton("사용자지정")
            self.grid.addWidget(self.frequency_mode, 0, 8)
            self.frequency_mode.clicked.connect(self.frequency_octave)

            self.max_freq_lbl = QLabel('최대 Freq \n' + str(self.max_freq_set), self)
            self.grid.addWidget(self.max_freq_lbl, 1, 8)
            self.max_freq_lbl.setAlignment(Qt.AlignCenter)

            self.min_freq_lbl = QLabel('최소 Freq \n' + str(self.min_freq_set), self)
            self.grid.addWidget(self.min_freq_lbl, 2, 8)
            self.min_freq_lbl.setAlignment(Qt.AlignCenter)

            self.frequency_slider = QRangeSlider()
            self.frequency_slider.setRange(0, 30)
            self.frequency_slider.setSingleStep(2)
            self.frequency_slider.valueChanged.connect(self.frequency_slider_value_changed)
            self.frequency_slider.setStyleSheet("margin-left: 5em; ")
            self.grid.addWidget(self.frequency_slider, 3, 8, 5, 2)

        else:  #
            self.frequency_flag = 0  # off
            self.recur_flag = 0;

            text = self.frequency_mode.text()
            self.grid.removeWidget(self.frequency_mode)
            self.frequency_mode.deleteLater()
            self.frequency_mode = None

            if (text == '사용자지정'):
                self.grid.removeWidget(self.max_freq_lbl)
                self.max_freq_lbl.deleteLater()
                self.max_freq_lbl = None

                self.grid.removeWidget(self.min_freq_lbl)
                self.min_freq_lbl.deleteLater()
                self.min_freq_lbl = None

                self.grid.removeWidget(self.frequency_slider)
                self.frequency_slider.deleteLater()
                self.frequency_slider = None
            else:
                self.grid.removeWidget(self.octave_lbl)
                self.octave_lbl.deleteLater()
                self.octave_lbl = None

    def frequency_octave(self):
        self.grid.removeWidget(self.frequency_mode)
        self.frequency_mode.deleteLater()
        self.frequency_mode = None

        self.grid.removeWidget(self.max_freq_lbl)
        self.max_freq_lbl.deleteLater()
        self.max_freq_lbl = None

        self.grid.removeWidget(self.min_freq_lbl)
        self.min_freq_lbl.deleteLater()
        self.min_freq_lbl = None

        self.grid.removeWidget(self.frequency_slider)
        self.frequency_slider.deleteLater()
        self.frequency_slider = None

        self.frequency_mode = QPushButton("Octave")
        self.grid.addWidget(self.frequency_mode, 0, 8)
        self.frequency_mode.clicked.connect(self.frequency_3rd_octave)

        self.octave_lbl = QComboBox(self)
        self.octave_lbl.addItem('250Hz')
        self.octave_lbl.addItem('500Hz')
        self.octave_lbl.addItem('1000Hz')
        self.octave_lbl.addItem('2000Hz')
        self.octave_lbl.addItem('4000Hz')
        self.octave_lbl.addItem('8000Hz')
        self.octave_lbl.addItem('16000Hz')
        self.grid.addWidget(self.octave_lbl, 1, 8)

    def frequency_3rd_octave(self):
        self.grid.removeWidget(self.frequency_mode)
        self.frequency_mode.deleteLater()
        self.frequency_mode = None

        self.grid.removeWidget(self.octave_lbl)
        self.octave_lbl.deleteLater()
        self.octave_lbl = None

        self.recur_flag = 1

        self.frequency_mode = QPushButton("3rd Oct")
        self.grid.addWidget(self.frequency_mode, 0, 8)
        self.frequency_mode.clicked.connect(self.frequency_event)

        self.octave_lbl = QComboBox(self)
        self.octave_lbl.addItem('250Hz')
        self.octave_lbl.addItem('315Hz')
        self.octave_lbl.addItem('400Hz')
        self.octave_lbl.addItem('500Hz')
        self.octave_lbl.addItem('630Hz')
        self.octave_lbl.addItem('800Hz')
        self.octave_lbl.addItem('1000Hz')
        self.octave_lbl.addItem('1250Hz')
        self.octave_lbl.addItem('1600Hz')
        self.octave_lbl.addItem('2000Hz')
        self.octave_lbl.addItem('2500Hz')
        self.octave_lbl.addItem('3150Hz')
        self.octave_lbl.addItem('4000Hz')
        self.octave_lbl.addItem('5000Hz')
        self.octave_lbl.addItem('6300Hz')
        self.octave_lbl.addItem('8000Hz')
        self.octave_lbl.addItem('10000Hz')
        self.octave_lbl.addItem('12500Hz')
        self.octave_lbl.addItem('16000Hz')
        self.octave_lbl.addItem('20000Hz')

        self.grid.addWidget(self.octave_lbl, 1, 8)

    def sound_control(self):
        if self.sound_flag == 0:  # init or sound off -> sound on
            self.sound_flag = 1  # on
            self.sound_btn.setIcon(QIcon('icons/sound.png'))

            self.no_signal_btn = QPushButton('', self)
            self.no_signal_btn.setMinimumHeight(65)
            self.no_signal_btn.setMaximumWidth(85)
            self.no_signal_btn.setIcon(QIcon('./icons/no-signal.png'))
            self.no_signal_btn.setIconSize(QSize(60, 60))
            self.no_signal_btn.setStyleSheet("background-color: #55B0BC;")
            self.grid.addWidget(self.no_signal_btn, 0, 8)
            self.no_signal_btn.clicked.connect(self.sound_event)

            self.sound_slider = QSlider(Qt.Vertical,self)
            self.sound_slider.setRange(0, 50)
            self.sound_slider.setSingleStep(2)
            self.sound_slider.setStyleSheet("margin-left: 3.5em; margin-bottom: 30px")
            self.grid.addWidget(self.sound_slider, 1, 8, 6, 1)

        else:  # sound on -> sound off
            self.sound_flag = 0  # off
            self.sound_btn.setIcon(QIcon('icons/sound-off.png'))
            self.grid.removeWidget(self.no_signal_btn)
            self.no_signal_btn.deleteLater()
            self.no_signal_btn = None

            self.grid.removeWidget(self.sound_slider)
            self.sound_slider.deleteLater()
            self.sound_slider = None

    def sound_event(self):
        if Triggers.sound_trig == 0:  # 전영역 주파수
            Triggers.sound_trig += 1
            self.no_signal_btn.setIcon(QIcon('icons/no-signal.png'))

        elif Triggers.sound_trig > 0:  # 선택 영역 주파수
            Triggers.sound_trig = 0
            self.no_signal_btn.setIcon(QIcon('icons/signal.png'))

    # time setting (측정 영상 저장 시간 설정)
    def time_setting_event(self):
        if self.time_st_flag == 0:  # init or time_setting on
            self.time_st_flag = 1  # on

            self.saved_lbl = QLabel('저장시간', self)
            self.grid.addWidget(self.saved_lbl, 0, 8)

            self.time_set = QComboBox(self)
            self.time_set.addItem('10 초')
            self.time_set.addItem('30 초')
            self.time_set.addItem('60 초')
            self.grid.addWidget(self.time_set, 1, 8)

        else:  # time_setting off
            self.time_st_flag = 0  # off
            # print(self.time_set.currentText())

            self.grid.removeWidget(self.saved_lbl)
            self.saved_lbl.deleteLater()
            self.saved_lbl = None

            self.grid.removeWidget(self.time_set)
            self.time_set.deleteLater()
            self.time_set = None

    def time_navigation_event(self):
        if self.time_nv_flag == 0:  # init or time_navigation on
            self.time_nv_flag = 1  # on

            self.time_lbl = QLabel('0')
            self.grid.addWidget(self.time_lbl, 0, 8)
            self.time_lbl.setStyleSheet("margin-left: 2em;")

            self.time_up_btn = QPushButton('', self)
            self.time_up_btn.setMinimumHeight(65)
            self.time_up_btn.setMaximumWidth(85)
            self.time_up_btn.setIcon(QIcon('./icons/up-arrow.png'))
            self.time_up_btn.setIconSize(QSize(60, 60))
            self.time_up_btn.setStyleSheet("background-color: #55B0BC;")
            self.time_up_btn.clicked.connect(self.time_up_event)
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
            self.time_down_btn.clicked.connect(self.time_down_event)
            self.grid.addWidget(self.time_down_btn, 6, 8)


        else:  # time_navigation off
            self.time_nv_flag = 0  # off

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

    # time_navigation_arrow_btn_event
    def time_up_event(self):
        self.now_time = self.slider.value()
        self.slider.setValue(self.now_time + 1)

    def time_down_event(self):
        self.now_time = self.slider.value()
        self.slider.setValue(self.now_time - 1)

    def slider_value_changed(self):
        self.time_val = self.slider.value()
        self.time_lbl.setText(str(self.time_val))

    # frequency_slider_event
    def frequency_slider_value_changed(self):
        self.freq_val = self.frequency_slider.value()
        self.max_freq_set = self.freq_val[1]
        self.min_freq_set = self.freq_val[0]
        self.max_freq_lbl.setText('최대 Freq \n' + str(self.max_freq_set))
        self.min_freq_lbl.setText('최소 Freq \n' + str(self.min_freq_set))
        # print('low:' + str(self.freq_val[0]))
        # print('high:' + str(self.freq_val[1]))

    # file open
    def fileOpen(self):
        fileName = QFileDialog.getOpenFileName(self, self.tr("Open Data Files"), './', self.tr(
            "Data Files (*.csv *.xls *.xlsx *.tdms);; Images (*.png *.xpm *.jpg *.gif);; All Files(*.*)"))
        print("load file : ", fileName[0])
        return fileName


class MeasurementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')  # 단축키
        exitAction.setStatusTip('Exit application')  # 상태팁
        exitAction.triggered.connect(qApp.quit)  # 어플리케이션 종료

        self.statusBar()

        menubar = self.menuBar()
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
