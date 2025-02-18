from microbit import *
import radio

display.show(Image.HAPPY)

radio.config(channel=0, queue=1) # Channel to use from number on handout

while True:
    data = radio.receive()

    if data:
        display.scroll(data)