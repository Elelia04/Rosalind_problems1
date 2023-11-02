'''
n = number of months 
k = number of offspring pairs 
'''
def fib_rec(n,k): 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1,k) + k*fib_rec(n-2,k)
    
print(fib_rec(34,4))
    

