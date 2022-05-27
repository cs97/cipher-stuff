#!/bin/python3.10
#
# usage:
#   import easy_aes
#   x = easy_aes('my_strong_key')
#   y = x.encrypt_cbc(bytes('some text', 'utf-8'))

#import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class aes_cbc():

  def __init__(self, password):
      self.__key = hashlib.sha256(bytes(password, "utf8")).digest()

  def decrypt_cbc(self, enc):
      iv = enc[:AES.block_size]
      cipher = AES.new(self.__key, AES.MODE_CBC, iv)
      data = (cipher.decrypt(enc[AES.block_size:]))
      padding_bytes = data[-1]
      return data[:-padding_bytes]

  def encrypt_cbc(self, raw):
      raw = raw + bytes(((16 - len(raw) % 16) * chr(16 - len(raw) % 16)), 'utf8')
      iv = get_random_bytes(AES.block_size)
      cipher = AES.new(self.__key, AES.MODE_CBC,iv)
      return (iv + cipher.encrypt(raw))
