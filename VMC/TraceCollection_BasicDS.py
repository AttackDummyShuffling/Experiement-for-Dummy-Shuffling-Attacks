import hashlib
import random
from AnlysisTool import *

def addroudkey(U, K, trace):  #U[8],K[8]
    s = [0]*8
    for i in range(8):
        s[i] = U[i] ^ K[i]
        trace.append(s[i])
    return s
def sbox(U, r, trace):  #U[8]
    s = [0]*8
    y14 = U[3] ^ U[5]
    trace.append(y14)
    y13 = U[0] ^ U[6]
    trace.append(y13)
    y9 = U[0] ^ U[3]
    trace.append(y9)
    y8 = U[0] ^ U[5]
    trace.append(y8)
    t0 = U[1] ^ U[2]
    trace.append(t0)
    y1 = t0 ^ U[7]
    trace.append(y1)
    y4 = y1 ^ U[3]
    trace.append(y4)
    y12 = y13 ^ y14
    trace.append(y12)
    y2 = y1 ^ U[0]
    trace.append(y2)
    y5 = y1 ^ U[6]
    trace.append(y5)
    y3 = y5 ^ y8
    trace.append(y3)
    t1 = U[4] ^ y12
    trace.append(t1)
    y15 = t1 ^ U[5]
    trace.append(y15)
    y20 = t1 ^ U[1]
    trace.append(y20)
    y6 = y15 ^ U[7]
    trace.append(y6)
    y10 = y15 ^ t0
    trace.append(y10)
    y11 = y20 ^ y9
    trace.append(y11)
    y7 = U[7] ^ y11
    trace.append(y7)
    y17 = y10 ^ y11
    trace.append(y17)
    y19 = y10 ^ y8
    trace.append(y19)
    y16 = t0 ^ y11
    trace.append(y16)
    y21 = y13 ^ y16
    trace.append(y21)
    y18 = U[0] ^ y16
    trace.append(y18)
    t2 = y12 & y15
    trace.append(t2)
    t2 = t2 ^ r[0]
    trace.append(t2)
    t3 = y3 & y6
    trace.append(t3)
    t3 = t3 ^ r[1]
    trace.append(t3)
    t4 = t3 ^ t2
    trace.append(t4)
    t5 = y4 & U[7]
    trace.append(t5)
    t5 = t5 ^ r[2]
    trace.append(t5)
    t6 = t5 ^ t2
    trace.append(t6)
    t7 = y13 & y16
    trace.append(t7)
    t7 = t7 ^ r[3]
    trace.append(t7)
    t8 = y5 & y1
    trace.append(t8)
    t8 = t8 ^ r[4]
    trace.append(t8)
    t9 = t8 ^ t7
    trace.append(t9)
    t10 = y2 & y7
    trace.append(t10)
    t10 = t10 ^ r[5]
    trace.append(t10)
    t11 = t10 ^ t7
    trace.append(t11)
    t12 = y9 & y11
    trace.append(t12)
    t12 = t12 ^ r[6]
    trace.append(t12)
    t13 = y14 & y17
    trace.append(t13)
    t13 = t13 ^ r[7]
    trace.append(t13)
    t14 = t13 ^ t12
    trace.append(t14)
    t15 = y8 & y10
    trace.append(t15)
    t15 = t15 ^ r[8]
    trace.append(t15)
    t16 = t15 ^ t12
    trace.append(t16)
    t17 = t4 ^ y20
    trace.append(t17)
    t18 = t6 ^ t16
    trace.append(t18)
    t19 = t9 ^ t14
    trace.append(t19)
    t20 = t11 ^ t16
    trace.append(t20)
    t21 = t17 ^ t14
    trace.append(t21)
    t22 = t18 ^ y19
    trace.append(t22)
    t23 = t19 ^ y21
    trace.append(t23)
    t24 = t20 ^ y18
    trace.append(t24)
    t25 = t21 ^ t22
    trace.append(t25)
    t26 = t21 & t23
    trace.append(t26)
    t26 = t26 ^ r[9]
    trace.append(t26)
    t27 = t24 ^ t26
    trace.append(t27)
    t28 = t25 & t27
    trace.append(t28)
    t28 = t28 ^ r[10]
    trace.append(t28)
    t29 = t28 ^ t22
    trace.append(t29)
    t30 = t23 ^ t24
    trace.append(t30)
    t31 = t22 ^ t26
    trace.append(t31)
    t32 = t31 & t30
    trace.append(t32)
    t32 = t32 ^ r[11]
    trace.append(t32)
    t33 = t32 ^ t24
    trace.append(t33)
    t34 = t23 ^ t33
    trace.append(t34)
    t35 = t27 ^ t33
    trace.append(t35)
    t36 = t24 & t35
    trace.append(t36)
    t36 = t36 ^ r[12]
    trace.append(t36)
    t37 = t36 ^ t34
    trace.append(t37)
    t38 = t27 ^ t36
    trace.append(t38)
    t39 = t29 & t38
    trace.append(t39)
    t39 = t39 ^ r[13]
    trace.append(t39)
    t40 = t25 ^ t39
    trace.append(t40)
    t41 = t40 ^ t37
    trace.append(t41)
    t42 = t29 ^ t33
    trace.append(t42)
    t43 = t29 ^ t40
    trace.append(t43)
    t44 = t33 ^ t37
    trace.append(t44)
    t45 = t42 ^ t41
    trace.append(t45)
    z0 = t44 & y15
    trace.append(z0)
    z0 = z0 ^ r[14]
    trace.append(z0)
    z1 = t37 & y6
    trace.append(z1)
    z1 = z1 ^ r[15]
    trace.append(z1)
    z2 = t33 & U[7]
    trace.append(z2)
    z2 = z2 ^ r[16]
    trace.append(z2)
    z3 = t43 & y16
    trace.append(z3)
    z3 = z3 ^ r[17]
    trace.append(z3)
    z4 = t40 & y1
    trace.append(z4)
    z4 = z4 ^ r[18]
    trace.append(z4)
    z5 = t29 & y7
    trace.append(z5)
    z5 = z5 ^ r[19]
    trace.append(z5)
    z6 = t42 & y11
    trace.append(z6)
    z6 = z6 ^ r[20]
    trace.append(z6)
    z7 = t45 & y17
    trace.append(z7)
    z7 = z7 ^ r[21]
    trace.append(z7)
    z8 = t41 & y10
    trace.append(z8)
    z8 = z8 ^ r[22]
    trace.append(z8)
    z9 = t44 & y12
    trace.append(z9)
    z9 = z9 ^ r[23]
    trace.append(z9)
    z10 = t37 & y3
    trace.append(z10)
    z10 = z10 ^ r[24]
    trace.append(z10)
    z11 = t33 & y4
    trace.append(z11)
    z11 = z11 ^ r[25]
    trace.append(z11)
    z12 = t43 & y13
    trace.append(z12)
    z12 = z12 ^ r[26]
    trace.append(z12)
    z13 = t40 & y5
    trace.append(z13)
    z13 = z13 ^ r[27]
    trace.append(z13)
    z14 = t29 & y2
    trace.append(z14)
    z14 = z14 ^ r[28]
    trace.append(z14)
    z15 = t42 & y9
    trace.append(z15)
    z15 = z15 ^ r[29]
    trace.append(z15)
    z16 = t45 & y14
    trace.append(z16)
    z16 = z16 ^ r[30]
    trace.append(z16)
    z17 = t41 & y8
    trace.append(z17)
    z17 = z17 ^ r[31]
    trace.append(z17)
    tc1 = z15 ^ z16
    trace.append(tc1)
    tc2 = z10 ^ tc1
    trace.append(tc2)
    tc3 = z9 ^ tc2
    trace.append(tc3)
    tc4 = z0 ^ z2
    trace.append(tc4)
    tc5 = z1 ^ z0
    trace.append(tc5)
    tc6 = z3 ^ z4
    trace.append(tc6)
    tc7 = z12 ^ tc4
    trace.append(tc7)
    tc8 = z7 ^ tc6
    trace.append(tc8)
    tc9 = z8 ^ tc7
    trace.append(tc9)
    tc10 = tc8 ^ tc9
    trace.append(tc10)
    tc11 = tc6 ^ tc5
    trace.append(tc11)
    tc12 = z3 ^ z5
    trace.append(tc12)
    tc13 = z13 ^ tc1
    trace.append(tc13)
    tc14 = tc4 ^ tc12
    trace.append(tc14)
    s[3] = tc3 ^ tc11
    trace.append(s[3])
    tc16 = z6 ^ tc8
    trace.append(tc16)
    tc17 = z14 ^ tc10
    trace.append(tc17)
    tc18 = tc13 ^ tc14
    trace.append(tc18)
    s[7] = z12 ^ tc18
    trace.append(s[7])
    s[7] = s[7] ^ 1
    trace.append(s[7])
    tc20 = z15 ^ tc16
    trace.append(tc20)
    tc21 = tc2 ^ z11
    trace.append(tc21)
    s[0] = tc3 ^ tc16
    trace.append(s[0])
    s[6] = tc10 ^ tc18
    trace.append(s[6])
    s[6] = s[6] ^ 1
    trace.append(s[6])
    s[4] = tc14 ^ s[3]
    trace.append(s[4])
    s[1] = s[3] ^ tc16
    trace.append(s[1])
    s[1] = s[1] ^ 1
    trace.append(s[1])
    tc26 = tc17 ^ tc20
    trace.append(tc26)
    s[2] = tc26 ^ z17
    trace.append(s[2])
    s[2] = s[2] ^ 1
    trace.append(s[2])
    s[5] = tc21 ^ tc17
    trace.append(s[5])
    return s
