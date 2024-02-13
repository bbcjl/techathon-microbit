from microbit import *
import radio

radio.on()
radio.config(channel=0, power=7)

mode = 0
mode_max = 3
is_in_demo_mode = False

def change_mode(mode):
    mode += 1
    if mode > mode_max:
        mode = 0
    display.scroll(mode)
    return mode

while True:
    #None Mode
    if not is_in_demo_mode:
        if pin_logo.is_touched():
            mode = change_mode(mode)
    
        if button_a.is_pressed():
            radio.send("left")
            display.show(Image.ARROW_W)
            sleep(100)
            display.clear()
            while button_a.is_pressed():
                pass
    
        if button_b.is_pressed():
            radio.send("right")
            display.show(Image.ARROW_E)
            sleep(100)
            display.clear()
            while button_b.is_pressed():
                pass

    #Bus Mode
    if mode == 1:
        if button_a.is_pressed():
            is_in_demo_mode = True
            radio.config(power=0)
            display.show(Image.DUCK)
            while not pin_logo.is_touched():
                radio.send("25 to Rail Station")
                sleep(500)
            display.clear()
            radio.config(power=7)
            mode = change_mode(mode)
            is_in_demo_mode = False

    #Theft Mode
    if mode == 3:
        if button_a.is_pressed():
            is_in_demo_mode = True
            display.scroll('T')
            while not pin_logo.is_touched():
                message = radio.receive()
                if message:
                    for i in range(0, 4):
                        display.show(Image.CHESSBOARD)
                        sleep(200)
                        display.show(Image.NO)
                        sleep(200)
                    display.scroll("Item detected as stolen!", delay = 100)
            mode = change_mode(mode)
            is_in_demo_mode = False


