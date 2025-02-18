from microbit import *

radio.config(channel=0) # Channel to use from number on handout

while True:
    data = radio.receive()

    if data:
        display.scroll(data)