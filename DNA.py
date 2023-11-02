a = input('Insert DNA string: ')
count_A = 0
count_C = 0
count_G = 0
count_T = 0

for el in a:
    if el == 'A':
        count_A += 1
    elif el == 'C':
        count_C += 1
    elif el == 'G':
        count_G += 1
    elif el == 'T':
        count_T += 1

print(count_A, count_C, count_G, count_T)

