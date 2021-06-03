################################################################################################
#### Generate lexicon_size numeric valued words at random                                    ###
################################################################################################
import codecs
import sys
import random
from const import *

########################################################################
### Functions added for ranking
########################################################################
def gen_newword(word, locrep_lst):
    nword = word
    for lr in (locrep_lst): 
        loc = lr[0] 
        rep = lr[1] 
        nword[loc] = rep
    return nword
########################################################################


def genNumwords(lsize, word_lst): 
    #print str(sys.stdout.encoding)
    #sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout)
    lines = []
    snd_feat = []
    for w in range(1,lsize + 1) :
        numword = [] 
        continue_to = 1
        while (continue_to):
            new_snd = random.randint(0,NUM_SOUNDS-1)
            numword.append(new_snd)
            if(len(numword) > 1 and random.random() > 1/((len(numword)-1)**0.75)):
                continue_to = 0
                word_lst.append(numword)
    #print word_lst               ## This will print number valued word_list
#word_lst = []
#genNumwords(100, word_lst)
#word = [73, 5, 7, 8]
#lr_lst = [[1, 10], [2, 11], [3, 73]]
#nw = gen_newword(word, lr_lst)
#print nw