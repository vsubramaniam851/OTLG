import OTLGRunner
import codecs
import csv
#Main area where code is called and run.
#For each word of a certain syllable length the code is called.
Result2 = OTLGRunner.OTLGGen("AllConstraints", "Candidate2")
#First, the code is called on the file with all candidates and on the file with the constraints.
#print(OTLGRunner.evalList)
"""for i in range(0, len(Result2[1])):
    #print(Result2[1][i])"""
#print('\033[1m' + "\t\t" + Result2[0] + '\033[0m')
#Then the result is printed with the evaluation of each candidate and the best candidate in bold and tabbed twice
#to the right to differentiate it.
Result3 = OTLGRunner.OTLGGen("AllConstraints", "Candidate3")
#Repeated for 3 syllables, 4 syllable, so on...
"""for i in range(0, len(Result3[1])):
    #print(Result3[1][i])
print('\033[1m' + "\t\t" + Result3[0] + '\033[0m')"""
Result4 = OTLGRunner.OTLGGen("AllConstraints", "Candidate4")
"""for i in range(0, len(Result4[1])):
    print(Result4[1][i])
print('\033[1m' + "\t\t" + Result4[0] + '\033[0m')"""
Result5 = OTLGRunner.OTLGGen("AllConstraints", "Candidate5")
"""for i in range(0, len(Result5[1])):
    print(Result5[1][i])
print('\033[1m' + "\t\t" + Result5[0] + '\033[0m')"""
Result6 = OTLGRunner.OTLGGen("AllConstraints", "Candidate6")
"""for i in range(0, len(Result6[1])):
    print(Result6[1][i])
print('\033[1m' + "\t\t" + Result6[0] + '\033[0m')"""
Result7 = OTLGRunner.OTLGGen("AllConstraints", "Candidate7")
"""for i in range(0, len(Result7[1])):
    print(Result7[1][i])
print('\033[1m' + "\t\t" + Result7[0] + '\033[0m')"""
Result8 = OTLGRunner.OTLGGen("AllConstraints", "Candidate8")
"""for i in range(0, len(Result8[1])):
    print(Result8[1][i])
print('\033[1m' + "\t\t" + Result8[0] + '\033[0m')"""
#Result9 = OTLGRunner.OTLGGen("AllConstraints", "Candidate9")
#print '\033[1m' + "\t\t" + Result9[0] + '\033[0m'
#Result10 = OTLGRunner.OTLGGen("AllConstraints", "Candidate10")
#print '\033[1m' + "\t\t" + Result10 + '\033[0m'


file = open('OutputFile.txt', 'w')
file.write("\tAlignL1\t AlignR1\t NonFinality\t ExtLapseL\t Clash\t AlignR2\t AlignL2\t AlignEdges\t ExtLapse\t Lapse\t ExtLapseR\t LapseL\t LapseR\n")
for i in range(0, len(Result2[1])):
    file.write(Result2[1][i] + "\n")
for i in range(0, len(Result3[1])):
    file.write(Result3[1][i] + "\n")
for i in range(0, len(Result4[1])):
    file.write(Result4[1][i] + "\n")
for i in range(0, len(Result5[1])):
    file.write(Result5[1][i] + "\n")
for i in range(0, len(Result6[1])):
    file.write(Result6[1][i] + "\n")
for i in range(0, len(Result7[1])):
    file.write(Result7[1][i] + "\n")
for i in range(0, len(Result8[1])):
    file.write(Result8[1][i] + "\n")
file.close()


"""file1 = open('OutputFile.txt', 'r')
content = file1.readlines()
with open('OutputTableux.csv', mode = 'w') as Output:
    Output_Writer = csv.writer(Output, delimiter = ',')
    for i in range(0, len(content) - 1):
        print (content[i])
        #Output_Writer.writerow(content[i])"""