def mixcolumn(U,trace):  #U[32]
    y = [0] * 32
    x32 = U[5] ^ U[13]
    trace.append(x32)
    x33 = U[6] ^ U[30]
    trace.append(x33)
    x34 = U[21] ^ x33
    trace.append(x34)
    x35 = U[14] ^ U[30]
    trace.append(x35)
    x36 = U[13] ^ U[29]
    trace.append(x36)
    x37 = x35 ^ x36
    trace.append(x37)
    x38 = U[14] ^ U[22]
    trace.append(x38)
    x39 = U[5] ^ x38
    trace.append(x39)
    x40 = x37 ^ x39
    trace.append(x40)
    y[21] = x40
    x41 = U[21] ^ U[29]
    trace.append(x41)
    x42 = x39 ^ x41
    trace.append(x42)
    y[13] = x42
    x43 = U[0] ^ U[24]
    trace.append(x43)
    x44 = U[15] ^ U[23]
    trace.append(x44)
    x45 = U[7] ^ x43
    trace.append(x45)
    x46 = x44 ^ x45
    trace.append(x46)
    y[31] = x46
    x47 = U[0] ^ U[8]
    trace.append(x47)
    x48 = U[31] ^ x44
    trace.append(x48)
    x49 = x47 ^ x48
    trace.append(x49)
    y[7] = x49
    x50 = U[9] ^ U[17]
    trace.append(x50)
    x51 = U[16] ^ x43
    trace.append(x51)
    x52 = x50 ^ x51
    trace.append(x52)
    y[8] = x52
    x53 = U[1] ^ U[25]
    trace.append(x53)
    x54 = x47 ^ x53
    trace.append(x54)
    x55 = U[16] ^ x54
    trace.append(x55)
    y[24] = x55
    x56 = U[18] ^ U[26]
    trace.append(x56)
    x57 = U[9] ^ x56
    trace.append(x57)
    x58 = x53 ^ x57
    trace.append(x58)
    y[17] = x58
    x59 = U[3] ^ U[11]
    trace.append(x59)
    x60 = U[10] ^ x59
    trace.append(x60)
    x61 = x56 ^ x60
    trace.append(x61)
    y[2] = x61
    x62 = U[2] ^ U[10]
    trace.append(x62)
    x63 = U[25] ^ x62
    trace.append(x63)
    x64 = x50 ^ x63
    trace.append(x64)
    y[1] = x64
    x65 = U[19] ^ U[27]
    trace.append(x65)
    x66 = U[26] ^ x65
    trace.append(x66)
    x67 = x62 ^ x66
    trace.append(x67)
    y[18] = x67
    x68 = U[6] ^ U[31]
    trace.append(x68)
    x69 = x38 ^ x68
    trace.append(x69)
    x70 = x45 ^ x69
    trace.append(x70)
    y[30] = x70
    x71 = U[1] ^ U[17]
    trace.append(x71)
    x72 = U[24] ^ x71
    trace.append(x72)
    x73 = x54 ^ x72
    trace.append(x73)
    y[16] = x73
    x74 = U[8] ^ U[16]
    trace.append(x74)
    x75 = x50 ^ x74
    trace.append(x75)
    x76 = x72 ^ x75
    trace.append(x76)
    y[0] = x76
    x77 = U[7] ^ U[15]
    trace.append(x77)
    x78 = x74 ^ x77
    trace.append(x78)
    x79 = x48 ^ x78
    trace.append(x79)
    y[15] = x79
    x80 = U[16] ^ U[24]
    trace.append(x80)
    x81 = U[31] ^ x80
    trace.append(x81)
    x82 = x77 ^ x81
    trace.append(x82)
    y[23] = x82
    x83 = U[2] ^ U[18]
    trace.append(x83)
    x84 = x71 ^ x83
    trace.append(x84)
    x85 = x57 ^ x84
    trace.append(x85)
    y[25] = x85
    x86 = x63 ^ x84
    trace.append(x86)
    y[9] = x86
    x87 = U[11] ^ U[27]
    trace.append(x87)
    x88 = x83 ^ x87
    trace.append(x88)
    x89 = x60 ^ x88
    trace.append(x89)
    y[26] = x89
    x90 = x66 ^ x88
    trace.append(x90)
    y[10] = x90
    x91 = x68 ^ x80
    trace.append(x91)
    x92 = U[23] ^ x35
    trace.append(x92)
    x93 = x91 ^ x92
    trace.append(x93)
    y[22] = x93
    x94 = U[22] ^ x35
    trace.append(x94)
    x95 = x47 ^ x77
    trace.append(x95)
    x96 = x94 ^ x95
    trace.append(x96)
    y[6] = x96
    x97 = U[22] ^ x44
    trace.append(x97)
    x98 = x33 ^ x74
    trace.append(x98)
    x99 = x97 ^ x98
    trace.append(x99)
    y[14] = x99
    x100 = U[20] ^ U[28]
    trace.append(x100)
    x101 = U[12] ^ x47
    trace.append(x101)
    x102 = x32 ^ x100
    trace.append(x102)
    x103 = x101 ^ x102
    trace.append(x103)
    y[4] = x103
    x104 = U[4] ^ U[19]
    trace.append(x104)
    x105 = x87 ^ x104
    trace.append(x105)
    x106 = x101 ^ x105
    trace.append(x106)
    y[3] = x106
    x107 = x80 ^ x100
    trace.append(x107)
    x108 = U[3] ^ x87
    trace.append(x108)
    x109 = x107 ^ x108
    trace.append(x109)
    y[19] = x109
    x110 = U[28] ^ x104
    trace.append(x110)
    x111 = x43 ^ x59
    trace.append(x111)
    x112 = x110 ^ x111
    trace.append(x112)
    y[27] = x112
    x113 = U[12] ^ U[20]
    trace.append(x113)
    x114 = x65 ^ x113
    trace.append(x114)
    x115 = U[3] ^ x74
    trace.append(x115)
    x116 = x114 ^ x115
    trace.append(x116)
    y[11] = x116
    x117 = U[5] ^ U[29]
    trace.append(x117)
    x118 = U[4] ^ x43
    trace.append(x118)
    x119 = x113 ^ x117
    trace.append(x119)
    x120 = x118 ^ x119
    trace.append(x120)
    y[28] = x120
    x121 = U[13] ^ x74
    trace.append(x121)
    x122 = U[4] ^ U[21]
    trace.append(x122)
    x123 = x100 ^ x122
    trace.append(x123)
    x124 = x121 ^ x123
    trace.append(x124)
    y[12] = x124
    x125 = x41 ^ x80
    trace.append(x125)
    x126 = U[12] ^ U[28]
    trace.append(x126)
    x127 = U[4] ^ x126
    trace.append(x127)
    x128 = x125 ^ x127
    trace.append(x128)
    y[20] = x128
    x129 = x34 ^ x37
    trace.append(x129)
    y[5] = x129
    x130 = x32 ^ x34
    trace.append(x130)
    y[29] = x130
    return y

