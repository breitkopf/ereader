# bcmutil.py - Blockchain Messaging Utility # Handles message encryption, ePaper display formatting,
# (C) 2018 Omar Metwally :: ANALOG LABS
# omar@analog.earth
# LICENSE:  ANALOG LABS LICENSE (analog.earth)


import os
from time import time
import os.path

SECRET = ""
ACCURACY = 3

KEY = "analog labs 2018".encode("latin-1")
IV = "This is an IV456".encode("latin-1")

class BCMUtil:

    def __init__(self):
       self.bottle = []  # a bottle is a collection of (encrypted or unencrypted) messages
       self.checkpoints = []
       #print('Initialized new Blockchain Message Utility object.')

    def format_string_to_2in7epd(self, string_in):
        row_length = 0 
        row = ''
        display_string = ''
        words = string_in.split(' ')

        for w in words:
            curr_word = w
            if len(w) > 20:
                print('No words greater than 20 characters!')
                curr_word = w[:10]+'-\n'+w[10:]+' '
                row = w[10:]
            
            # new projected row length
            row_length = len(row) + len(curr_word) + 1
            print('Row length: ',row_length)

            if row_length > 20:
                display_string += '\n'
                display_string += curr_word + ' '
                row = curr_word + ' '
            else:
                row += curr_word + ' '
                display_string += curr_word + ' '

        return display_string


    def format_string_to_2in9epd(self, string_in):
        row_length = 0 
        row = ''
        display_string = ''
        words = string_in.split(' ')

        for w in words:
            if len(w) > 15:
                print('No words greater than 15 characters!')
                return
            row_length = len(row) + len(w) + 1
            if row_length > 15:
                display_string += '\n'
                display_string += w + ' '
                row = w + ' '
            else:
                row += w + ' '
                display_string += w + ' '

        print('String formatted to 2.9in ePaper display: ')
        print(display_string)
        return display_string


