from microbit import *
import radio

display.show(Image.HAPPY)

radio.config(channel=0, power=0) # Channel to use from number on handout
# Note: power may need to be as low as 0 to reduce how eager the receiver is to trigger

while True:
    radio.send("25 to Rail Station")