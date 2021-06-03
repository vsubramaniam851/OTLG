def CandEval(y, Constraints):
    Cand = list(y)
    # splitting String y into a list of characters
    # Setting all constraint violation variables to 0.
    #All Constraints that will evaluate the candidate. These are their functions.
    def AlignR(x):
        ALIGNR = 0
        if x[len(x) - 1] != 'A':
            for i in range(0, len(x)):
                if x[i] == 'A':
                    differenceR = (len(x) - 1) - i
                    ALIGNR = ALIGNR + differenceR
        return ALIGNR

    def AlignL(x):
        ALIGNL = 0
        if x[0] != 'A':
            for i in range(0, len(x)):
                if x[i] == 'A':
                    differenceL = i - 0
                    ALIGNL = ALIGNL + differenceL
        return ALIGNL

    def LapseR(x):
        LAPSER = 0
        if x[len(x) - 1] != 'A' and x[len(x) - 2] != 'A':
            LAPSER = LAPSER + 1
        return LAPSER

    def LapseL(x):
        LAPSEL = 0
        if x[0] != 'A' and x[1] != 'A':
            LAPSEL = LAPSEL + 1
        return LAPSEL

    def ExtLapseL(x):
        EXTLAPSEL = 0
        if x[0] != 'A' and x[1] != 'A' and x[2] != 'A':
            EXTLAPSEL = EXTLAPSEL + 1
        return EXTLAPSEL

    def ExtLapseR(x):
        EXTLAPSER = 0
        if x[len(x) - 1] != 'A' and x[len(x) - 2] != 'A' and x[len(x) - 3] != 'A':
            EXTLAPSER = EXTLAPSER + 1
        return EXTLAPSER

    def Lapse(x):
        LAPSE = 0
        for i in range(0, len(x) - 1):
            if x[i] != 'A' and x[i + 1] != 'A':
                LAPSE = LAPSE + 1
        return LAPSE

    def ExtLapse(x):
        EXTLAPSE = 0
        for i in range(0, len(x) - 2):
            if x[i] != 'A' and x[i + 1] != 'A' and x[i + 2] != 'A':
                EXTLAPSE = EXTLAPSE + 1
        return EXTLAPSE

    def Nonfinality(x):
        NONFINALITY = 0
        if x[len(x) - 1] == 'A':
            NONFINALITY = NONFINALITY + 1
        return NONFINALITY

    # Evaluation of the candidate. First going to check if the candidate is a two syllable word.
    if len(Cand) == 2:
        AL = AlignL(Cand)
        AR = AlignR(Cand)
        NF = Nonfinality(Cand)
        #The following lines of code will resort the list of evaluations so that it fulfills the ranking. This is why
        #the constraints were passed in.
        v = []
        for i in range(0, len(Constraints)):
            if Constraints[i] == "AlignL":
                v.append(AL)
            if Constraints[i] == "AlignR":
                v.append(AR)
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
        #print v
        x = map(str, v)
        x = ''.join(x)
        x = int(x)
        return x

    else:
        #If candidate is a 3 syllable word or over, go here.
        AR = AlignR(Cand)
        AL = AlignL(Cand)
        LL = LapseL(Cand)
        LR = LapseR(Cand)
        EXTL = ExtLapseL(Cand)
        EXTR = ExtLapseR(Cand)
        L = Lapse(Cand)
        EXT = ExtLapse(Cand)
        NF = Nonfinality(Cand)
        v = []
        #Same process as above. Here, for all words more than three syllables, the process is repeated and the list is
        #resorted to fit the ranking.
        for i in range(0, len(Constraints)):
            if Constraints[i] == "AlignL":
                v.append(AL)
            elif Constraints[i] == "AlignR":
                v.append(AR)
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
        #print v
        x = map(str, v)
        x = ''.join(x)
        x = int(x)
        return x