
from client import OpenAiClient
from audio_recording import audio_recording
from matrix import faces
import os

API_KEY = os.getenv("API_KEY")

client = OpenAiClient(API_KEY)
faces = faces()
with open("raspberry/instructions.txt", "r", encoding="UTF-8") as file:
    instructions = file.read()



messages = [{"role": "developer", "content": instructions}]

while True:
    audio_data = audio_recording()  # Get user audio
    input = client.trancription(audio_data)  # transcript user audio
    print(f"input: {input}")  # save user message in the context
    messages = client.record_message(messages, "user", input)
    output = client.get_response(messages)  # get robot message
    output, face = faces.split_face_and_message(output)
    print(f"output: {output}\nface:{face}")
    # save robot message in the context
    messages = client.record_message(messages, "assistant", output)
    faces.show_face(face)
    client.text_to_speech(output)  # convert robot message to audio
