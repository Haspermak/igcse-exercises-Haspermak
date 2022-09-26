numbers = []
ammout = input("input a number")
listpart = 9
ammout = int(ammout)
for n in range (0, ammout):
    
    listpart = input("input a number")
    numbers.append(listpart)
    
print(numbers)
highest = 0
lowest = 0
for n in range(0, len(numbers)):
    print(numbers[n])
    if highest < numbers[n]:
        highest = numbers[n]
        
for n in range(0, len(numbers)):
    print(numbers[n])
    if lowest > numbers[n]:
        lowest = numbers[n]