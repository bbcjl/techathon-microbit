from microbit import *
import radio

uart.init(baudrate = 9_600)
radio.config(channel = 0)

display.show(Image.ARROW_SE)

while True:
    data = radio.receive()

    if data == "left":
        display.show(Image.ARROW_W)
        uart.write("left\n")

    if data == "right":
        display.show(Image.ARROW_E)
        uart.write("right\n")
