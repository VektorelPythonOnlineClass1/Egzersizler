import time
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys
import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()



delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')



class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True        



    def initUI(self):
        self.win = uic.loadUi(r"C:\Users\kagan\OneDrive\Masaüstü\python kurs\visual sutudio\Egzersizler\Kagan\autoclicker/autoclicker.ui")
        self.BtBaslat.win.clicked.connect(self.TıklamayaBasla)
        self.BtIptal.win.clicked.connect(self.TıklamayıDurdur)
        self.show()



    def  TıklamayaBasla(self):
        self.running = True
        def run(self):
            while self.program_running:
                while self.running:
                    mouse.click(self.button)
                    time.sleep(self.delay)
                    time.sleep(0.1)



mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()                   



def TıklamayıDurdur(self):
    self.running= False
    self.stop_clicking()
    self.program_running = False



    def on_press(key):
        if key == start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == exit_key:
            click_thread.exit()
            listener.stop()




    with Listener(on_press=on_press) as listener:
        listener.join()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())                             