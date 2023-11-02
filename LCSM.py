def r_seq(file):
    with open(file,'r') as f:
        lines = f.readlines()
    
    titles = {}
    current_title = None
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            current_title = line
            titles[current_title] = ""
        else:
            titles[current_title] += line.replace( "X", "A")
            
    return list(titles.values())

def LCSM(sequence):
    seq = r_seq(sequence)
    smallest_seq = min(seq, key=len)
    for i in range(len(smallest_seq), 0, -1):  
        for j in range(len(smallest_seq) - i + 1):  
            common_seq = smallest_seq[j:j + i]
            if all(common_seq in s for s in seq): 
                return common_seq


f = r"C:\Users\Eleonora\OneDrive\Desktop\Python_ex_2\fasta.tx"
A = LCSM(f)
print(A)