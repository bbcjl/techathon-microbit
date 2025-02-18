from microbit import *
import radio
import time

radio.config(channel = 0, power = 7, queue = 1)

modes = ["none", "bus", "none", "theft"]
mode = 0

busLastMessageTime = 0
busLastReceivedTime = 0

while True:
    if button_a.was_pressed():
        display.show(Image.ARROW_W)
        radio.send("left")
        sleep(200)

    if button_b.was_pressed():
        display.show(Image.ARROW_E)
        radio.send("right")
        sleep(200)

    if pin_logo.is_touched():
        mode += 1

        if mode >= len(modes):
            mode = 0

        if modes[mode] == "bus":
            display.show("B")
            busLastMessageTime = -6_000
        elif modes[mode] == "theft":
            display.show("T")
        else:
            display.show(Image.NO)

        sleep(500)

        display.clear()

    if modes[mode] == "none":
        display.show(Image.HAPPY)

    if modes[mode] == "bus":
        data = radio.receive()

        if data == "left" or data == "right":
            continue

        if data != None:
            busLastReceivedTime = time.ticks_ms()

            if time.ticks_ms() - busLastMessageTime > 10_000:
                display.scroll(data, delay = 100, wait = False)
                busLastMessageTime = time.ticks_ms()

        if data == None and time.ticks_ms() - busLastReceivedTime > 3_000:
            display.clear()

    if modes[mode] == "theft":
        if accelerometer.get_strength() > 1_500:
            display.show(Image.ANGRY)

            radio.send("Stolen")