#l=32个与门，h为槽的个数,plaintext[16][8],K[round+1][16][8]
def ShiftRow(s):
    order = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]
    s = [s[i] for i in order]
    return s


#---------------Surper Sbox Dummy Shuffling---------------#

# P[4][8]: binary
# K[4][8]: binary
# r[4][32]: binary
def SurperSbox(plaintext, K, trace, r):
    
    state = [[0] * 8 for _ in range(4)]        # AddRoundkey and SubByte operations
    temp = [] # contains the imput of the MixColunms


#    print("AD trace length", len(trace))
    # AddRoundKey 
    for i in range(4):
        state[i] = addroudkey(plaintext[i], K[i], trace)

#    print("SB trace length", len(trace))
    # SubByte
    for i in range(4):
        state[i] = sbox(state[i], r[i], trace)

#    print("MC trace length", len(trace))
    # MixColumns
    # state to temp
    for i in range(4):
        for j in range(8):
            temp.append(state[i][j])

#    print("End trace length", len(trace))

    temp = mixcolumn(temp, trace)

    return temp

def DummyShuffleSurperSbox(Plaintext, K, Ns): # Ns: slot number
    trace = []
    MainSlotIndex = random.randint(0, Ns - 1)
    
    for i in range(Ns):

        if i == MainSlotIndex:  # Main slot
            r = []
            for byte in range(4):
                r.append([0] * 32)
            state = SurperSbox(Plaintext, K, trace, r)
        else:
            r = []
            for byte in range(4):
                r.append([])
                for bit in range(32):
                    r[byte].append(random.randint(0,1)) # Gen 32 random numbers used in S-box

            RanPlain = []
            
            for byte in range(4):
                RanPlain.append([])
                for bit in range(8):
                    RanPlain[byte].append(random.randint(0,1)) # Gen random input of each slot
            state = SurperSbox(RanPlain, K, trace, r)

    return trace
                

