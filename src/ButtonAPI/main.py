
import StreamDeck.StreamDeck as StreamDeck
import threading
from PIL import Image, ImageDraw, ImageFont
import time
from threading import Event

current_folder = None


def key_change_callback(deck, key, state):
    if(state == "Pressed"):
        current_folder.on_pressed(key)
    elif(state == "Released"):
        current_folder.on_released(key)



if __name__ == "__main__":
    manager = StreamDeck.DeviceManager()
    deck = manager.enumerate()[0]

    deck.open()
    deck.reset()

    deck.set_brightness(100)

    deck.set_key_callback(key_change_callback)

    # wait forever
    Event().wait()
        