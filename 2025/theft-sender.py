from microbit import *
import radio

sleep(3000)

display.show(Image.HAPPY)

radio.config(channel=0, power=7) # Channel to use from number on handout

while True:
    if accelerometer.get_strength() > 1500:
        display.show(Image.ANGRY)

        radio.send("Stolen")