### text ###

# P[4][8]: binary
# K[4][8]: binary
K = []
P = []
for byte in range(4):
    K.append([])
    P.append([])
    for bit in range(8):
        K[byte].append(random.randint(0,1))
        P[byte].append(random.randint(0,1))

#Ns = 32
#trace = DummyShuffleSurperSbox(P, K, 32)
#print(len(trace))
##print(trace)

def GenPlain():
    Pi = []
    for byte in range(4):
        Pi.append([])
        for bit in range(8):
            Pi[byte].append(random.randint(0,1))
    return Pi


def GenKey():
    Pi = []
    for byte in range(4):
        Pi.append([])
        for bit in range(8):
            Pi[byte].append(random.randint(0,1))
    return Pi

    
# P = [], after function will contains all plaintexts with p[16]
# 
def CollectTrace_SurperSbox(P, K, Nt, Ns):
#    Ns = 16    
    TraceArray = []
    for time in range(Nt):
        # Random Gen Pi[4][8]: binary    
        Pi = GenPlain()
        trace = DummyShuffleSurperSbox(Pi, K, Ns)

#        for byte in range(len(Pi)):
#            Pi[byte] = BintoHex(Pi[byte])

        TraceArray.append(trace)
        P.append(Pi)

    return TraceArray

#K = GenKey()
#P = []
#print(len(CollectTrace_SurperSbox(P, K, 1)[0]))
#Pi = GenPlain()
#K = GenKey()
#print(len(DummyShuffleSurperSbox(Pi, K, 16)))
#K = GenKey()
#print(K)
#P = []
#Nt = 10
#
#TraceArray = CollectTrace_SurperSbox(P, K, Nt)
#print(len(TraceArray), len(TraceArray[0]), len(P))
#for i in range(len(P)):
#    print(i, P[i])

    
        



