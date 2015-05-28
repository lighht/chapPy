import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import chapPy

class Widget(QLabel):
    trigger = pyqtSignal()
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        super(Widget, self).__init__()
        self.button = QPushButton('Start', self)
        self.label = QLabel(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.button_clicked)
        self.trigger.connect(self.handle_trigger)
        self.statusbar = QStatusBar()
        layout.addWidget(self.statusbar)

    def button_clicked(self):
        self.trigger.emit()

    @pyqtSlot()
    def handle_trigger(self):
        message = "Greeting.."
        #greeting = self.get_greeting()
        self.statusbar.showMessage(message, 5)
        message = "wait to hear"
        #self.statusbar.showMessage(message, 5)
        #self.text_to_speech(greeting)
        message = "Listening"
        self.statusbar.showMessage(message, 5)
        stt = self.speech_to_text()
        self.statusbar.showMessage(stt, 5)
        reply = chapPy.chap_chat(text=stt)
        self.statusbar.showMessage(reply, 5)
        print(reply)
        self.text_to_speech(reply)

    def speech_to_text(self):
        import pyaudio  # Needs pyaudio as we use the mic and speakers
        import speech_recognition as sr

        r = sr.Recognizer()
        with sr.Microphone() as source:  # use the default microphone as the audio source
            audio = r.listen(source)  # listen for the first phrase and extract it into audio data
            print("Listening..")
        try:
            output = r.recognize(audio)  # recognize speech using Google Speech Recognition
            print(output)
        except LookupError:  # speech is unintelligible
            print("Could not understand audio")
            output = "I did not understand what you said"
        return output

    def text_to_speech(self, text):
        import pyglet
        import time
        from gtts import gTTS

        tts = gTTS(text=text, lang="en")
        tts.save("gtts.mp3")
        music = pyglet.resource.media('gtts.mp3')
        music.play()
        # time.sleep(2)

    def get_greeting(self):
        import datetime

        now = datetime.datetime.now()
        hour = now.hour
        if hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 13:
            greeting = "Good noon"
        elif 13 <= hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        return greeting


app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec_())
