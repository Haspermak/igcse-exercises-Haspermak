######THIS CODE HAS THE SIMPLIFIED VERSION OF THE PROBLEM IN MIND AS I DID NOT READ THE FULL TASK PROPERLY
#OITEMS Order items - A list of strings
#OQTY Order quantities - A list of integers
#IPRICES Item prices - A list of integers
#INAMES Item names - A list of strings

#Cheeseburger 7
#Hot dog 3
#Chips 4
#Drink 1

#most ordered
#most revenue 
OITEMS = ['Cheeseburger', 'Hot dog', 'Drink', 'Hot dog', 'Hot dog', 'Cheeseburger', 'Hot dog']
OQTY = [1, 2, 5, 1, 2, 2, 1]
IPRICES = [7, 3, 4, 1]
INAMES = ['Cheeseburger', 'Hot dog', 'Chips', 'Drink']
IMA = [0, 0, 0, 0]
IAMT = [0, 0, 0, 0]
IMA2 = ['a','a','a','a']
itemtype = 0
itemamt = 0
metaphoricalductape = 0
metaphoricalductape1 = 0

replacelater = 0 
replacelater1 = 0
replacelater2 = 0
replacelater3 = 0
replacelater4 = 0
#these are for sorting the ordered list at *
replacelater5 = 0
replacelater6 = 0
replacelater7 = 0
replacelater8 = 0

a = 0
b = 0
c = 0
d = 0


#list.sort() high to low
for n in OITEMS:
    itemtype = OITEMS[metaphoricalductape]#the nth thing in OITEMS
    itemamt = OQTY[metaphoricalductape]
    metaphoricalductape = metaphoricalductape+1
    if itemtype.startswith('Cheeseburger') == True:
        replacelater = PRICES[0]*itemamt
        replacelater1 = replacelater + IMA[0]
        IMA.pop(0)
        IMA.insert(0, replacelater1)
        
    if itemtype.startswith('Hot dog') == True:
        replacelater = PRICES[1]*itemamt
        replacelater2 = replacelater + IMA[1]
        IMA.pop(1)
        IMA.insert(1, replacelater2)
    if itemtype.startswith('Drink') == True:
        replacelater = PRICES[2]*itemamt
        replacelater3 = replacelater + IMA[2]
        IMA.pop(2)
        IMA.insert(2, replacelater3)
    if itemtype.startswith('Chips') == True:
        replacelater = PRICES[3]*itemamt
        replacelater4 = replacelater + IMA[3]
        IMA.pop(3)
        IMA.insert(3, replacelater4)
#################################################################################################################################################
    metaphoricalductape = metaphoricalductape + 1
replacelater5 = IMA[0]
replacelater6 = IMA[1]
replacelater7 = IMA[2]
replacelater8 = IMA[3]
IMA.sort()
for i in IMA:
    metaphoricalductape2 = metaphoricalductape2 + 1
    if i == replacelater5:
        
    
        
        
        