#---------------------------------------------------------#



#
#def slots(plaintext,K,r,round,trace):
#    state = [[0] * 8 for _ in range(16)]
#    temp = [[0] * 32 for _ in range(4)]
#    for i in range(16):
#        state[i] = addroudkey(plaintext[i], K[0][i], trace)
#    for i in range(round):
#        for j in range(16):
#            state[j] = sbox(state[j], r, trace)
#        state = ShiftRow(state)
#        if i != round-1:
#            for a in range(4):
#                mix = [] * 32
#                for b in range(4):
#                    mix += state[b+4*a]
#                temp[a] = mixcolumn(mix, trace)
#            for a in range(16):
#                for b in range(8):
#                    state[a][b] = temp[a//4][b+(a % 4)*8]
#        for j in range(16):
#            state[j] = addroudkey(state[j], K[i+1][j], trace)
#    return state
#def dummyshuffleAES(plaintext,K,h,trace):    #h为槽的个数
#    state = [[0] * 8 for _ in range(16) for _ in range(h)]
#    location = random.randint(0,h-1)
#    u1 = [[0] * 8 for _ in range(16)]
#    r = [0]*32
#    for i in range(h):
#        if location == i:
#            r = [0] * 32
#            state[i] = slots(plaintext, K, r,2, trace)
#        else:
#            for a in range(16):
#                for b in range(8):
#                    u1[a][b] = random.randint(0,1)
#            for a in range(32):
#                r[a] = random.randint(0,1)
#            state[i] = slots(u1, K, r, 2, trace)
#    return state

