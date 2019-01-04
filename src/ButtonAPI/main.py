
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


    # TODO Should be able to detect PLUGGING-IN and REMOVING
    # TODO Should have full macro support, any key can be programmed
    # TODO Should have nested folders
    
    
    # TODO Remodel the crappy streamdeck API
    # First plugged in deck always be deck[0]

    # Varibles
    # StreamDeck.decks
    
    # Functions
    # StreamDeck.Deck.set_image(image)

    # Events
    # StreamDeck.on_deck_plugged_in(deck)
    # StreamDeck.on_deck_removed(deck)
    # StreamDeck.Deck.on_button_pressed()
    # StreamDeck.Deck.on_button_released()
    
    


    manager = StreamDeck.DeviceManager()
    deck = manager.enumerate()[0]

    deck.open()
    deck.reset()

    deck.set_brightness(100)

    deck.set_key_callback(key_change_callback)

    # wait forever
    Event().wait()
        