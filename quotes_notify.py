from PyQt5 import Qt
import sys
import random
from time import sleep

all_quotes = open('quotes.txt', 'r')
vocab = all_quotes.read()
vocab = vocab.split('\n')
#path = "C:\\Users\\Jitender\\AppData\\Local\\Programs\\Python\\Python36\\assistant\\self script\\alert2.jpg"
def send_message(title, message):
    app = Qt.QApplication(sys.argv)
    notification_box = Qt.QSystemTrayIcon(Qt.QIcon(':alert2.jpg'), app)
    notification_box.show()
    notification_box.showMessage(title, message)
    return

while True:
    i = random.randint(0, 2002)
    if  i % 2 == 0:
        if len(vocab[i]) < 80:
            send_message(vocab[i],vocab[i+1])
            sleep(20)

        else:
            continue
    else:
        continue
