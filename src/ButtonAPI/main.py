
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


    # TODO Should be able to detect PLUGGING and UN-PLUGGING
    # TODO Should have full macro support, any key can be programmed
    # TODO Should have nested folders


    manager = StreamDeck.DeviceManager()
    deck = manager.enumerate()[0]

    deck.open()
    deck.reset()

    deck.set_brightness(100)

    deck.set_key_callback(key_change_callback)

    # wait forever
    Event().wait()
        