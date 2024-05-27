from scipy.stats import norm
import math

# Ns is the slot number used in the attacked dummy shuffling
# Nt is the trace number


def NtDetermine(gamma0, gamma1, Ns):

    gamma0 = pow(gamma0, 1/Ns)

    Nt = pow(Ns * norm.ppf(1 - gamma1) - math.sqrt(pow(Ns,2) - 1) * norm.ppf(gamma0), 2)
    c = Nt / 2 + math.sqrt(Nt) / 2 * norm.ppf(1 - gamma1)

    return [Nt, c]

gamma1 = pow(2, -20)

def ComGamma1(Ns, Nt, c):

    mur = Nt * (1 / 2)
    sigma = math.sqrt(Nt / 4)
    gamma0 = 1 - norm.cdf( (c - mur) / sigma )
    
    return gamma0

def ComGamma0(Ns, Nt, c):

    mur = Nt * (1 / 2 + 1 / 2 / Ns)
    sigma = math.sqrt(Nt / 4 * ( 1 - 1 / Ns / Ns))
    gamma0 = norm.cdf( (c - mur) / sigma )
    gamma0 = pow(gamma0, Ns)
    
    return gamma0

def ComSuccessRate(Ns, Nt, c):

    return 1 - ComGamma0(Ns, Nt, c)
 
