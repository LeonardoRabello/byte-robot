
import speech_recognition as sr
from picamera2 import Picamera2
import subprocess

microphone = sr.Recognizer()
cam = Picamera2()

video_config = cam.create_video_configuration(
    main={"size":(768, 768)}
    )
cam.configure(video_config)

#listening
with sr.Microphone() as source:
    microphone.adjust_for_ambient_noise(source)
    audio = microphone.listen(source)
    cam.start_and_record_video('/data/input/video.h264')
    print('listening...')
    try:
        texto = microphone.recognize_google(audio, language='pt-BR')
    except:
        print("wasn't possible detect the audio, try speak again")
cam.stop_recording()
cam.close()

command = ['ffmpeg',
           '-i', '/data/input/video.h264',
           '-c:v', 'flv1',
           '-c:a', 'mp3',
            '/data/input/video.flv']
subprocess.run(command, check=True)
print('The archive was converted')

with open("input.txt", "w") as file:
    file.write(texto)


