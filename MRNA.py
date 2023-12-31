prot_seq = 'MHDTLVERVPTEKRLQCENNLQAVKLKNQSQQTPAWFLGEAKIFEAFWGGWWRKNLVMECLHRGGFRGIALAQEGISWDVAFYENPAIVSSLPHLEECDWRFSTNQAHWWHYQLIVFSKSYYMGLITHDWSEPSMYCIPRKIPMWYEWGEAMMYMRLPHVELAVIMRFMAIADSGMKRGWVLELCLQHLKDCRIKHLWKVFGGWPHQWLRTFWHAAKQHIFLDCICAWNFKWGKMQDCEIEYWCQVQTEGIHRHDRSSWRDSSNRMRHMIGSLFDQILHNQKHTEFPNFPNRTTETDRNDSFWNKVIFEAPKHHYENHTNGQHPSRHHTYCMHWFPCVWVILDALMFNDNIGGHPNISCQHLINMITVYDCLKFKAYAMTSWDVVEWKIRGIHSPYIEPALKLWREVEAFRTSTQFTKCTPVRYTPEEDRKRVMWLPMMVKDWADVHLVTTGECMDDFHCSVARIQHPKFPTCRQYSYQDIMRTWTMKYYMVFARFPGDHSRPQTFTAYCVWLSVMWTEIQTPPGIMIFFAREKQQGWTMTKEFSGPDNWPVHDKSNLQAYMHCVGGAPVWYWACCEKKGLKFNNMRDGHIIMSIDFNRHLEPAAHMRMCNFSSDVYYASAIVQGKCRFAQERVANITTHHPRTNLMCKVTCIFAWGHERRSAHKMTTTGGVAQHTWTRCEQTVQNMAIPDNFNPQPPCDGRRQKNRKLLNPCRHMNFMMKGMDVHGTITQMWIGRAILCCFGYSPICPKTSIKWRCFACRKDMRDCIQIIWDKEIKGHKDHSTYHMQHDVVHPTCHEFRCVPEVVTDCQDYMMNVHNEYYDVKFCHRQKIAYCASLAHTVESDEQETFCVICLSSVKKMCRRNLWGLFYFRNGWTDNSMMSRFNHQVWQDWLVCNPWSHKEGTWFGTFDVVYFGLKYGNHAELYVERYHSCKQEECAMKCSDRLTFEWRIKCLTRLACKQINRQALFDPPWTVEPGAVKPPCQPRGMWADGYYHWNMQQ'
count = 1
lst_num = []

#Creating a dictionary which counts the amount of RNA codons which can encode for the same amino acid 
cod_dict = {'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4, 'Stop:codon':3}

for amino_acid in prot_seq:
    count = (cod_dict[amino_acid]*count) % 1000000
count = (count*cod_dict['Stop:codon'])%1000000

print(count)





