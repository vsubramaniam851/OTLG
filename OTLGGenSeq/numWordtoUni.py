################################################################################################
#### Generate words at random                                                                ###
#### Generate lexicon_size number of words                                                   ###
################################################################################################
import codecs
import sys
import random
from const import *

#print str(sys.stdout.encoding)
#sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout)

def numword_to_sndword(word):

    sndword = []
    sndword_str = ""

    for uw in word:
     w = uw +1
     if ((w < 1) and (w > 74)):
         print "ERROR Numeric value of word is out of range\n"
     if (w == 1):
         sndword.append(US1)
     if (w == 2):
         sndword.append( US2)
     if (w == 3):
         sndword.append( US3)
     if (w == 4):
         sndword.append( US4)
     if (w == 5):
         sndword.append( US5)
     if (w == 6):
         sndword.append( US6)
     if (w == 7):
         sndword.append( US7)
     if (w == 8):
         sndword.append( US8)
     if (w == 9):
         sndword.append( US9)
     if (w == 10):
         sndword.append( US10)
     if (w == 11):
         sndword.append( US11)
     if (w == 12):
         sndword.append( US12)
     if (w == 13):
         sndword.append( US13)
     if (w == 14):
         sndword.append( US14)
     if (w == 15):
         sndword.append( US15)
     if (w == 16):
         sndword.append( US16)
     if (w == 17):
         sndword.append( US17)
     if (w == 18):
         sndword.append( US18)
     if (w == 19):
         sndword.append( US19)
     if (w == 20):
         sndword.append( US20)
     if (w == 21):
         sndword.append( US21)
     if (w == 22):
         sndword.append( US22)
     if (w == 23):
         sndword.append( US23)
     if (w == 24):
         sndword.append( US24)
     if (w == 25):
         sndword.append( US25)
     if (w == 26):
         sndword.append( US26)
     if (w == 27):
         sndword.append( US27)
     if (w == 28):
         sndword.append( US28)
     if (w == 29):
         sndword.append( US29)
     if (w == 30):
         sndword.append( US30)
     if (w == 31):
         sndword.append( US31)
     if (w == 32):
         sndword.append( US32)
     if (w == 33):
         sndword.append( US33)
     if (w == 34):
         sndword.append( US34)
     if (w == 35):
         sndword.append( US35)
     if (w == 36):
         sndword.append( US36)
     if (w == 37):
         sndword.append( US37)
     if (w == 38):
         sndword.append( US38)
     if (w == 39):
         sndword.append( US39)
     if (w == 40):
         sndword.append( US40)
     if (w == 41):
         sndword.append( US41)
     if (w == 42):
         sndword.append( US42)
     if (w == 43):
         sndword.append( US43)
     if (w == 44):
         sndword.append( US44)
     if (w == 45):
         sndword.append( US45)
     if (w == 46):
         sndword.append( US46)
     if (w == 47):
         sndword.append( US47)
     if (w == 48):
         sndword.append( US48)
     if (w == 49):
         sndword.append( US49)
     if (w == 50):
         sndword.append( US50)
     if (w == 51):
         sndword.append( US51)
     if (w == 52):
         sndword.append( US52)
     if (w == 53):
         sndword.append( US53)
     if (w == 54):
         sndword.append( US54)
     if (w == 55):
         sndword.append( US55)
     if (w == 56):
         sndword.append( US56)
     if (w == 57):
         sndword.append( US57)
     if (w == 58):
         sndword.append( US58)
     if (w == 59):
         sndword.append( US59)
     if (w == 60):
         sndword.append( US60)
     if (w == 61):
         sndword.append( US61)
     if (w == 62):
         sndword.append( US62)
     if (w == 63):
         sndword.append( US63)
     if (w == 64):
         sndword.append( US64)
     if (w == 65):
         sndword.append( US65)
     if (w == 66):
         sndword.append( US66)
     if (w == 67):
         sndword.append( US67)
     if (w == 68):
         sndword.append( US68)
     if (w == 69):
         sndword.append( US69)
     if (w == 70):
         sndword.append( US70)
     if (w == 71):
         sndword.append( US71)
     if (w == 72):
         sndword.append( US72)
     if (w == 73):
         sndword.append( US73)
     if (w == 74):
         sndword.append( US74)
    for s in sndword:
        sndword_str += s
    #print sndword_str
    return sndword_str

#numword_to_sndword(numword)