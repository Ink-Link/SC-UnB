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

def xor(a, b):
    saida = ""

    for i in range(len(a)):
        if a[i] == b[i]:
            saida += "0"
        else:
            saida += "1"
    return saida

def F(right, subchave):
    exp = right[3] + right[0] + right[1] + right[2] + right[1] + right[2] + right[3] + right[0]
    
    P = [[xor(exp[0], subchave[0]), xor(exp[1], subchave[1]), xor(exp[2], subchave[2]), xor(exp[3], subchave[3])],
    [xor(exp[4], subchave[4]), xor(exp[5], subchave[5]), xor(exp[6], subchave[6]), xor(exp[7], subchave[7])]]
    
    S0 = [["01", "00", "11", "10"],
    ["11","10","01","00"],
    ["00","10","01","11"],
    ["11","01","11","10"]]

    S1 = [["00", "01", "10", "11"],
    ["10","00","01","11"],
    ["11","00","01","00"],
    ["10","01","00","11"]]
        
    chave = S0[int(P[0][0] + P[0][3], 2)][int(P[0][1] + P[0][2], 2)] + S1[int(P[1][0] + P[1][3], 2)][int(P[1][1] + P[1][2], 2)]

    chave = chave[1] + chave[3] + chave[2] + chave[0]
    
    return chave


def ip(msg):
    msg = msg[1] + msg[5] + msg[2] + msg[0] + msg[3] + msg[7] + msg[4] + msg[6]  

    return msg

def ipInv(msg):
    msg = msg[3] + msg[0] + msg[2] + msg[4] + msg[6] + msg[1] + msg[7] + msg[5]

    return msg

def feistel(left, right, chave):
    resultado = F(right, chave)

    print(left)

    print(resultado)

    resultado = xor(left, resultado)

    print(resultado)

    return right, resultado

def SDES(msg, chave):
    k1, k2 = (genChave(perm10(chave)))

    msg = ip(msg)

    L, R = msg[0:4], msg[4:8]

    L, R = feistel(L, R, k1)

    R, L = feistel(L, R, k2)

    return ipInv(L + R)
####### CRIPTOGRAFIA #######

# RESULTADO DESEJADO : 10101000
# RESULTADO ATINGIDO : ???

#print(F("1101", "10100100"))

print(SDES("11010111", "1010000010"))

"""a, b = genChave("1000001100")
print(a, b)"""