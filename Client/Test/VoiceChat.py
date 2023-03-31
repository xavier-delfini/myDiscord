import pyaudio
import wave
import threading


class VoiceChat:
    def __init__(self, connexion):
        self.connexion = connexion
        self.audio = pyaudio.PyAudio()
        self.buffer = 1024
        WAVE_OUTPUT_FILENAME = "input.wav"
        self.output = self.audio.open(format=pyaudio.paInt16, output=True, rate=44100, channels=1,
                                      frames_per_buffer=self.buffer)
        self.input_stream = self.audio.open(format=pyaudio.paInt16, input=True, rate=44100, channels=1,
                                            frames_per_buffer=self.buffer)
    def test(self):
        data = self.input_stream.read(self.buffer)
    def record(self):
        while True:
            data = self.input_stream.read(self.buffer)
            #self.transport.write(data)

    def get_audio_from_server(self):
        while True:
            audio_received = self.connexion.recv(2048)

    def start(self):
        pass
test=VoiceChat("a")
test.test()