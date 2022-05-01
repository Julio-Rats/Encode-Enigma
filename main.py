from ast import While
from copy   import deepcopy
from random import randint

import code

def valid_gear(ord_gear):
    for element in range(len(ord_gear)):
        if (int(ord_gear[element]) > 5 or int(ord_gear[element]) < 1):
            return False
        for another in range(element+1,len(ord_gear)):
            if (ord_gear[element] == ord_gear[another]):
                return False
            
    return True

def valid_pos(pos_gear):
    for element in pos_gear:
        if (element > 26 or element < 1):
            return False
                    
    return True

print("Escolha 3 numeros entre 1 e 5, essa sera a ordem das engrenagens comutadoras (sem repetir).")
print("Entre com a ordem das engrenagens: ",end="")
ord_gear = list(input().strip().replace(" ", "").replace(",", ""))

while(not (valid_gear(ord_gear) and len(ord_gear) == 3)):
    print("Entrada invalida, tente novamente: ",end="")
    ord_gear = list(input().strip().replace(" ", "").replace(",", ""))
    
pos_gear = list()
print("\nEscolha 3 numeros entre 1 e 26, essa sera a posição inicial das engrenagens comutadoras.")
print("Escolha a posição da primeira engrenagem: ",end="")
pos_gear.append(int(input().strip().replace(" ","")))
print("Escolha a posição da segunda engrenagem: ",end="")
pos_gear.append(int(input().strip().replace(" ","")))
print("Escolha a posição da terceira engrenagem: ",end="")
pos_gear.append(int(input().strip().replace(" ","")))

while(not valid_pos(pos_gear)):
    print("\nPosições invalidas, tente novamente.")
    pos_gear = list()
    print("Escolha a posição da primeira engrenagem: ",end="")
    pos_gear.append(int(input().strip().replace(" ","")))
    print("Escolha a posição da segunda engrenagem: ",end="")
    pos_gear.append(int(input().strip().replace(" ","")))
    print("Escolha a posição da terceira engrenagem: ",end="")
    pos_gear.append(int(input().strip().replace(" ","")))



for ord in range(len(ord_gear)):
    ord_gear[ord] = int(ord_gear[ord])

code.num_gear = deepcopy(ord_gear)
code.dif_gear = deepcopy(pos_gear)

for pos in range(len(code.dif_gear)):
    code.dif_gear[pos] -= 1



print("\nInsira a mensagem: ",end="")
msg = input()
print("")


print("Ordem Utilizada: ",ord_gear)
print("Posições Utilizadas: ",pos_gear)

c = code.run(msg)

print("\nMensagem computada:")
print(c)
print("")


