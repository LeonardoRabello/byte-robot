#Importing libraries
import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS
import pygame

##Getting API key
load_dotenv()

#setting up AI
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
pygame.mixer.init()

#input
with open('input.txt', 'r') as file:
   text = file.read()
print('a')
video_file = genai.upload_file(path='/data/input/video.flv')
print('a')

while video_file.state.name == 'PROCESSING':
    pass
if video_file.state.name == 'FAILED':
    raise ValueError(video_file.state.name)
print('a')

response = chat.send_message([video_file, 'o que voce ve'])

#output
print(response.text)
tts = gTTS(response.text, 'com.br', 'pt')
tts.save('/data/output/output.mp3')
sound = pygame.mixer.Sound('/data/output/output.mp3')
sound.play()

#waiting audio end
while pygame.mixer.get_busy():
    pass
