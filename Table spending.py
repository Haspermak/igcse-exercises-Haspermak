table = ['J', 'D', 'J', 'G', 'G', 'C', 'K', 'F', 'C', 'C', 'E', 'E', 'J', 'C', 'H', 'K', 'H', 'F', 'G', 'K', 'K', 'K', 'H', 'E', 'J', 'B', 'C', 'E', 'H', 'G', 'H', 'J', 'I', 'B', 'B', 'G', 'J', 'H', 'B', 'B', 'B', 'I', 'H', 'D', 'E', 'I', 'A', 'I', 'J', 'I', 'H', 'A', 'D', 'F', 'H', 'B', 'E', 'K', 'C', 'K', 'I', 'F', 'G', 'K', 'G', 'A', 'J', 'K', 'B', 'K', 'K', 'D', 'D', 'H', 'B', 'I', 'K', 'F', 'G', 'I', 'C', 'H', 'E', 'H', 'D', 'J', 'C', 'A', 'J', 'I', 'J', 'G', 'J', 'C', 'J', 'I', 'H', 'I', 'D', 'E']
spending = [163, 446, 384, 214, 439, 448, 323, 344, 48, 155, 373, 369, 418, 477, 144, 297, 290, 33, 172, 16, 383, 57, 160, 289, 382, 418, 113, 284, 179, 229, 468, 368, 252, 428, 315, 93, 247, 260, 84, 327, 404, 443, 121, 184, 383, 55, 125, 237, 485, 476, 110, 83, 29, 294, 115, 361, 333, 186, 65, 247, 492, 199, 11, 13, 12, 476, 207, 181, 239, 387, 63, 79, 196, 334, 433, 242, 98, 126, 485, 111, 262, 470, 360, 48, 413, 74, 132, 320, 121, 500, 365, 356, 484, 261, 245, 83, 311, 376, 210, 400]
unique = ['A',  'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
spend2 = 0
table2 = "a" #str

for tablenumber in range(len(table)):
    spend2 = spending[tablenumber] #Spending corrisponding with table No
    table2 = table[tablenumber] #Table number str()**
    
    if table2.startswith('A') == True:
        spend2 = spend2 + totals[0]
        totals.pop(0)
        totals.insert(0, spend2)
    if table2.startswith('B') == True:
        spend2 = spend2 + totals[1]
        totals.pop(1)
        totals.insert(1, spend2)
    if table2.startswith('C') == True:
        spend2 = spend2 + totals[2]
        totals.pop(2)
        totals.insert(2, spend2)
    if table2.startswith('D') == True:
        spend2 = spend2 + totals[3]
        totals.pop(3)
        totals.insert(3, spend2)
    if table2.startswith('E') == True:
        spend2 = spend2 + totals[4]
        totals.pop(4)
        totals.insert(4, spend2)
    if table2.startswith('F') == True:
        spend2 = spend2 + totals[5]
        totals.pop(5)
        totals.insert(5, spend2)
    if table2.startswith('G') == True:
        spend2 = spend2 + totals[6]
        totals.pop(6)
        totals.insert(6, spend2)
    if table2.startswith('H') == True:
        spend2 = spend2 + totals[7]
        totals.pop(7)
        totals.insert(7, spend2)
    if table2.startswith('I') == True:
        spend2 = spend2 + totals[8]
        totals.pop(8)
        totals.insert(8, spend2)
    if table2.startswith('J') == True:
        spend2 = spend2 + totals[9]
        totals.pop(9)
        totals.insert(9, spend2)
    if table2.startswith('K') == True:
        spend2 = spend2 + totals[10]
        totals.pop(10)
        totals.insert(10, spend2)
    
    table.pop(0)
    spending.pop(0)
    print(totals)

    
#     table.pop(0)
#  spending.pop(0)
#those at end ^^^
    
    





abcdefghijk