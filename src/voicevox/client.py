import os
import requests
import json

from settings import VOICEVOX_HOST
from voicevox.speaker import Speaker

class Voicevox:
    """
    voicevoxクライアントに対する操作をまとめたクラス
    """
    def __init__(self) -> None:
        self.host = VOICEVOX_HOST

    def create_audio(self, text: str, speaker: Speaker):
        """
        指定されたテキストの内容を指定したキャラクターに読み上げさせた内容を
        wavファイルに保存する関数
        :param text: 読み上げてもらう内容
        :param speaker: 読み上げを行うキャラクター
        """
        query_response = self._create_audio_query(text, speaker)
        audio_response = self._create_audio_synthesis(query_response)
        with open('./foo.wav', mode='wb') as f:
            f.write(audio_response.content)

    def _create_audio_query(self, text: str, speaker: Speaker):
        """
        音声合成用のクエリを作成する関数
        :param text: 読み上げてもらう内容
        :param speaker: 読み上げを行うキャラクター
        """
        return requests.post(
            os.path.join(self.host, 'audio_query'),
            params={
                'text': text,
                'speaker': speaker,
            }
        )

    def _create_audio_synthesis(self, query_response):
        """
        音声合成を行う関数
        :param query_response: audio_queryによって作成されたレスポンス
        """
        return requests.post(
            os.path.join(self.host, 'synthesis'),
            data=json.dumps(query_response.json())
        )
