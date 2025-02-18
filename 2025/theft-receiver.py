from microbit import *
import radio

display.show(Image.HAPPY)

radio.config(channel=0) # Channel to use from number on handout

while True:
    message = radio.receive()
    if message:
        for i in range(0, 4):
            display.show(Image.CHESSBOARD)
            sleep(200)
            display.show(Image.NO)
            sleep(200)
        display.scroll("Item detected as stolen!", delay = 100)