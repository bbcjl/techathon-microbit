from microbit import *

while True:
    message = radio.receive()
    if message:
        for i in range(0, 4):
            display.show(Image.CHESSBOARD)
            sleep(200)
            display.show(Image.NO)
            sleep(200)
        display.scroll("Item detected as stolen!", delay = 100)