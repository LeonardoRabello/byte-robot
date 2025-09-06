import speech_recognition as sr
import io
import scipy.io.wavfile
import numpy as np

recognizer = sr.Recognizer()


def audio_recording():
    with sr.Microphone(sample_rate=44100) as source:
        print("Aguardando você começar a falar...")
        audio = recognizer.listen(source)
        print("Gravação finalizada.")

    raw_data = audio.get_raw_data()
    audio_np = np.frombuffer(raw_data, dtype=np.int16)

    buffer = io.BytesIO()
    scipy.io.wavfile.write(buffer, 44100, audio_np)
    buffer.seek(0)

    buffer.name = "audio.wav"   # 👈 importante: dá um nome pro arquivo
    return buffer
