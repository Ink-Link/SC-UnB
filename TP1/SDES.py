####### GERAÇÃO DE CHAVE #######
def perm10(k): 
    chaveP = k[2]+k[4]+k[1]+k[6]+k[3]+k[9]+k[0]+k[8]+k[5]
    return chaveP

def perm8(kLS):
    chaveP = kLS[5]+kLS[2]+kLS[6]+kLS[3]+kLS[7]+kLS[4]+kLS[9]+kLS[8]
    return chaveP

def permMista(k, n): # Chave, numero da permutacao
    chaveP = 0

    if n == 10:
        for i in [3,5,2,7,4,10,1,9,8,6]:
            chaveP += k[i-1]
    else:
        for i in [6,3,7,4,8,5,10,9]:
            chaveP += k[i-1]

    return chaveP

def ls(k, n): # Chave, numero do shift
    pass

def genChave(chave):


    # Primeira metade
    c1 = chave[:]
    primeiro2 = c1.pop(1)

    # Segunda metade
    c2 = chave[:]
    primeiro2 = c2.pop(1)
    
    k1 = 0
    k2 = 0

    return k1, k2

chave

####### CRIPTOGRAFIA #######
def ip():
    pass

def ipInv():
    pass

# RESULTADO DESEJADO : 10101000
# RESULTADO ATINGIDO : ???