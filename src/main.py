from voicevox.client import Voicevox
from voicevox.speaker import Speaker

if __name__ == '__main__':
    print(Speaker.METAN_NORMAL)

    client = Voicevox()
    client.create_audio('これはサンプルだよ', Speaker.ZUNDA_NORMAL)