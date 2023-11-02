def mortal_rab(n, m):
    if n == 1:
        return 1
    
    rabbit_pairs = [0] * m
    rabbit_pairs[0] = 1  #initial pair of rabbits in the first month 

    for month in range(2, n + 1):
        new_pairs = sum(rabbit_pairs[1:])
        
        for i in range(m - 1, 0, -1):
            rabbit_pairs[i] = rabbit_pairs[i - 1]
    
        rabbit_pairs[0] = new_pairs

    tot_pairs = sum(rabbit_pairs)
    return tot_pairs

print(mortal_rab(81, 17))
  

