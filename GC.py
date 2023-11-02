Fasta_input = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''

seq_list = []
sequences = Fasta_input.split('>')
count_max = 0
name_string = ""

for seq in sequences:
    if seq:  
        a = seq.split('\n')
        DNAseq = ''.join(a[1:])
        seq_list.append(DNAseq)
        name = a[0]
        C_count = DNAseq.count('C')
        G_count = DNAseq.count('G')
        ctot = (C_count + G_count) / len(DNAseq)
        if ctot > count_max:
            count_max = ctot
            name_string = name

print(f"{name_string}\n{count_max * 100:.6f}")
