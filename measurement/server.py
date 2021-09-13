from socket import *
import time
import numpy as np
import struct
from PyQt5.QtCore import QThread

def server():

    host = "127.0.0.1"
    port = 12345

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(1)
    print("Waiting for client")

    connectionSocket, addr = serverSocket.accept()
    print('connection in', str(connectionSocket))

    f1 = 35 # frequency 1 (Hz)
    f2 = 10 # frequency 2 (Hz)

    start = time.time()
    i = 0
    
    while True:
        # time
        now_time = time.time() - start

        # original signal
        signal = 0.6 * np.sin(2 * np.pi * f1 * now_time) + 3 * np.cos(2 * np.pi * f2 * now_time + np.pi/2) # 복잡한 신호
        # signal = np.sin(2 * np.pi * f2 * now_time) # 간단한 신호

        time.sleep(0.01)

        data = str(now_time) + ' ' + str(signal) + '\n'

        connectionSocket.send(data.encode('utf-8'))

        i += 1

    serverSocket.close()


server()