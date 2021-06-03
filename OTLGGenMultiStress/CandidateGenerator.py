def CandGen(word):
    wordList = list(word)
    newWord = list(wordList)
    CandList = []
    for i in range(0, len(wordList)):
        wordList[i] = 'A'
        newWord1 = list(wordList)
        for j in range(0, len(wordList)):
            if i != j:
                wordList[j] = 'o'
                CandList.append("".join(wordList))
                wordList = list(newWord1)
        wordList = list(newWord)
    return CandList

f2 = open("Candidate2", "w+")
List2 = CandGen("aa")
for i in range(0, len(List2)):
    f2.write(List2[i] + "\n")
f2.close()

f3 = open("Candidate3", "w+")
List3 = CandGen("aaa")
for i in range(0, len(List3)):
    f3.write(List3[i] + "\n")
f3.close()

f4 = open("Candidate4", "w+")
List4 = CandGen("aaaa")
for i in range(0, len(List4)):
    f4.write(List4[i] + "\n")
f4.close()

f5 = open("Candidate5", "w+")
List5 = CandGen("aaaaa")
for i in range(0, len(List5)):
    f5.write(List5[i] + "\n")
f5.close()

f6= open("Candidate6", "w+")
List6 = CandGen("aaaaaa")
for i in range(0, len(List6)):
    f6.write(List6[i] + "\n")
f6.close()

f7 = open("Candidate7", "w+")
List7 = CandGen("aaaaaaa")
for i in range(0, len(List7)):
    f7.write(List7[i] + "\n")
f7.close()

f8 = open("Candidate8", "w+")
List8 = CandGen("aaaaaaaa")
for i in range(0, len(List8)):
    f8.write(List8[i] + "\n")
f8.close()

f9 = open("Candidate9", "w+")
List9 = CandGen("aaaaaaaaa")
for i in range(0, len(List9)):
    f9.write(List9[i] + "\n")
f9.close()

f10 = open("Candidate10", "w+")
List10 = CandGen("aaaaaaaaaa")
for i in range(0, len(List10)):
    f10.write(List10[i] + "\n")
f10.close()

