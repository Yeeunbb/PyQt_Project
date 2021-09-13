from PyQt5.QtCore import QThread, pyqtSignal
import time as tm


# server로부터 데이터를 받고, slicing하는 클래스
class Worker(QThread):
    thread_signal = pyqtSignal(list)

    def __init__(self, val, parent=None, client=None):
        super(Worker, self).__init__(parent)
        self.val = val
        self.thread_type = ''
        self.working = True
        self.client = client

    def run(self):
        if self.working:  # receive real time data
            while True:
                data = self.client.recv(1024)
                recv_data = data.decode('utf-8')

                t = recv_data.split()[0::2]
                s = recv_data.split()[1::2]

                t = list(map(float, t))[0]
                s = list(map(float, s))[0]

                self.val = [t, s]
                self.thread_signal.emit(self.val)

                tm.sleep(0.12)

        else:  # stop, 그래프그리기 중단
            self.terminate()
            self.quit()