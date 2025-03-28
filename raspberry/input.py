import speech_recognition as sr
from picamera2 import Picamera2
#import subprocess

microphone = sr.Recognizer()
cam = Picamera2()

video_config = cam.create_video_configuration(
    main={"size": (768, 768)}
)
cam.configure(video_config)

# Função para capturar áudio
#def get_audio():
with sr.Microphone() as source:
    microphone.adjust_for_ambient_noise(source)
    print('Listening...')
    audio = microphone.listen(source)
    
    try:
        text = microphone.recognize_google(audio, language='pt-BR')
        print(text)
        #return text
    except sr.UnknownValueError:
        print("Wasn't possible detect the audio. Try speak again")
        #return("Wasn't possible detect the audio. Try speak again")

#Função para capturar áudio e vídeo
def get_audio_and_video():
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
       
        cam.start_recording('/data/input/video.mp4')
        audio = microphone.listen(source)
        cam.stop_recording()
        cam.close()

        try:
            text = microphone.recognize_google(audio, language='pt-BR')
            return text
        except sr.UnknownValueError:
            print("Não foi possível detectar o áudio, tente falar novamente.")
            return "Não foi possível detectar o áudio."

