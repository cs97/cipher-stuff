#!/bin/python
#
#   usage:
#       import poor-cipher
#
#       key = "very_good_key"
#       text = "some nice text"
#
#       c = poor-cipher.poor_cipher(key)
#
#       print(cipher.str_enc(text))
#
#   output:
#       éÔßÞÕØÒÉßÊñê
#       

class poor_cipher():
    def __init__(self, newkey: str):
        self.key = newkey
        
    def key_pos(self, pos: int):
        return self.key[pos % len(key)]

    def str_enc(self, str_in: str):
        str_out = ''
        for x in range(len(str_in)):
            str_out = str_out + chr(ord(str_in[x]) + ord(self.key_pos(x)))   #^ +
        return str_out

    def str_dec(self, str_in: str):
        str_out = ''
        for x in range(len(str_in)):
            str_out = str_out + chr(ord(str_in[x]) - ord(self.key_pos(x)))   #^ -
        return str_out
