
enone = 0
entwo = 0
answer = 0
od = True
soxnight = 0
numbers = []

ammout = input("input a how many items are there ")
listpart = 9
ammout = int(ammout)

for n in range (0, ammout):
    listpart = int(input("input a number "))
    numbers.append(listpart)
ammout = str(ammout)
numbers.sort()

if int(ammout)%2 == 0:
    od = False
ammout = int(ammout)
ammout = ammout/2
numbers = list(numbers)

if od == True:
    numbers = list(numbers)
    while ammout >= 1:
        numbers = list(numbers)
        numbers.pop(0)
        numbers.pop()
        ammout = ammout-1
    print(numbers)
elif od == False:
    numbers = list(numbers)
    while ammout >= 2:
        numbers = list(numbers)
        numbers.pop(0)
        numbers.pop()
        ammout = ammout-1
    enone = numbers[0]
    entwo = numbers[1]
    answer = enone + entwo
    answer = answer/2
    print(answer)

#10
#123 148 134 150 155 170 138 163 149 148
#148.5