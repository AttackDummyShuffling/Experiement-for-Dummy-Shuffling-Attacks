

#-------------------Anlysis----------------------#
def TransMatrix(Matrix):

    traceNum = len(Matrix)
    t = len(Matrix[0])
    
    NewMatrix = []
    
    for i in range(t):
        NewMatrix.append([])
        for j in range(traceNum):
            NewMatrix[i].append(Matrix[j][i])
    return NewMatrix

def ComScore(Array1, Array2):

    Score = 0
    for i in range(len(Array1)):
        if Array1[i] == Array2[i]:
            Score = Score + 1

    return Score
#------------------------------------------------#

def GenRandoms(Num, Size):
    import random
    Array = []
    for i in range(Num):
        Array.append(random.randint(0, (1 << Size) - 1))

    return Array
    
#------------------------------------------------#
# binArray[0] is the msb
def HextoBin(Hex):
    
    binArray = []
    for i in range(8):
        binArray.append((Hex >> (7-i) ) & 1)

    return binArray

# binArray[0] is the msb
def BintoHex(binArray):
    Hex = 0
    for i in range(8):
        Hex += ( binArray[i] << (7-i))

    return Hex
#------------------------------------------------#   

#-------------------GenKeys----------------------#
def GenRounKeys(RoundNum):
    K = []
    for i in range(RoundNum):
        Ki = GenRandoms(16,8)
        for j in range(16):
            Ki[j] = HextoBin(Ki[j])

        K.append(Ki)

    return K
#------------------------------------------------#