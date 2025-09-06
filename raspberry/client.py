import openai
import sounddevice as sd
from typing import List, Dict


class OpenAiClient:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.client = openai.OpenAI()

    def trancription(self, audio_input):
        transcript = self.client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_input,
            language="pt"
        )
        return (transcript.text)

    def record_message(self, messages: List[Dict[str, str]], speaker: str, content: str):
        messages.append({
            "role": speaker,
            "content": content
        })
        return messages

    def get_response(self, messages: List[Dict[str, str]]):
        completion = self.client.chat.completions.create(
            model="gpt-4.1-nano-2025-04-14",
            messages=messages
        )

        return completion.choices[0].message.content

    def text_to_speech(self, text: str, voice: str = "alloy", speed: float = 1.25):
        with openai.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice=voice,
            input=text,
            response_format="pcm",
            speed=speed
        ) as response:
            # Cria stream de saída RAW para PCM16
            with sd.RawOutputStream(samplerate=24000, channels=1, dtype='int16') as stream:
                for chunk in response.iter_bytes(chunk_size=4096):
                    stream.write(chunk)


