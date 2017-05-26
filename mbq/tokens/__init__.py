from .decoder import Decoder
from .exceptions import TokenError  # noqa


def init(key, audiences):
    global decoder
    decoder = Decoder(key, audiences)
