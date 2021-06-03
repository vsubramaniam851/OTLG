################################################################################################
###  Process the features, constraints and generate lexicon_size words at random.            ###
###  Pass the words through constraints and output a table of the form                       ###
###  Keep generating until at least until 100 valid words are found.                         ###
#### Word --> vector where bit i is 1 means constraint i is satisfied; 0 means violated.     ###
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

### Globals for feature processing
featuresfile = "Features.Phonetic.txt"
#feature_matrix = [[0 for j in range(NUM_FEAT)] for i in range(NUM_SOUNDS)] 
################################################################################################
### Global Variables                                                                         ###
################################################################################################
Constraintfile_1 = "Maori.Inventory.txt"
Constraintfile_2 = "Maori.Sequences.txt"
numInvCons = 19    ### This needs to be FIXED
val_flag = 0
word_lst = []
lines = []
snd_feat = []
wordCons_lst = []
wordCons_matrix = []
################################################################################################
### Ranking functions                                                                        ###
################################################################################################
###  Produce a wordCons_matrix which gives the number of times each word violates constaints ###
###  The structure will be: [[word,  num1, num2,   ...,                    numk]             ###
###                          [word,  num1, num2m   ...,                    numk]             ###
###                          ....                                                            ###
###                         ]                                                                ###
################################################################################################

################################################################################################
### Compare constraint 1 with constraint 2 and return 1 if constraint 1 is greater than      ###
### constraint 2. Return 0 otherwise.                                                        ###
################################################################################################
def consGreater(clst1, wc):
    clst2 = []
    flag = 0
    for c in range(1, len(wc)):
        clst2.append(wc[c])
    clst1_str = ''.join(str(e) for e in clst1)
    clst2_str = ''.join(str(e) for e in clst2)
    if (clst1_str > clst2_str): 
        return 1 
    else: 
        return 0
################################################################################################
### Compare cons1 with each constraint in the list and check if it is greater than any of    ###
### them. If so, return 0 else, return 1.                                                    ###
################################################################################################
def consGreater_lst(clst, wc_mat):
    flag = 1
    for wc in (wc_mat):
        if (consGreater(clst, wc)): 
            flag = 0
            break
    return flag
################################################################################################
def filter_wordConsmatrix(wc_mat):
    filter_wcmat = []
    for wc in (wc_mat):
        cns_lst = []
        for c in range(1, len(wc)):
            cns_lst.append(wc[c])
        if (consGreater_lst(cns_lst, wc_mat)):
            filter_wcmat.append(wc)
    return filter_wcmat
################################################################################################
def typeCons(cons):
    if (len(cons) > 1): 
        return SEQ_CONS
    return INV_CONS
################################################################################################
def checkSndCons(snd, cons):
    val = cons
    if (val < 0):
        val = -val
    if(feature_matrix[snd][val-1] == cons):
        return 1
    else:
        return 0
##################################################################################################
### For each symbol in the word check if it satisfies all of the elements in the invcons list. ### 
### If so return 1. Else 0.                                                                    ###
##################################################################################################
def check_Word_InvC(word, invcons):
    sat = 0
    for snd in (word):
        for cons in range (0, len(invcons)-1):
            sat += checkSndCons(snd, invcons[cons])
    return sat
##################################################################################################
#def check_Word_InvC(word, invcons):
#    for snd in (word):
#        sat = 1
#        for cons in range (0, len(invcons)-1):
#            sat = sat and checkSndCons(snd, invcons[cons])
#        if (sat == 1):
#            return 1
#    if (sat == 1):
#        return 1
#    else: 
#        return 0
##################################################################################################
### Process the sequential constraints into array cons_feat
##################################################################################################
def collect_consfeat (seqcons):
    cons_feat = []
    begin = 1
    for sc in (seqcons): 
        for f in range(0, len(sc)-1):   ## Collect all except last
            if (f == 0) and (sc[f] == 0):
                if (begin == 1):
                    begin = 0
                    cons_feat.append('^')
                else:
                    cons_feat.append('$')
            else:
                begin = 0
                cons_feat.append(sc[f])
    return cons_feat
##################################################################################################
def collect_wordfeat(word, seqcons):
    cfeat = []
    wordfeat = []
    cfeat = collect_consfeat(seqcons)
    for w in word:
        for cs in cfeat:
            if (cs != '^' and cs != '$'):
                wordfeat.append(feature_matrix[w][abs(cs) - 1])
    return wordfeat
##################################################################################################
### Check the number of times a word violates a sequential constraint.                         ###
##################################################################################################
def check_Word_SeqC(word, seqcons):
    match = []
    #match = 0
    cfeat = []
    wfeat = []
    consStr = ""
    wordStr = ""
    cfeat = collect_consfeat(seqcons)
    wfeat = collect_wordfeat(word, seqcons)
    for cf in cfeat:
        consStr += str(cf)
    for wf in wfeat:
        wordStr += str(wf)
    match = re.findall(consStr,wordStr)
    num_mat = len(match)
    return num_mat