#def collectTrace(P,K,n):   #n为明文的个数
##    file = open("trace.txt", "w")
#    TraceArray = []
#    for i in range(n):
#        trace = []
#        Temp = [[0] * 8 for _ in range(16)]
#        for j in range(16):
#            for k in range(8):
#                Temp[j][k] = random.randint(0, 1)
#                trace.append(Temp[j][k])
#        P.append(Temp)
#        dummyshuffleAES(P[i], K, 4, trace)
#        TraceArray.append(trace)
##    file.write("Plaintext:\n")
##    file.write(str(P))
##    file.write("\n")
##    file.write("Trace:\n")
##    file.write(str(TraceArray))
##    file.close()
#    return TraceArray
#def hex_to_binary(hex_num):
#    binary = bin(int(hex_num))[2:]
#    array = []
#    a = [0]*(8-len(binary))
#    b = list(map(int, binary))
#    array = a+b
#    return array

















#'''
#trace = []
#plaintext = [0x32,0x43,0xf6,0xa8,0x88,0x5a,0x30,0x8d,0x31,0x31,0x98,0xa2,0xe0,0x37,0x07,0x34]
#U = [[0,0,1,1,0,0,1,0],[0,1,0,0,0,0,1,1],[1,1,1,1,0,1,1,0],[1,0,1,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,1,0,1,1,0,1,0],[0,0,1,1,0,0,0,0],[1,0,0,0,1,1,0,1],
#     [0,0,1,1,0,0,0,1],[0,0,1,1,0,0,0,1],[1,0,0,1,1,0,0,0],[1,0,1,0,0,0,1,0],[1,1,1,0,0,0,0,0],[0,0,1,1,0,1,1,1],[0,0,0,0,0,1,1,1],[0,0,1,1,0,1,0,0]]
#'''
#K = [[[0] * 8 for _ in range(16)] for _ in range(3)]
#key0 = [0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c]
#key1 = [0xa0,0xfa,0xfe,0x17,0x88,0x54,0x2c,0xb1,0x23,0xa3,0x39,0x39,0x2a,0x6c,0x76,0x05]
#key2 = [0xf2,0xc2,0x95,0xf2,0x7a,0x96,0xb9,0x43,0x59,0x35,0x80,0x7a,0x73,0x59,0xf6,0x7f]




