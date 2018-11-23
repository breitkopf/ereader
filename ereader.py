# fleetfox_2in7epd.py
# Blockchain Messaging Service (BMS Client)
# Compatible with 2.7in epd
#( (C) 2018 Omar Metwally :: ANALOG LABS
# omar@analog.earth
# LICENSE: Analog Labs License (analog.earth)

import epd2in7b
from PIL import Image, ImageFont, ImageDraw
import serial, sys, os
from random import randint
from time import sleep, time
from bcmutil import BCMUtil
import hashlib
import RPi.GPIO as GPIO
import subprocess
import atexit

GPIO.setmode(GPIO.BCM)

COLORED = 1

key1 = 5
key2 = 6
key3 = 13
key4 = 19

GPIO.setup(key1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

checkpoint_util = BCMUtil()
greeting = "Loading Fleet Fox Blockchain Messaging Service..."
print(greeting)
#greeting= "ANALOG.EARTH\n\nTo the future machine with the computational power to unlock today's encrypted secrets. To the future human with the spiritual power to unlock all secrets.\n\n"


def exit_handler():
    pass
    '''
    print('Shutting down...')
    bash_command = "sudo shutdown now"
    bash_command = bash_command.split()
    subprocess.run( bash_command, check = True, shell=True )
    '''


def update_2in7epd(text_string,image_path, sleep_sec):
    epd = epd2in7b.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0] * int((epd.width * epd.height / 8))
    frame_red = [0] * int((epd.width * epd.height / 8))
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 14)

    print(text_string)

    if image_path:
        frame_black = epd.get_frame_buffer(Image.open(image_path))
    if text_string:
        epd.draw_string_at(frame_black, 4, 4, text_string, font, COLORED)
    epd.display_frame(frame_black, frame_red)

    sleep(sleep_sec)

atexit.register(exit_handler)

home_greeting = "Fleet Fox Receiver\nanalog.earth\n\nKey1:Home\nKey2:Account\nKey3:GPS Coords\nKey4: Sync \n\nKey1+Key2: Ping\nKey1+Key3:Drop Pin\nKey1+Key4: Exit"
#frame_black = epd.get_frame_buffer(Image.open('foxbw.bmp'))
#epd.draw_string_at(frame_black, 4, 4, msg_util.format_string_to_2in7epd(greeting), font, COLORED)
#epd.display_frame(frame_black, frame_red)

update_2in7epd(home_greeting,None,0)

while True:
                # read from GPS module
                # read 2.7in epd keys
                key1state = GPIO.input(key1)
                key2state = GPIO.input(key2)
                key3state = GPIO.input(key3)
                key4state = GPIO.input(key4)

                if not key1state and not key4state:
                    display_string = "Shutting down Fleet Fox..."
                    print(display_string)
                    update_2in7epd( display_string, None, 0 )
                    exit(0)

                if not key1state and key2state and key3state and key4state:
                    DISPLAY_HOME_TO_EPD = 1
                if not key2state and key1state and key3state and key4state:
                    DISPLAY_STATUS_TO_EPD = 1
                if not key3state and key1state and key2state and key4state:
                    DISPLAY_COORDS_TO_EPD = 1
                if not key4state and key1state and key2state and key3state:
                    display_string = "Downloading Chkpts..."
                    update_2in7epd(display_string, None, 0) 



