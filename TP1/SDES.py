####### GERAÇÃO DE CHAVE #######
def perm10(k): 
    chaveP = k[2]+k[4]+k[1]+k[6]+k[3]+k[9]+k[0]+k[8]+k[7]+k[5]
    return chaveP

def perm8(kLS):
    chaveP = kLS[5]+kLS[2]+kLS[6]+kLS[3]+kLS[7]+kLS[4]+kLS[9]+kLS[8]
    return chaveP

def permMista(k, n): # Chave, numero da permutacao
    chaveP = ""

    if n == 10:
        for i in [3,5,2,7,4,10,1,9,8,6]:
            chaveP += k[i-1]
    else:
        for i in [6,3,7,4,8,5,10,9]:
            chaveP += k[i-1]

    return chaveP

def ls(k, n): # Chave, numero do shift
        chave = ""
        
        changeList = [0 for i in range(len(k))]

        for i in range(len(k)):
            if (i - n) < 0:
                changeList[len(k) - n + i] = k[i]
            else:
                changeList[i - n] = k[i]
        
        for bit in changeList:
            chave += bit
        return chave

def genChave(chave): 

    # Primeira metade
    c1 = chave[0:5]
    # Segunda metade
    c2 = chave[5:10]

    c1 = ls(c1, 1)

    c2 = ls(c2, 1)

    k1 = c1 + c2
    k1 = perm8(k1)
    k2 = ls(c1, 2) + ls(c2, 2)
    k2 = perm8(k2)

    return k1, k2

####### CRIPTOGRAFIA #######
def ip():
    pass

def ipInv():
    pass

# RESULTADO DESEJADO : 10101000
# RESULTADO ATINGIDO : ???
a, b = genChave("1000001100")
print(a, b)