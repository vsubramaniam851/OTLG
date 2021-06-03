def CandEval(y, Constraints):
    Cand = list(y)
    # splitting String y into a list of characters
    # Setting all constraint violation variables to 0.
    #All Constraints that will evaluate the candidate. These are their functions.
    def AlignR1(x):
        ALIGNR = 0
        if x[len(x) - 1] != 'A':
            for i in range(0, len(x)):
                if x[i] == 'A':
                    differenceR = (len(x) - 1) - i
                    ALIGNR = ALIGNR + differenceR
        if x[len(x) - 1] != 'o':
            for i in range(0, len(x)):
                if x[i] == 'o':
                    differenceR1 = (len(x) - 1) - i
                    ALIGNR = ALIGNR + differenceR1
        return ALIGNR

    def AlignL1(x):
        ALIGNL = 0
        if x[0] != 'A':
            for i in range(0, len(x)):
                if x[i] == 'A':
                    differenceL = i - 0
                    ALIGNL = ALIGNL + differenceL
        if x[0] != 'o':
            for i in range(0, len(x)):
                if x[i] == 'o':
                    differenceL1 = i - 0
                    ALIGNL = ALIGNL + differenceL1
        return ALIGNL

    def AlignEdges(x):
        EDGE = 0
        if x[0] != 'A' or x[0] != 'o':
            EDGE = EDGE + 1
        if x[len(x) - 1] != 'A' or x[len(x) - 1] != 'o':
            EDGE = EDGE + 1
        return EDGE

    def AlignR2(x):
        ALIGNR2 = 0
        if x[len(x) - 1] != 'A':
            for i in range(0, len(x)):
                if x[i] == 'o':
                    ALIGNR2 = ALIGNR2 + 1
        return ALIGNR2

    def AlignL2(x):
        ALIGNL2 = 0
        if x[0] != 'A':
            for i in range(0, len(x)):
                if x[i] == 'o':
                    ALIGNL2 = ALIGNL2 + 1
        return ALIGNL2

    def LapseR(x):
        LAPSER = 0
        if (x[len(x) - 1] != 'A' and x[len(x) - 1] != 'o') and (x[len(x) - 2] != 'A' and x[len(x) - 2] != 'o'):
            LAPSER = LAPSER + 1
        return LAPSER

    def LapseL(x):
        LAPSEL = 0
        if (x[0] != 'A' and x[0] != 'o') and (x[1] != 'A' and x[1] != 'o'):
            LAPSEL = LAPSEL + 1
        return LAPSEL

    def ExtLapseL(x):
        EXTLAPSEL = 0
        if (x[0] != 'A' and x[0] != 'o') and (x[1] != 'A' and x[1] != 'o') and (x[2] != 'A' and x[2] != 'o'):
            EXTLAPSEL = EXTLAPSEL + 1
        return EXTLAPSEL

    def ExtLapseR(x):
        EXTLAPSER = 0
        if (x[len(x) - 1] != 'A' and x[len(x) - 1] != 'o') and (x[len(x) - 2] != 'A' and x[len(x) - 2] != 'o') and (x[len(x) - 3] != 'A' and x[len(x) - 3] != 'o'):
            EXTLAPSER = EXTLAPSER + 1
        return EXTLAPSER

    def Lapse(x):
        LAPSE = 0
        for i in range(0, len(x) - 1):
            if (x[i] != 'A' and x[i] != 'o') and (x[i + 1] != 'A' and x[i+1] != 'o'):
                LAPSE = LAPSE + 1
        return LAPSE

    def ExtLapse(x):
        EXTLAPSE = 0
        for i in range(0, len(x) - 2):
            if (x[i] != 'A' and x[i] != 'o') and (x[i + 1] != 'A' and x[i+1] != 'o') and (x[i + 2] != 'A' and x[i+2] != 'o'):
                EXTLAPSE = EXTLAPSE + 1
        return EXTLAPSE

    def Nonfinality(x):
        NONFINALITY = 0
        if x[len(x) - 1] == 'A':
            NONFINALITY = NONFINALITY + 1
        return NONFINALITY

    def clash(x):
        CLASH = 0
        for i in range(0, len(x)-1):
            if x[i] == 'A' and x[i+1] == 'o':
                CLASH = CLASH + 1
        for i in range(0, len(x)-1):
            if x[i] == 'o' and x[i+1] == 'o':
                CLASH = CLASH + 1
        return CLASH
    # Evaluation of the candidate. First going to check if the candidate is a two syllable word.
    if len(Cand) == 2:
        AL1 = AlignL1(Cand)
        AR1 = AlignR1(Cand)
        NF = Nonfinality(Cand)
        CL = clash(Cand)
        v = []
        #The following lines of code will resort the list of evaluations so that it fulfills the ranking. This is why
        #the constraints were passed in.
        for i in range(0, len(Constraints)):
            if Constraints[i] == "AlignL1":
                v.append(AL1)
            if Constraints[i] == "AlignR1":
                v.append(AR1)
            if Constraints[i] == "AlignEdges":
                v.append(0)
            if Constraints[i] == "Clash":
                v.append(CL)
            if Constraints[i] == "LapseR":
                v.append(0)
            if Constraints[i] == "LapseL":
                v.append(0)
            if Constraints[i] == "ExtLapseL":
                v.append(0)
            if Constraints[i] == "ExtLapseR":
                v.append(0)
            if Constraints[i] == "Lapse":
                v.append(0)
            if Constraints[i] == "ExtLapse":
                v.append(0)
            if Constraints[i] == "NonFinality":
                v.append(NF)
            if Constraints[i] == "AlignR2":
                v.append(0)
            if Constraints[i] == "AlignL2":
                v.append(0)
        #print(Cand)
        #x = map(str, v)
        #x = ''.join(x)
        #x = int(x)
        #print(x)
        return v
    else:
        #If candidate is a 3 syllable word or over, go here.
        AR1 = AlignR1(Cand)
        AL = AlignL1(Cand)
        LL = LapseL(Cand)
        LR = LapseR(Cand)
        EXTL = ExtLapseL(Cand)
        EXTR = ExtLapseR(Cand)
        L = Lapse(Cand)
        EXT = ExtLapse(Cand)
        NF = Nonfinality(Cand)
        AE = AlignEdges(Cand)
        CL = clash(Cand)
        AR2 = AlignR2(Cand)
        AL2 = AlignL2(Cand)
        v = []
        #Same process as above. Here, for all words more than three syllables, the process is repeated and the list is
        #resorted to fit the ranking.
        for i in range(0, len(Constraints)):
            if Constraints[i] == "AlignL1":
                v.append(AL)
            elif Constraints[i] == "AlignR1":
                v.append(AR1)
            elif Constraints[i] == "AlignEdges":
                v.append(AE)
            elif Constraints[i] == "LapseR":
                v.append(LR)
            elif Constraints[i] == "LapseL":
                v.append(LL)
            elif Constraints[i] == "ExtLapseL":
                v.append(EXTL)
            elif Constraints[i] == "ExtLapseR":
                v.append(EXTR)
            elif Constraints[i] == "Lapse":
                v.append(L)
            elif Constraints[i] == "ExtLapse":
                v.append(EXT)
            elif Constraints[i] == "NonFinality":
                v.append(NF)
            elif Constraints[i] == "Clash":
                v.append(CL)
            elif Constraints[i] == "AlignR2":
                v.append(AR2)
            elif Constraints[i] == "AlignL2":
                v.append(AL2)
        #print(Cand)
        #x = map(str, v)
        #x = ''.join(x)
        #x = int(x)
        #print(v)
        return v
def IntEval(y, Constraints):
    v = CandEval(y, Constraints)
    x = map(str, v)
    x = ''.join(x)
    x = int(x)
    #print(x)
    return x





