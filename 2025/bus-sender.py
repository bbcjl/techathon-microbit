from microbit import *

radio.config(channel=0, power=7) # Channel to use from number on handout

while True:
    radio.send("25 to Rail Station")