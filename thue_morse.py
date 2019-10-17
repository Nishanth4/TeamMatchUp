
def complement(seq):
    comp = ""

    for i in range(len(seq)):
        if (seq[i] == '0'):
            comp+='1'
        else:
            comp+='0'
    
    return comp

def createSequence(n):

    sequence = "0"

    for i in range(1,n):
        sequence+=complement(sequence)

    return sequence