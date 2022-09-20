number = input("input a number: ")
number = int(number)
a = 1
b = 1
c = 0
#fibbonat
while c < number:
    c = a + b
    a = b
    b = c 
print(c)
    
