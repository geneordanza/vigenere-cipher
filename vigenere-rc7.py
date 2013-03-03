#!/usr/bin/python
'''
Description: Implementation of vigenere cipher.
Last Revision: July 28, 2011 (revision 7)
Author: Gene Ordanza <gordanza@travelogix.com>
'''

from itertools import izip

class Crypto(object):
   def __init__(self):
      self.alphnum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '
      self.mixed   = 'EIFMSZ50XBGNT16 CUHOV27ARJPW38LDKQY49'
      self.table   = []
      self.size = len(self.alphnum)
      self.genTable(self.mixed, self.table, self.size)

   # Display matrix for visual check of intersection between key and plain text
   def showMatrix(self):
      print '\n'.join(self.table)

   # Generate Table for Vigenere lookup (quickie hackishsolution, needs refactoring)
   def genTable(self, mixed, table, size):
      temp = []
      table.extend([mixed[x:size] + mixed[:x] for x,y in enumerate(mixed)])
      temp.append('-' + self.alphnum)
      for x,y in izip(enumerate(self.alphnum), enumerate(table)):
         temp.append(x[1] + y[1])
      self.table = temp


   # Accept plain text (input) and return cipher text (output)
   def encrypt(self, text, key):
      text = text.upper()
      key  = key.upper() * 20
      block = []

      for data in izip(enumerate(text), enumerate(key)):
         for letter in self.table:
            if ((letter[0] == data[1][1])):
               x = self.table[0].find(data[0][1])
               #x = letter.find(data[0][1])
               block.extend(letter[x])

      return ''.join(block)

   # Accept cipher text (input) and convert back to plain text (output)
   def decrypt(self, text, key):
      text = text.upper()
      key  = key.upper() * 20
      block = []

      for data in izip(enumerate(text), enumerate(key)):
         for letter in self.table:
            if letter[0] == data[1][1]:
               x = letter.rfind(data[0][1])
               block.extend(self.table[0][x])

      return ''.join(block)

if  __name__ == '__main__':
   text='now is the time for all good men to come to the aid of their fellow man'
   key  = 'excalibur'

   vigen = Crypto()
   #vigen.showMatrix()

   cipher = vigen.encrypt(text, key)
   print vigen.encrypt(text, key)
   print vigen.decrypt(cipher, key)
