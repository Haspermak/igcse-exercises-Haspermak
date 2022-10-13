SN = ["CHAN","WONG","LEE","LAM","CHEUNG","LEUNG","LAU","TANG","NG","HO","YU","MAK","LO","LIU","YEUNG","LAI","CHUNG","CHU","ZHANG","SO"]
SA = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
AL = ["CHAN", "LIU", "LAM", "WONG", "TANG", "CHU", "LAM", "WONG", "CHUNG", "LIU", "LO","HO", "CHAN", "LEUNG", "TANG", "TANG", "SO", "CHEUNG", "LEE", "CHUNG", "CHEUNG","WONG", "SO", "SO", "CHEUNG", "LEUNG", "LEE", "CHUNG", "NG", "SO", "LEE", "CHEUNG","NG", "YU", "LAI", "TANG", "LAI", "CHU", "ZHANG", "LIU", "CHAN", "YU", "CHUNG","CHUNG", "HO", "LAM", "SO", "CHAN", "CHAN", "CHUNG", "CHEUNG", "LIU", "CHAN", "TANG","LIU", "CHAN", "LEUNG", "YU", "CHEUNG", "TANG", "LAM", "CHUNG", "LIU", "CHU", "LEUNG","LEE", "CHUNG", "CHUNG", "LEUNG", "CHEUNG", "YU", "CHU", "CHAN", "YU", "ZHANG", "YU","YU", "WONG", "LEE", "YU", "TANG", "ZHANG", "CHUNG", "LO", "YU", "LAI", "LEUNG","WONG", "CHU", "LAI", "YU", "CHUNG", "SO", "CHU", "CHAN", "YU", "CHUNG", "WONG","LEUNG", "CHEUNG", "YU", "LEUNG", "YU", "LO", "HO", "LO", "CHAN", "YU", "CHEUNG","LO", "SO", "YU", "LAM", "CHU", "ZHANG", "CHAN", "LAI", "LEUNG", "CHAN", "CHU", "HO","LEUNG", "LIU", "CHEUNG", "CHAN", "HO", "LEE", "CHU", "ZHANG", "CHUNG", "LEUNG","CHU", "LAM", "LAI", "WONG", "WONG", "CHEUNG", "CHAN", "CHAN", "TANG", "LAI", "LEUNG","CHAN", "CHUNG", "CHUNG", "CHU", "CHUNG", "SO", "LAI", "CHU", "CHUNG", "WONG", "LAI","LEUNG", "LAM", "LAM", "HO", "TANG", "CHEUNG", "LIU", "LEUNG", "CHU", "LIU", "LEE","NG", "CHUNG", "LIU", "LAI", "YU"]
O = []
#20 ppl total
CHAN = 0
WONG= 0
LEE = 0
LAM = 0
CHEUNG = 0
LEUNG = 0
LAU = 0
TANG = 0
NG = 0
HO = 0
MAK = 0
YU = 0
LO = 0
LIU = 0
YEUNG = 0
LAI = 0
CHUNG = 0
CHU = 0
ZHANG = 0
SO = 0
test = 0

for n in AL:
    if n.startswith('CHAN') == True:
        CHAN = CHAN + 1
    elif n.startswith('WONG') == True:
        WONG = WONG + 1
    elif n.startswith('LEE') == True:
        LEE = LEE  + 1
    elif n.startswith('LAM') == True:
        LAM = LAM + 1
    elif n.startswith('CHEUNG') == True:
        CHEUNG = CHEUNG + 1
    elif n.startswith('LEUNG') == True:
        LEUNG = LEUNG + 1
    elif n.startswith('LAU') == True:
        LAU = LAU + 1
    elif n.startswith('TANG') == True:
        TANG = TANG + 1
    elif n.startswith('NG') == True:
        NG = NG + 1
    elif n.startswith('HO') == True:
        HO = HO + 1
    elif n.startswith('MAK') == True:
        MAK = MAK + 1
    elif n.startswith('LO') == True:
        LO = LO + 1
    elif n.startswith('LIU') == True:
        LIU = LIU + 1
    elif n.startswith('YEUNG') == True:
        YEUNG = YEUNG + 1
    elif n.startswith('LAI') == True:
        LAI = LAI + 1
    elif n.startswith('CHUNG') == True:
        CHUNG = CHUNG + 1
    elif n.startswith('CHU') == True:
        CHU = CHU + 1
    elif n.startswith('ZHANG') == True:
        ZHANG = ZHANG + 1
    elif n.startswith('SO') == True:
        SO = SO + 1
    elif n.startswith('YU') == True:
        YU = YU + 1
    else:
        test = test + 1
    
 #test is how many things are not accounted fo
SA = [CHAN,WONG,LEE,LAM,CHEUNG,LEUNG,LAU,TANG,NG,HO,YU,MAK,LO,LIU,YEUNG,LAI,CHUNG,CHU,ZHANG,SO]
print(SA)
SA.sort()

for a in SA:
    if a == CHAN:
        O.append("CHAN")
        CHAN = -1
    elif a == WONG:
        O.append("WONG")
        WONG = -1
    elif a == LEE:
        O.append("LEE")
        LEE = -1
    elif a == LAM:
        O.append("LAM")
        LAM = -1
    elif a == CHEUNG:
        O.append("CHEUNG")
        CHEUNG = -1
    elif a == LEUNG:
        O.append("LEUNG") 
        LEUNG = -1
    elif a == LAU:
        O.append("LAU")
        LAU = -1
    elif a == TANG:
        O.append("TANG")
        TANG = -1
    elif a == NG:
        O.append("NG")
        NG = -1
    elif a == HO:
        O.append("HO")
        HO = -1
    elif a == YU:
        O.append("YU")
        YU = -1
    elif a == MAK:
        O.append("MAK")
        MAK = -1
    elif a == LO:
        O.append("LO")
        LO = -1
    elif a == LIU:
        O.append("LIU")
        LIU = -1
    elif a == YEUNG:
        O.append("YEUNG")
        YEUNG = -1
    elif a == LAI:
        O.append("LAI")
        LAI = -1
    elif a == CHUNG:
        O.append("CHUNG")
        CHUNG = -1
    elif a == CHU:
        O.append("CHU")
        CHU = -1
    elif a == ZHANG:
        O.append("ZHANG")
        ZHANG = -1
    elif a == SO:
        O.append("SO")
        SO = -1


    
b = 0
c = []
for d in SA:
    if d == 0:
        b = b + 1
if b != 0:
    
    print(O[:b])
else:
    print("no perfect students")
print(O[19:])
print(SA[19:])





    
        




