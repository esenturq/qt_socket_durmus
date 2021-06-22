import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
import socket


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Serve stepper") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Step:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

    def clickMethod(self):
        print('Servo step: ' + self.line.text())
        host = 'local host'
        port = 5000

        # create a socket at client side
        # using TCP / IP protocol
        s = socket.socket(socket.AF_INET,
                        socket.SOCK_STREAM)

        # connect it to server and port
        # number on local computer.
        s.connect(('127.0.0.1', port))

        # receive message string from
        # server, at a time 1024 B
        #s.send(b"HELLO, How are you ? \
            #Welcome to Akash hacking World")
        msg = self.line.text()
        s.send(msg.encode())
        #msg = "Bye.............."
        #s.send(msg.encode())

        # disconnect the server
        s.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )