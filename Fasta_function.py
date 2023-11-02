def Fasta_rem(Fasta_input):
    sequences = Fasta_input.split('>')
    seq_list = []
    
    for seq in sequences:
        if seq:
            a = seq.split('\n')
            DNAseq = ''.join(a[1:])
            seq_list.append(DNAseq)
            
    print(seq_list)