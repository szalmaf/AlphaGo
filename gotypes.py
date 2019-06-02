import enum


class Player(enum.Enum):
    black = 1
    white = 2


    @property
    def other(self):
        return Player.black if self == Player.black else Player.white


