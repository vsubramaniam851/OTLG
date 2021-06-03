def CandComparison(s):
    #Takes dictionary of candidate/evaluation integer and finds the minimum.
    #Once this is found, it returns the list with the the word and corresponding lowest integer.
    s.items()
    x = min(s.items(), key=lambda x: x[1])
    return x