##################################################################################################
### Check a word against the constraint lst                                                    ###
##################################################################################################
def check_wordConslst (word):
    wordCons_lst = []
    wordCons_lst.append(word)
    for cons in (constraint_matrix):
        if (typeCons(cons) == INV_CONS):
            result = check_Word_InvC(word, cons[0])
        elif (typeCons(cons) == SEQ_CONS):
            result = check_Word_SeqC(word, cons)
        wordCons_lst.append(result)
    return wordCons_lst
##################################################################################################
### Check a word against the constraint lst                                                    ###
##################################################################################################
def check_wordlst():
    for w in (word_lst):
        #wordCons_lst = []
        wordCons_lst = check_wordConslst(w)
        wordCons_matrix.append(wordCons_lst)
    return wordCons_matrix
##################################################################################################
### Generate 100 words pass them through constraint list. If the ##
### the valid flag = 1 then remove  words from the word list     ##
### that satisfy EVEN ONE inventory constraint. Update the       ##
### number of valid words found and continue until we find       ##
### lexicon size words. If valid flag == 0 then proceed without  ##
### discarding any words.                                         ##
###################################################################
def valid_word(wcm, num):
    for c in range(1, num+1):
        if (wcm[c] == 1):
            return 0
    return 1
###################################################################
def remove_words(wc_mat,numInvCons):
    upd_wcm = []
    for wc in wc_mat: 
        if valid_word(wc, numInvCons):
            upd_wcm.append(wc)
    return upd_wcm
###################################################################
def mk_str(wc, start):
    genstr = ""
    for i in range(1, len(wc)):
        genstr += str(wc[i])
    return genstr
###################################################################
def genrwCons_mat(wcm):
    nwcm = []
    for i in range(0, len(wcm)): 
        wc1 = wcm[i] 
        w1 = wc1[0] 
        val1 = mk_str(wc1, 1) 
        flag = 0
        for j in range(i, len(wcm)):
            val2 = mk_str(wcm[j],1)
            if (val1 > val2):
                flag = 1
        if (flag == 0): ## Did not find any smaller; so add to output
            nwcm.append(wcm[i])
    return nwcm
##############################################################################################
### Function that generates words along with their constraint list violations.             ###
##############################################################################################
def genWords_Cons(val_flag):
    ### Process the features
    num_vwords = 0
    vwc_mat = []
    owc_mat = []
    tmp_wc = []
    proc_feat()

    ### Process the constraints
    constraint_matrix = proc_Constr()
    if (val_flag == 1):                           ### If only valid words are to be generated
        while (num_vwords < VLEX_SIZE): 
            genNumwords(LEX_SIZE, word_lst) 
            wordCons_matrix = check_wordlst()     ### Check the words and create this matrix
            tmpwc = remove_words(wordCons_matrix, numInvCons)   ### 
            if (len(tmpwc)): 
                vwc_mat = []
                for wc in (tmpwc):
                    if wc not in owc_mat: 
                        vwc_mat.append(wc)
                if (len(vwc_mat)): 
                        owc_mat += vwc_mat 
                        num_vwords += len(vwc_mat)
                        print num_vwords
        wordCons_matrix = owc_mat
    if (val_flag == 2):    ### Rank the constraints
        wordCons_matrix - check_wordlst()
        nwCons_mat = genrwCons_mat(wordCons_matrix)
        wordCons_matrix = nwCons_mat
    if (val_flag == 0):
        genNumwords(LEX_SIZE, word_lst) 
        wordCons_matrix = check_wordlst()
    return wordCons_matrix
###############################################################################################
#### Main Function                                                                          ###
##############################################################################################
def genCWordsandPrint(): 
    val_flag = 0
    ## Set valid words flag 
    wordCons_matrix = genWords_Cons(val_flag) 
    filter_wcmat = filter_wordConsmatrix(wordCons_matrix)
    
    ## Get the words and constraint satisfaction matrix
    if (val_flag == 1): 
        outf = open("FilterVWordCons", "wb") 
    if (val_flag == 2):
        outf = open("RVWordCons", "wb") 
    if (val_flag == 0):
        outf1 = open("UnfilterWordCons", "wb") 
        outf = open("FilterWordCons", "wb") 
    outStr = ""
    whead = "Word"
    chead = "Constraint Evaluations"
    OutStr = whead.ljust(20)                        
    ##Headers for the output file
    OutStr += chead
    outf.write(OutStr);
    outf1.write(OutStr);
    outf.write("\n\n")
    outf1.write("\n\n")
    for wcm in (wordCons_matrix):
          outf1.write("%s\n" % wcm)
    for wc in (filter_wcmat):
        outStr = ""
        outStr += numword_to_sndword(wc[0]).ljust(20)
        for c in range(1, len(wc)):
            outStr += str(wc[c])
        outf.write(outStr.encode("UTF-8"))
        outf.write("\n\n")
    outf.close()
    outf1.close()

## Call the main function to run the program
genCWordsandPrint()