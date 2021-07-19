import sys
import pyqtgraph as pg
import FinanceDataReader as fdr
# from bs4 import BeautifulSoup
# from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QGridLayout, QLabel, QPushButton)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        rec_btn = QPushButton('', self)
        rec_btn.setMinimumHeight(125)
        rec_btn.setMaximumWidth(150)
        rec_btn.setIcon(QIcon('./icons/rec.jpg'))
        rec_btn.setIconSize(QSize(100, 100))
        rec_btn.setStyleSheet("background-color: #55B0BC;")

        capture_btn = QPushButton('', self)
        capture_btn.setMinimumHeight(125)
        capture_btn.setMaximumWidth(150)
        capture_btn.setIcon(QIcon('./icons/capture.png'))
        capture_btn.setIconSize(QSize(100, 100))
        capture_btn.setStyleSheet("background-color: #55B0BC;")

        time_marker_btn = QPushButton('', self)
        time_marker_btn.setMinimumHeight(125)
        time_marker_btn.setMaximumWidth(150)
        time_marker_btn.setIcon(QIcon('./icons/time-marker.png'))
        time_marker_btn.setIconSize(QSize(100, 100))
        time_marker_btn.setStyleSheet("background-color: #55B0BC;")

        file_open_btn = QPushButton('', self)
        file_open_btn.setMinimumHeight(125)
        file_open_btn.setMaximumWidth(150)
        file_open_btn.setIcon(QIcon('./icons/file-open.png'))
        file_open_btn.setIconSize(QSize(100, 100))
        file_open_btn.setStyleSheet("background-color: #55B0BC;")

        file_save_btn = QPushButton('', self)
        file_save_btn.setMinimumHeight(125)
        file_save_btn.setMaximumWidth(150)
        file_save_btn.setIcon(QIcon('./icons/file-save.png'))
        file_save_btn.setIconSize(QSize(100, 100))
        file_save_btn.setStyleSheet("background-color: #55B0BC;")

        led_btn = QPushButton('', self)
        led_btn.setMinimumHeight(125)
        led_btn.setMaximumWidth(150)
        led_btn.setIcon(QIcon('./icons/led.png'))
        led_btn.setIconSize(QSize(100, 100))
        led_btn.setStyleSheet("background-color: #55B0BC;")

        play_btn = QPushButton('', self)
        play_btn.setMinimumHeight(125)
        play_btn.setMaximumWidth(150)
        play_btn.setIcon(QIcon('./icons/play.png'))
        play_btn.setIconSize(QSize(100, 100))
        play_btn.setStyleSheet("background-color: #55B0BC;")


        exit_btn = QPushButton('', self)
        exit_btn.setMinimumHeight(125)
        exit_btn.setMaximumWidth(150)
        exit_btn.setIcon(QIcon('./icons/exit.png'))
        exit_btn.setIconSize(QSize(100, 100))
        exit_btn.setStyleSheet("background-color: #55B0BC;")

        video_btn = QPushButton('', self)
        video_btn.setMinimumHeight(125)
        video_btn.setMaximumWidth(150)
        video_btn.setIcon(QIcon('./icons/video.png'))
        video_btn.setIconSize(QSize(100, 100))
        video_btn.setStyleSheet("background-color: #55B0BC;")

        db_scaling_btn = QPushButton('', self)
        db_scaling_btn.setMinimumHeight(125)
        db_scaling_btn.setMaximumWidth(150)
        db_scaling_btn.setIcon(QIcon('./icons/db-scaling.png'))
        db_scaling_btn.setIconSize(QSize(100, 100))
        db_scaling_btn.setStyleSheet("background-color: #55B0BC;")

        time_marker_move_btn = QPushButton('', self)
        time_marker_move_btn.setMinimumHeight(125)
        time_marker_move_btn.setMaximumWidth(150)
        time_marker_move_btn.setIcon(QIcon('./icons/time-marker.png'))
        time_marker_move_btn.setIconSize(QSize(100, 100))
        time_marker_move_btn.setStyleSheet("background-color: #55B0BC;")

        sound_btn = QPushButton('', self)
        sound_btn.setMinimumHeight(125)
        sound_btn.setMaximumWidth(150)
        sound_btn.setIcon(QIcon('./icons/sound.png'))
        sound_btn.setIconSize(QSize(100, 100))
        sound_btn.setStyleSheet("background-color: #55B0BC;")

        time_setting_btn = QPushButton('', self)
        time_setting_btn.setMinimumHeight(125)
        time_setting_btn.setMaximumWidth(150)
        time_setting_btn.setIcon(QIcon('./icons/time-setting.png'))
        time_setting_btn.setIconSize(QSize(100, 100))
        time_setting_btn.setStyleSheet("background-color: #55B0BC;")

        time_navigation_btn = QPushButton('', self)
        time_navigation_btn.setMinimumHeight(125)
        time_navigation_btn.setMaximumWidth(150)
        time_navigation_btn.setIcon(QIcon('./icons/time-navigator.png'))
        time_navigation_btn.setIconSize(QSize(100, 100))
        time_navigation_btn.setStyleSheet("background-color: #55B0BC;")


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


        grid.addWidget(rec_btn, 0, 0)
        grid.addWidget(capture_btn, 1, 0)
        grid.addWidget(time_marker_btn, 2, 0)
        grid.addWidget(file_open_btn, 3, 0)
        grid.addWidget(file_save_btn, 4, 0)
        grid.addWidget(led_btn, 5, 0)
        grid.addWidget(play_btn, 6, 0)

        grid.addWidget(lbl_video, 0, 1, 4, 1)
        grid.addWidget(lbl_graph1, 4, 1, 2, 1)

        grid.addWidget(lbl_bar1, 0, 2, 4, 1)
        grid.addWidget(lbl_bar2, 4, 2, 2, 1)

        grid.addWidget(lbl_graph2, 4, 3, 2, 1)

        grid.addWidget(lbl_setting, 0, 4, 7, 1)


        grid.addWidget(exit_btn, 0, 5)
        grid.addWidget(video_btn, 1, 5)
        grid.addWidget(db_scaling_btn, 2, 5)
        grid.addWidget(time_marker_move_btn, 3, 5)
        grid.addWidget(sound_btn, 4, 5)
        grid.addWidget(time_setting_btn, 5, 5)
        grid.addWidget(time_navigation_btn, 6, 5)


        self.setWindowTitle('Sound Cam')
        self.resize(720, 480)
        # self.show()



class MyMainWindow(QMainWindow):
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

        wg = MyWidget()
        self.setCentralWidget(wg)

        self.setGeometry(50, 50, 720, 480)
        self.setWindowTitle('Sound Cam')
        # self.resize(720, 480)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyWidget()
   ex2 = MyMainWindow()
   sys.exit(app.exec_())