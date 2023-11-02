DNA_string = 'GATGGAACTTGACTACGTAAATT'
New_DNAstr = ''

for el in DNA_string:
    if el == 'T':
        New_DNAstr += 'U'
    else:
        New_DNAstr += el

print(New_DNAstr)
        
        
