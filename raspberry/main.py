import RPi.GPIO as GPIO
import os

from client import OpenAiClient
from audio_recording import audio_recording
from matrix import faces
from motor import Motor


API_KEY = os.getenv("API_KEY")

client = OpenAiClient(API_KEY)
faces = faces()
motor = Motor(12, 13, 22, 23, 24, 25)  # PWM1, PWM2, R_EN1, L_EN1, R_EN2, L_EN2 (PWM Motor 1 -> 12, 18 PWM Motor 2 -> 13, 19)
with open("raspberry/instructions.txt", "r", encoding="UTF-8") as file:
    instructions = file.read()

mode = 2

messages = [{"role": "developer", "content": instructions}]

while mode == 1:
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
while mode == 2:
    motor.move(10)