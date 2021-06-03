################################################################################################
###  Check if the word satisfies a constraint                                                ###
################################################################################################
import codecs
import sys
import random
import re
from const import *
from procFeature import *
from procConstr import *
from genNumWords import *
from numWordtoUni import *
from helpers import *
from chkWordsCons import *
from chooseConstr import *

### Globals for feature processing
val_flag = 0
word_lst = []
lines = []
snd_feat = []
wordCons_lst = []
wordCons_matrix = []
##################################################################################################
### Generate LEX_SIZE words pass them through constraint list. If the the valid flag = 1 then  ###
### remove words from the word list that satisfy any of the constraints. Update the number of  ###
### valid words found and continue until we find VLEX_SIZE words.                              ###
##################################################################################################

##################################################################################################
### If the word in the wordCons_matrix entry satisfies a constraint then return 0 else 1.      ###
##################################################################################################
def valid_word(wcm):
    for c in range(1, len(wcm)):
        if (wcm[c] > 0):
            return 0
    return 1
##################################################################################################
### Remove words that violate any of rhe constraints                                          ####
##################################################################################################
def remove_words(wc_mat):
    upd_wcm = []
    for wc in wc_mat: 
        if valid_word(wc):        ### word satisfy any constraint
            upd_wcm.append(wc)    ### add the entry to updated mat
    return upd_wcm                ### Return updated wordcons_mat
##################################################################################################
### This is the main function. It does the following actions.                                  ###
### 1. Randomly choose CONS_SIZE constraints from the repository/marked                        ###
### 2. Process the features                                                                    ###
### 3. Process the constraints                                                                 ###
### 4. Randomly generate LEX_SIZE words                                                        ###
### 5. Pass the words and select words not violating any of the constraints.                   ###
### 6. Update the output list of words while removing duplicates.                              ###
### 7. Continue steps 4-6 until VLEX_SIZE output words are obtained. Print these.              ###
##################################################################################################
def genLanguage(val_flag):
    num_vwords = 0
    vwc_mat = []
    owc_mat = []
    tmp_wc = []
    word_lst = []

    ### Process the features
    proc_feat()
    ### Randomly generate constraints
    #chooseCons_lst()
    ### Process the constraints
    constraint_matrix = proc_Constr()

    if (val_flag == 1):                           ### Generate only valid words
        while (num_vwords < VLEX_SIZE):           ### not collected VLEX_SIZE output words yet
            word_lst = []
            genNumwords(LEX_SIZE, word_lst)       ### generate LEX_SIZE words
            result = []
            for w in word_lst: 
                if (w not in result):
                    result.append(w)
            word_lst = result
            wordCons_matrix = check_wordlst(word_lst) ### Pass the words through the constraints
            tmpwc = []
            tmpwc = remove_words(wordCons_matrix) ### remove the words that violate any constraint
            if (len(tmpwc)):                      ### if there are any valid words 
                vwc_mat = []
                for wc in (tmpwc):
                    if wc not in owc_mat:         ### Check that these are not already found
                        vwc_mat.append(wc)        ### Add them to the new valid words
                if (len(vwc_mat)): 
                        print vwc_mat
                        owc_mat += vwc_mat        ### Update the set of output words
                        num_vwords += len(vwc_mat) ### Update the number of output words
                        print num_vwords
        wordCons_matrix = owc_mat                 ### Add the new words
    return wordCons_matrix
###############################################################################################
#### Main Function                                                                          ###
##############################################################################################
def genLanguagePrint(): 
    val_flag = 1                                  ### Set valid words flag 
    wordCons_matrix = genLanguage(val_flag)       ### Generate the language
    
    if (val_flag == 1): 
        outf = open("Language", "wb") 
    whead = "Words"                              ### Headers for the output file
    outf.write(whead);
    outf.write("\n\n")
    for wcm in (wordCons_matrix):
        outStr = numword_to_sndword(wcm[0])
        outf.write(outStr.encode("UTF-8"))
        outf.write("\n")
    outf.close()
## Call the main function to run the program
genLanguagePrint()