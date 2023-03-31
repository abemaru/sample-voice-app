from enum import IntEnum

class Speaker(IntEnum):
    """
    voicevox apiのaudio_query/に投げる際に
    どのキャラの音声で再生させるかを指定するクラス
    """

    # ずんだもん
    ZUNDA_NORMAL = 3
    ZUNDA_SWEET = 1
    ZUNDA_TUNTUN = 7
    ZUNDA_SEXY = 5

    # 四国めたん
    METAN_NORMAL = 2
    METAN_SWEET = 0
    METAN_SEXY = 4
    METAN_TUNTUN = 6

    # 春日部つむぎ
    TUMUGI = 8

    # 冥鳴ひまり
    HIMARI = 14

    # 九州そら
    SORA_NORMAL = 16
    SORA_SWEET = 15
    SORA_SEXY = 17
    SORA_TUNTUN = 18
    SORA_ASMR = 19
