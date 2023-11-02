Fasta_input = '''>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT'''

from HAMM import hamming_dist 

sequences = Fasta_input.split('>')
seq_list = []

# Extract sequences without the FASTA headers
for seq in sequences:
    if seq:
        a = seq.split('\n')
        DNAseq = ''.join(a[1:])
        seq_list.append(DNAseq)

seq_1 = seq_list[0]
seq_2 = seq_list[1]

s1 = 0 #number of transitions 
s2= 0 #number of translations

hamming_dist(seq_1, seq_2)

#Dictionary for transitions and translations 
transitions = {'AG', 'GA', 'CT', 'TC'}
transversions = {'AC', 'CA', 'AT', 'TA', 'GC', 'CG', 'GT', 'TG'}

if len(seq_1) == len(seq_2):
    for base1, base2 in zip(seq_1, seq_2):
        if base1 != base2:
            if base1 + base2 in transitions:
                s1 += 1
            elif base1 + base2 in transversions:
                s2 += 1

ratio = s1 / s2 

#Rounding the ratio
round_rat = round(ratio,11)
print(round_rat)

                    




