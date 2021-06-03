import OTLGRunner
#Main area where code is called and run.
#For each word of a certain syllable length the code is called.
Result2 = OTLGRunner.OTLGGen("AllConstraints", "Candidate2")
#First, the code is called on the file with all candidates and on the file with the constraints.
print '\033[1m' + "\t\t" + Result2 + '\033[0m'
#Then the result is printed with the evaluation of each candidate and the best candidate in bold and tabbed twice
#to the right to differentiate it.
Result3 = OTLGRunner.OTLGGen("AllConstraints", "Candidate3")
#Repeated for 3 syllables, 4 syllable, so on...
print '\033[1m' + "\t\t" + Result3 + '\033[0m'
Result4 = OTLGRunner.OTLGGen("AllConstraints", "Candidate4")
print '\033[1m' + "\t\t" + Result4 + '\033[0m'
Result5 = OTLGRunner.OTLGGen("AllConstraints", "Candidate5")
print '\033[1m' + "\t\t" + Result5 + '\033[0m'
Result6 = OTLGRunner.OTLGGen("AllConstraints", "Candidate6")
print '\033[1m' + "\t\t" + Result6 + '\033[0m'
Result7 = OTLGRunner.OTLGGen("AllConstraints", "Candidate7")
print '\033[1m' + "\t\t" + Result7 + '\033[0m'
Result8 = OTLGRunner.OTLGGen("AllConstraints", "Candidate8")
print '\033[1m' + "\t\t" + Result8 + '\033[0m'
#Result9 = OTLGRunner.OTLGGen("AllConstraints", "Candidate9")
#print '\033[1m' + "\t\t" + Result9 + '\033[0m'
#Result10 = OTLGRunner.OTLGGen("AllConstraints", "Candidate10")
#print '\033[1m' + "\t\t" + Result10 + '\033[0m'