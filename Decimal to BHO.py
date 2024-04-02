def Bit(a):
    listA=['0','1']
    ansB=''
    for i in range (a):
        if a<2:
            ansB=(listA[a])+ansB
            break
        else:
            b=a%2
            ansB=(listA[b])+ansB
            a=a//2
    return(ansB)
def Hex(a):
    listH=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    ansH=''
    for i in range (a):
        if a<16:
            ansH=(listH[a])+ansH
            break
        else:
            b=a%16
            ansH=(listH[b])+ansH
            a=a//16
    return(ansH)
def Oct(a):
    listO=['0','1','2','3','4','5','6','7']
    ansO=''
    for i in range (a):
        if a<8:
            ansO=(listO[a])+ansO
            break
        else:
            b=a%8
            ansO=(listO[b])+ansO
            a=a//8
    return(ansO)
a=int(input("Enter Number:"))
print(Bit(a))
print(Hex(a))
print(Oct(a))