msg = input("input a message that ends with punctuation:")
result = " "
while msg.startswith(".") == False:
    ltr = msg[0]
    if ltr.isupper == True:
        ltr.upper()
    elif ltr.startswith("a") == True:
        ltr = "d"          
    elif ltr.startswith("b") == True:
        ltr = "e"
    elif ltr.startswith("c") == True:
        ltr = "f"
    elif ltr.startswith("d") == True:
        ltr = "g"
    elif ltr.startswith("e") == True:
        ltr = "h"
    elif ltr.startswith("f") == True:
        ltr = "i"
    elif ltr.startswith("g") == True:
        ltr = "j"
    elif ltr.startswith("h") == True:
        ltr = "k"
    elif ltr.startswith("i") == True:
        ltr = "l"
    elif ltr.startswith("j") == True:
        ltr = "m"
    elif ltr.startswith("k") == True:
        ltr = "n"
    elif ltr.startswith("l") == True:
        ltr = "o"
    elif ltr.startswith("m") == True:
        ltr = 'p'
    elif ltr.startswith("n") == True:
        ltr = 'q'
    elif ltr.startswith("o") == True:
        ltr = 'r'
    elif ltr.startswith("p") == True:
        ltr = 's'
    elif ltr.startswith("q") == True:
        ltr = 't'
    elif ltr.startswith("r") == True:
        ltr = 'u'
    elif ltr.startswith("s") == True:
        ltr = 'v'
    elif ltr.startswith("t") == True:
        ltr = 'w'
    elif ltr.startswith("u") == True:
        ltr = 'x'
    elif ltr.startswith("v") == True:
        ltr = 'y'
    elif ltr.startswith("w") == True:
        ltr = 'z'
    elif ltr.startswith("x") == True:
        ltr = 'a'
    elif ltr.startswith("y") == True:
        ltr = 'b'
    elif ltr.startswith("z") == True:
        ltr = 'c'
#nocap^ cap v
    elif ltr.startswith("A") == True:
        ltr = "D"          
    elif ltr.startswith("B") == True:
        ltr = "E"
    elif ltr.startswith("C") == True:
        ltr = "F"
    elif ltr.startswith("D") == True:
        ltr = "G"
    elif ltr.startswith("E") == True:
        ltr = "H"
    elif ltr.startswith("F") == True:
        ltr = "I"
    elif ltr.startswith("G") == True:
        ltr = "J"
    elif ltr.startswith("H") == True:
        ltr = "K"
    elif ltr.startswith("I") == True:
        ltr = "L"
    elif ltr.startswith("J") == True:
        ltr = "M"
    elif ltr.startswith("K") == True:
        ltr = "N"
    elif ltr.startswith("L") == True:
        ltr = "O"
    elif ltr.startswith("M") == True:
        ltr = 'P'
    elif ltr.startswith("N") == True:
        ltr = 'Q'
    elif ltr.startswith("O") == True:
        ltr = 'R'
    elif ltr.startswith("P") == True:
        ltr = 'S'
    elif ltr.startswith("Q") == True:
        ltr = 'T'
    elif ltr.startswith("R") == True:
        ltr = 'U'
    elif ltr.startswith("S") == True:
        ltr = 'V'
    elif ltr.startswith("T") == True:
        ltr = 'W'
    elif ltr.startswith("U") == True:
        ltr = 'X'
    elif ltr.startswith("V") == True:
        ltr = 'Y'
    elif ltr.startswith("W") == True:
        ltr = 'Z'
    elif ltr.startswith("X") == True:
        ltr = 'A'
    elif ltr.startswith("Y") == True:
        ltr = 'B'
    elif ltr.startswith("Z") == True:
        ltr = 'C'    
    elif ltr.startswith(",") == True:
        ltr = ','

    
    result = result + ltr
    msg = msg[1:]
    
print(result)