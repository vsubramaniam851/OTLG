###############################################################################################
### Process the randomly chosen constraints and store them into lists:                      ###
###      1. invCons_lst: a list of inventory constraints                                    ###
###      2. a list of sequence constraints                                                  ###
###############################################################################################
import codecs
import sys
import random
import re
from const import *
from helpers import *

Consfile   = "MarkednessCons.txt"
constraint_matrix = []
numInvCons = 0                   ### Number of inventory constraints

#############################################################################################
### Pre-process constraint and determine its type                                         ###
#############################################################################################
def setConstyp(cons_str):
    tcons = 0
    match = 0
    cons_lst = []
    if (re.findall(">", cons_str)):            ### Process a greater than constraint
        tmp_lst = cons_str.split(">") 
        cons_str = tmp_lst[0]
        tcons = tmp_lst[1]                     ### The number of times to violate the constraint
        tmp_lst = cons_str.split(":") 
        cons_str = tmp_lst[0]
        cons_lst.append(cons_str)
        cons_lst.append(tcons)
    elif (re.findall("NOT", cons_str)):        ### Process the negation constraint
        tcons = -1
        tmp_lst = cons_str.split("NOT(")
        cons_str = tmp_lst[1]
        tmp_lst = cons_str.split(")")
        cons_str = tmp_lst[0]
        tmp_lst = cons_str.split(";")
        cons_str = ""
        for t in (tmp_lst):
            cons_str = cons_str + "," + tmp_lst[t]
        cons_lst.append(cons_str)
        cons_lst.append(tcons)
    else:                                      ### Process a regular constraint
        cons_lst.append(cons_str)
        cons_lst.append(tcons)
    return cons_lst
##############################################################################################
### Process the constraints and store the result into constraint_matrix                    ###
##############################################################################################
def proc_Constr():
    lines = []
    one_constraint = []
    seq_constraint = []
    consf = open(Consfile, "r")
    lines = consf.readlines()
    ### Process lines1###########################################################################
    for i in range(0, len(lines)):         
        cons_lst = []
        seq_constraint = []
        cline = lines[i].replace('\n','')
        tmp_lst = cline.split("*")
        tmpcons = tmp_lst[1]
        tmp_lst = tmpcons.split("::")
        tmpcons = tmp_lst[0]
        tmp_lst = tmpcons.split("]")
        outer_lst = []
        for j in range(0, len(tmp_lst) -1):
            outer_lst.append(tmp_lst[j].split("[")[1])
        for c in range(0, len(outer_lst)):
            one_constraint = []
            cons_lst = setConstyp(outer_lst[c])
            consf = cons_lst[0]
            ctyp = cons_lst[1]
            feat_lst = consf.split(",")    
            for f in range (0, len(feat_lst)): 
                consf = get_feature(feat_lst[f])
                one_constraint.append(consf)
            one_constraint.append(ctyp)                  ## Append the last element to indicate type of constraint
            seq_constraint.append(one_constraint)
        constraint_matrix.append(seq_constraint)
    print constraint_matrix
    return constraint_matrix
#############################################################################################
#proc_Constr()