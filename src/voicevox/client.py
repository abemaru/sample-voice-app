import os
import requests
import json

from settings import VOICEVOX_HOST
from voicevox.speaker import Speaker

class Voicevox:
    def __init__(self) -> None:
        self.host = VOICEVOX_HOST

    def create_audio(self, text, speaker):
        query_response = self._create_audio_query(text, speaker)
        audio_response = self._create_audio_synthesis(query_response)
        with open('./foo.wav', mode='wb') as f:
            f.write(audio_response.content)

    def _create_audio_query(self, text, speaker):
        return requests.post(
            os.path.join(self.host, 'audio_query'),
            params={
                'text': text,
                'speaker': speaker,
            }
        )

    def _create_audio_synthesis(self, query_response):
        return requests.post(
            os.path.join(self.host, 'synthesis'),
            data=json.dumps(query_response.json())
        )
