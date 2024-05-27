from TraceCollection_BasicDS import *
from SuccessRate import *
from AnlysisTool import *

import sys
import matplotlib.pyplot as plt

import time
#Nt = int(sys.argv[1])

#outfileName = "Result" + str(Nt) + ".txt"
#print("Nt is: ", Nt)

#Ns = 32
#K = 256
#t = 11632
#
#Loci = 3 # Recover Loci byte of the first secret round key

#RoundNum = 3
## determine t (the number of nodes in a trace)
#P = []
#K = GenRounKeys(RoundNum)
#traceArray = collectTrace(P,K,1)
#t = len(traceArray[0])
#
#print(t)

#----------------------------------------------AES Sbox----------------------------------------------#
Sbox = [
0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
#----------------------------------------------------------------------------------------------------#



#-------------------------------------------------------------#

# i is the i-th key byte to recovery
# KArray[RoundNum][16][8]: each element is binary
# Nt: trace number
# return is the possible Loci-th key byte
#Nt = 400

def Exp(Nt, K, Loci, c, Ns):

    CommandPair = []
    
    # collect traceArray[Nt][t]: binary
    # After collection PArray[Nt][16][8]
    PArray = []
    traceArray = CollectTrace_SurperSbox(PArray, K, Nt, Ns)
#    traceArray = collectTrace(PArray, KArray, Nt)
    
    startime = time.time()
    t = len(traceArray[0])
    VecSet = TransMatrix(traceArray) # VecSet[t][Nt], VecSet[i] 
                                     # is the i-th node of Nt trace


    # Generate predictable value array
    PiArray = []
    for i in range(Nt):
        Pi = BintoHex(PArray[i][Loci])
        PiArray.append(Pi)

    
#    ScoreArray = []
    
    MaxScore = 0
    Recovered_Lock = 0
    for Guessk in range(256):
#        print(Guessk)
#        ScoreArray.append([])
#        print("Guess key: ", Guessk)
    # predicted node: lsb of the Loci-th byte after S-box operation
        PreArray = []
        for i in range(Nt):
            PreArray.append(Sbox[PiArray[i] ^ Guessk] & 1)

        # Compute Score(PreArray, VecSet[i])
        for i in range(t):
        
            Score = ComScore(PreArray, VecSet[i])
            
            if Score > c:

                CommandPair.append([Guessk, i])
            
            
#            ScoreArray[Guessk].append(Score)
#            if Score > MaxScore:
#                MaxScore = Score
#                Recovered_Lock = Guessk
    endtime = time.time()
    return [CommandPair, endtime - startime]

def IsRightPair(KArray, CommandPair, Loci):
    RightKey = BintoHex(KArray[Loci])
    
    NumRightPair = 0
    NumRightKey = 0
    
    if [RightKey, 615] in CommandPair:
#        NumRightPair = 1
        NumRightKey += 1
    if [RightKey, 1342] in CommandPair:
        NumRightKey += 1
    if [RightKey, 2069] in CommandPair:
        NumRightKey += 1
    if [RightKey, 2796] in CommandPair:
        NumRightKey += 1

    if NumRightKey > 0:
        NumRightPair = 1
    
    return [NumRightPair, len(CommandPair) - NumRightKey]
        
    


#KArray = [ [[0, 1, 1, 1, 0, 0, 1, 1]]]
#RecK = 113
#print(IsRightKey( KArray, RecK, 0) + 0)
#print("Success Rate: ", ComputeSuccessRate(Ns, t, 256, 400))
#print(Exp(Nt, KArray, 15))
#print(KArray[0][15])


#-------------------------------------------------------------#

def PrintToFile(command, fileName):
    import sys
    file = open(fileName, 'a')
    old = sys.stdout
    sys.stdout = file

    print(command)

    sys.stdout = old  
    file.close()

def ClearFile(fileName):
    import sys
    file = open(fileName, 'w')
    old = sys.stdout
    sys.stdout = file

    print("", end = "",sep = "")

    sys.stdout = old  
    file.close()


#--------------------- Plot the Scores ---------------------#

def Plot(Nt, K, Loci):


    # collect traceArray[Nt][t]: binary
    # After collection PArray[Nt][16][8]
    PArray = []
    traceArray = CollectTrace_SurperSbox(PArray, K, Nt)
#    traceArray = collectTrace(PArray, KArray, Nt)
    t = len(traceArray[0])
    VecSet = TransMatrix(traceArray) # VecSet[t][Nt], VecSet[i] 
                                     # is the i-th node of Nt trace


    # Generate predictable value array
    PiArray = []
    for i in range(Nt):
        Pi = BintoHex(PArray[i][Loci])
        PiArray.append(Pi)


    ScoreArray = []
    
    MaxScore = 0
    Recovered_Lock = 0
    for Guessk in range(256):
        print(Guessk)
        ScoreArray.append([])
#        print("Guess key: ", Guessk)
    # predicted node: lsb of the Loci-th byte after S-box operation
        PreArray = []
        for i in range(Nt):
            PreArray.append(Sbox[PiArray[i] ^ Guessk] & 1)

        # Compute Score(PreArray, VecSet[i])
        for i in range(t):
        
            Score = ComScore(PreArray, VecSet[i])
            
            ScoreArray[Guessk].append(Score)
            if Score > MaxScore:
                MaxScore = Score
                Recovered_Lock = Guessk

    ScoreArray = TransMatrix(ScoreArray)
    
    MaxWrongScore = []
    RightScore = []
    for node in range(t):
        
        RightScore.append(ScoreArray[node][Recovered_Lock])
        
        MWSi = 0
        for key in range(256):
            if (ScoreArray[node][key] > MWSi) & (key != Recovered_Lock):
                MWSi = ScoreArray[node][key]

        MaxWrongScore.append(MWSi)
    
    x = []
    for i in range(t):
        x.append(i)
#        RightScore[i] = MaxWrongScore[i] - Nt/2
#        MaxWrongScore[i] = MaxWrongScore[i] - Nt/2
#        if MaxWrongScore[i] < 0:
#            MaxWrongScore[i] = 0


    plt.plot(x, MaxWrongScore, color = "gray")

    plt.plot(x, RightScore, color = "blue")

    plt.savefig('RatePlot.png')
    plt.close()

#    PrintToFile(command, fileName)
#    fileName = "ScoreData.py"
    PrintToFile(str(MaxWrongScore), "MaxWrongScore.py")
    PrintToFile(str(RightScore), "RightScore.py")
    PrintToFile(str(ScoreArray), "ScoreArray.py")
    

#Nt = int(sys.argv[1])
#c = int(sys.argv[2])
#K = GenKey()
#print(K)
#Loci = 3
#Ns = int(sys.argv[3])

Ns = int(sys.argv[1])   # slot number in attacked dummy shuffling
Loci = int(sys.argv[2]) # recovery loci-th Sbox
Nt = int(sys.argv[3])   # data complexity
c = int(sys.argv[4])    # threshold value


K = GenKey() 
print("the key used in the encryption is:", K)


[key,time] = Exp(Nt, K, Loci, c, Ns)
print("recovered key:", key)
print("attack time:", time)
    


