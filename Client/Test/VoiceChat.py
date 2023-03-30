import pyaudio
import wave
import threading
class VoiceChat:
    def __init__(self):
        self.audio= pyaudio.PyAudio()
        self.buffer = 1024
        self.output = self.audio.open(format=pyaudio.paInt16, output=True, rate=44100, channels=2,frames_per_buffer=self.buffer)
        self.input_stream = self.audio.open(format=pyaudio.paInt16, input=True, rate=44100, channels=2, frames_per_buffer=self.buffer)

    def record(self):
        while True:
            data = self.input_stream.read(self.buffer)
            self.transport.write(data, )
    def start(self):
        pass