from vidstream import AudioSender
from vidstream import AudioReceiver

import threading


receiver = AudioReceiver('10.10.1.190', 9999)
receive_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('10.10.0.67', 9999)
sender_thread = threading.Thread(target=sender.start_stream)


receive_thread.start()
sender_thread.start()
