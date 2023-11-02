from math import comb
#importing the binomial ccoefficient function 


def gen_prob(k, N):
    p = 0.25  #probability of having AaBb genotipe 
    count = 0

    #binomial distribution 
    for n in range(N, 2**k + 1):
        a = comb(2**k, n) * (p ** n) * ((1 - p) ** (2**k - n))
        count += a

    return round(count,3)

print(gen_prob(7,32))

