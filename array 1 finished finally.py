
numbers = []
highest = 0
lowest = 9999999999999999999999999999999999999
dtw = 0
doesnwork = 0
pp = 0
ammout = input("input a how many items are there ")
listpart = 9
ammout = int(ammout)
for n in range (0, ammout):
    listpart = int(input("input a number "))
    numbers.append(listpart)
    
for i in numbers:
    if i < lowest:
        lowest = i
    if i > highest:
        highest = i
        
for l in numbers:
    dtw = l + dtw
    doesnwork = doesnwork+1



#input test1:
#10
# 123 148 134 150 155 170 138 163 149 148
#147.8 47.0




highest = int(highest)
lowest = int(lowest)  
e = float(highest - lowest)
pp = dtw/doesnwork
print(f"{pp} {e}")


 