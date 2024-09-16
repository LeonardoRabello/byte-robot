from picamera2 import Picamera2
import subprocess
from time import sleep

cam = Picamera2()

video_config = cam.create_video_configuration(
    main={"size":(768, 768)}
    )
cam.configure(video_config)

cam.start_and_record_video("video.h264")
print('gravando')
sleep(7)
cam.stop_recording()
cam.close()
print('exportando')
command = ['ffmpeg',
           '-i', 'video.h264',
           '-c:v', 'flv1',
           '-c:a', 'mp3',
            'video.flv']
subprocess.run(command, check=True)
print('The archive was converted')