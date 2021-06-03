import CandEval
import Comparison
def OTLGGen(constraints,candidate):
    #Main function where everything is happening
    CandidateEvaluation1 = {}
    #Empty Dictionary which will hold each candidate as a key and its evaluation as its value.
    #A file of candidates is opened. This file can only contain words of a certain syllable length.
    file = open(candidate, "r")
    x = file.readlines()
    #File of candidates is opened and inspected. Each line is read and placed in a list.
    for i in range(0, len(x)):
        x[i] = x[i].replace('\n', '')
        #Each candidate has the ending part removed.
    file.close()
    #Close the file to open a new file. This holds all the constraints
    #This repeated with the constraints file. This file is opened and inspected. The lines are read and placed
    #in a list.
    file2 = open(constraints, "r")
    constraints1 = file2.readlines()
    for i in range(0, len(constraints1)):
        constraints1[i] = constraints1[i].replace('\n', '')
        #Once again, the ending is removed to clean up the constraints.
    file2.close()

    RankedConstraints = []
    #New holder of constraints, just for clarity
    for i in range(0, len(constraints1)):
        RankedConstraints.append(constraints1[i])

    for i in range(0, len(x)):
        #Evaluation of Candidates
        CandidateEvaluation1[x[i]]= CandEval.CandEval(x[i], RankedConstraints)

    #Finished comparison and picks best candidate
    j = Comparison.CandComparison(CandidateEvaluation1)

    CandidateEvaluation2 = {}
    for key,value in CandidateEvaluation1.iteritems():
        #Shifting keys and values to a new dictionary.
        #This time, make the value into a list of digits. This represents the violation vector in list form.
        #This is done so that it is easy to know the number of "*" to put for the candidate.
        CandidateEvaluation2[key] = [int(d) for d in str(value)]

    for key,value in CandidateEvaluation2.iteritems():
        #This will print the evaluation of each candidate using * and !.
        #If a candidate violates any constraint once, it will put a *. If it violates it 3 times, ***, etc.
        #It will take the list of digits and print * for each index of the list.
        print(key),
        for i in range(0, len(value)):
            for k in range(0, value[i]):
                print("* "),
            if key != j[0] and i == 0:
                #If this candidate is not the winner and this is the highest constraint this candidate violates
                #put a ! to indicate that this is a FATAL VIOLATION.
                print("! "),
        print "\t",

    #print CandidateEvaluation1
    return j[0]