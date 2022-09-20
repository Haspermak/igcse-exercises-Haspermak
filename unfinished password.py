password = input("input a password:")
cap = 0
low = 0
pun = 0
num = 0
a = 1
b = a + 1

end = ""
p2 = password[a:a]
#p2 is first digit plus a
while p2 != end:
    
    if p2.isnumeric == True:
        num = num + 1
    
    if p2.isupper == True:
        cap = cap + 1

    if p2.islower == True:
        low = low + 1

    if p2.isnumeric == False:
        if p2.isalpha == False:
            pun = pun + 1
    
    a = a + 1
    p2 = p2[a:a]
    


if cap > 0:
    if low > 0:
        if pun > 0:
            if num > 0:
                print("valid")
                
            else:
                print("invalid")
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")






