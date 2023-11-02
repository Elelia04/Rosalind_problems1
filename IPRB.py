'''
k= hom dom
m = het
n = hom rec
'''
def hom_rec(k,m,n):
    sum_gen = k+m+n
    het_het= (m/sum_gen)*(((m-1)/(sum_gen-1))*1/4)
    het_homr = (m/sum_gen)*(n/(sum_gen-1))*(1/2)
    homr_het = (n/sum_gen)*(m/(sum_gen-1))*(1/2)
    homr_homr = (n/sum_gen)*((n-1)/(sum_gen-1))
    res = 1-(het_het + het_homr + homr_het +homr_homr)
    return res

print(hom_rec(18, 26, 19))
