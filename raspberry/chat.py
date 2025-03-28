#Importing libraries
from google import genai
import os
from dotenv import load_dotenv
from gtts import gTTS
import pygame

##Getting API key
load_dotenv()

#setting up AI
client = genai.Client(api_key=os.getenv("API_KEY"))
chat = client.chats.create(model="gemini-2.0-flash")
pygame.mixer.init()

#input
def fast_chat(text):
    response = chat.send_message(text)
    #output
    print(response.text)
    tts = gTTS(response.text, 'com.br', 'pt')
    tts.save('output.mp3')
    sound = pygame.mixer.Sound('output.mp3')
    sound.play()

    #waiting audio end
    while pygame.mixer.get_busy():
        pass

def video_chat(video_file, text):
    response = chat.send_message([video_file, text])
    #output
    print(response.text)
    tts = gTTS(response.text, 'com.br', 'pt')
    tts.save('/data/output/output.mp3')
    sound = pygame.mixer.Sound('/data/output/output.mp3')
    sound.play()

    #waiting audio end
    while pygame.mixer.get_busy():
        pass



