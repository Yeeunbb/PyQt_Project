import sys
import pyqtgraph as pg
import FinanceDataReader as fdr
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class MeasurementWidget(QWidget):

    def __init__(self):
        super().__init__()
    #     self.initUI()
    #
    # def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.rec_btn = QPushButton('', self)
        self.rec_btn.setMinimumHeight(65)
        self.rec_btn.setMaximumWidth(85)
        self.rec_btn.setIcon(QIcon('./icons/rec.png'))
        self.rec_btn.setIconSize(QSize(60, 60))
        self.rec_btn.setStyleSheet("background-color: #55B0BC;")

        self.capture_btn = QPushButton('', self)
        self.capture_btn.setMinimumHeight(65)
        self.capture_btn.setMaximumWidth(85)
        self.capture_btn.setIcon(QIcon('./icons/capture.png'))
        self.capture_btn.setIconSize(QSize(60, 60))
        self.capture_btn.setStyleSheet("background-color: #55B0BC;")

        self.time_marker_btn = QPushButton('', self)
        self.time_marker_btn.setMinimumHeight(65)
        self.time_marker_btn.setMaximumWidth(85)
        self.time_marker_btn.setIcon(QIcon('./icons/time-marker.png'))
        self.time_marker_btn.setIconSize(QSize(60, 60))
        self.time_marker_btn.setStyleSheet("background-color: #55B0BC;")

        self.file_open_btn = QPushButton('', self)
        self.file_open_btn.setMinimumHeight(65)
        self.file_open_btn.setMaximumWidth(85)
        self.file_open_btn.setIcon(QIcon('./icons/file-open.png'))
        self.file_open_btn.setIconSize(QSize(60, 60))
        self.file_open_btn.setStyleSheet("background-color: #55B0BC;")

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

        self.play_btn = QPushButton('', self)
        self.play_btn.setMinimumHeight(65)
        self.play_btn.setMaximumWidth(85)
        self.play_btn.setIcon(QIcon('./icons/play.png'))
        self.play_btn.setIconSize(QSize(60, 60))
        self.play_btn.setStyleSheet("background-color: #55B0BC;")


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

        self.db_scaling_btn = QPushButton('', self)
        self.db_scaling_btn.setMinimumHeight(65)
        self.db_scaling_btn.setMaximumWidth(85)
        self.db_scaling_btn.setIcon(QIcon('./icons/db-scaling.png'))
        self.db_scaling_btn.setIconSize(QSize(60, 60))
        self.db_scaling_btn.setStyleSheet("background-color: #55B0BC;")

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

        self.time_setting_btn = QPushButton('', self)
        self.time_setting_btn.setMinimumHeight(65)
        self.time_setting_btn.setMaximumWidth(85)
        self.time_setting_btn.setIcon(QIcon('./icons/time-setting.png'))
        self.time_setting_btn.setIconSize(QSize(60, 60))
        self.time_setting_btn.setStyleSheet("background-color: #55B0BC;")

        self.time_navigation_btn = QPushButton('', self)
        self.time_navigation_btn.setMinimumHeight(65)
        self.time_navigation_btn.setMaximumWidth(85)
        self.time_navigation_btn.setIcon(QIcon('./icons/time-navigator.png'))
        self.time_navigation_btn.setIconSize(QSize(60, 60))
        self.time_navigation_btn.setStyleSheet("background-color: #55B0BC;")


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

        lbl_setting = QLabel('Setting')
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


        grid.addWidget(self.rec_btn, 0, 0)
        grid.addWidget(self.capture_btn, 1, 0)
        grid.addWidget(self.time_marker_btn, 2, 0)
        grid.addWidget(self.file_open_btn, 3, 0)
        grid.addWidget(self.file_save_btn, 4, 0)
        grid.addWidget(self.led_btn, 5, 0)
        grid.addWidget(self.play_btn, 6, 0)

        grid.addWidget(lbl_video, 0, 1, 4, 1)
        grid.addWidget(lbl_graph1, 4, 1, 2, 1)

        grid.addWidget(lbl_bar1, 0, 2, 4, 1)
        grid.addWidget(lbl_bar2, 4, 2, 2, 1)

        grid.addWidget(lbl_graph2, 4, 3, 2, 1)

        grid.addWidget(lbl_setting, 0, 4, 7, 1)


        grid.addWidget(self.exit_btn, 0, 5)
        grid.addWidget(self.video_btn, 1, 5)
        grid.addWidget(self.db_scaling_btn, 2, 5)
        grid.addWidget(self.time_marker_move_btn, 3, 5)
        grid.addWidget(self.sound_btn, 4, 5)
        grid.addWidget(self.time_setting_btn, 5, 5)
        grid.addWidget(self.time_navigation_btn, 6, 5)

class MeasurementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q') # 단축키
        exitAction.setStatusTip('Exit application') # 상태팁
        exitAction.triggered.connect(qApp.quit) # 어플리케이션 종료

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        filemenu = menubar.addMenu('&Edit')
        filemenu.addAction(exitAction)

        wg = MeasurementWidget()
        self.setCentralWidget(wg)

        # self.setGeometry(50, 50, 720, 480)
        self.setWindowTitle('Sound Cam')
        self.resize(720, 480)
        self.show()

        # self.show()

# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex = MeasurementWidget()
#    ex2 = MyMainWindow()
#    sys.exit(app.exec_())