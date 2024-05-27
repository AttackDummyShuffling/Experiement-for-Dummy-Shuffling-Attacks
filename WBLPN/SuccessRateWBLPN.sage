def ComP(Tau, W):
    return (1 - Tau) ** W

def ComA(Tau, W, Pnfm):
    return ceil(log(1-Pnfm)/(log(1-(1-Tau)^W)))

def ComGamma0NoPool(Tau, c, m, A, W):
    return ComGamma0(ComAlpha0(Tau,c,m),ComBeta(c,m),(1-Tau)**W, A)

def ComGamma0WithPool(Tau, c, m, A, W, Tp):
    s = 0
    for k in range(0,Tp):
        s += binomial(Tp, k)*Tau**k*(1-Tau)**(Tp-k)*ComGamma0(ComAlpha0(Tau, c, m),ComBeta(c,m),binomial(Tp-k,W)/binomial(Tp,W), A)
    return s

def ComGamma1(c, m, A):
    return 1 - (1 - ComBeta(c,m)) ** A 

def ComMC(Tau, Gamma0, Gamma1, A, W): 
    P = ComP(Tau, W)
    A0 = 1-2* (1-Gamma1)**(1/A)
    B0 = 1-2*(Gamma0-(1-P)**A*(1-Gamma1)**A)/((P+(1-Gamma1)*(1-P))**A-(1-P)**A*(1-Gamma1)**A) 
    S = -1/sqrt(2) * erfinv(A0)
    T = sqrt(2*Tau*(1-Tau)) * erfinv(B0)
    m1 = ((T + S)/(1/2 - Tau))**2
    c1 = -S * sqrt(m1) + 1/2 * m1
    c2 = T * sqrt(m1) + Tau * m1

    m2 = int(m1)
    while true:
        m2 += 1
        c1 = -S * sqrt(m2) + 1/2 * m2
        c2 = T * sqrt(m2) + Tau * m2
        if  int(c1) - int(c2) >= 1:
            break
    return (m2, int(c1))

def ComAlpha0(Tau, c, m): 
    z = (c - Tau * m) / sqrt(Tau*(1-Tau)*m)
    phiz = 1/2 + 1/2 * erf(z / sqrt(2))
    N = 1 - phiz
    return N

def ComBeta(c, m): 
    z = (c - 1/2 * m) / sqrt(1/4 * m)
    phiz = 1/2 + 1/2 * erf(z / sqrt(2))
    N = phiz
    return N
	
def ComGamma0(alpha0, beta, P, A): 
    return (P + (1 - P) * (1 - beta)) ** A * alpha0 + (1 - alpha0) * (1 - beta) ** A * (1 - P) ** A

W = 10
Pnfm = 0.999
Tau = 1/4
A = ComA(Tau,W,Pnfm)
print("W=",W,"Tau=",Tau,"A=",A)

Gamma0 = 2**(-10)
Gamma1 = 2**(-10)
m,c = ComMC(Tau, Gamma0, Gamma1, A, W)
print("m=",m," c=",c)

Tp = 20*W
print("Tp=",Tp)
Gamma0NoPool = ComGamma0NoPool(Tau,c,m,A,W)
Gamma0WithPool = ComGamma0WithPool(Tau,c,m,A,W,Tp)
Gamma1 = ComGamma1(c,m,A)
print("Gamma0NoPool=", (Gamma0NoPool).n(digits = 10),"\nGamma0WithPool=",(Gamma0WithPool).n(digits = 10),"\nGamma1=",(Gamma1).n(digits = 10))