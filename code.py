from gears import *

set_gear = {1:gear1, 2:gear2, 3:gear3, 4:gear4, 5:gear5}
num_gear = [1,2,3]
dif_gear = [0,0,0]

def actMotion():
    global dif_gear
    dif_gear[1] = (dif_gear[1]+1) % 26
    if dif_gear[1] == 0:
        dif_gear[2] = (dif_gear[2]+1) % 26
        if dif_gear[2] == 0:
            dif_gear[3] = (dif_gear[3]+1) % 26
       
def code(letter):
    codLetter = ord(letter.lower()) - 97
    codLetter = plugs[codLetter]
    for gear,dif in zip(num_gear,dif_gear):
        codLetter = (set_gear[gear][(codLetter+dif)%26]+dif)%26
        
    codLetter = ivert[codLetter]
    
    for gear,dif in zip(num_gear[::-1],dif_gear[::-1]):
        codLetter = (set_gear[gear][(codLetter-dif)%26]-dif)%26
        
    codLetter = plugs[codLetter]
    return codLetter

def run(word):
    cript = ""
    for letter in word:
        actMotion()
        if letter != " ":
            cript += chr(code(letter)+97)
        else:
            cript += " "
        
    return cript    