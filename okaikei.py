
# coding: utf_8
##strictìãç⁄
dif = 0
difn = 0
i = 0
j = 0
k = 0
pricemod = 0
ppp = ""
mtr = ""
mode = ""
n = 5*[0]
N = 4*[0]
paa = 5*[0]
print "1îNê∂âΩêl?",

n[0] = raw_input()
if n[0] == "":
    n[0] = 0
if n[0] == "strict" or n[0] == "mild" or n[0] == "Mild":
    mode = n[0]
    print "1îNê∂âΩêl?",
    n[0] = raw_input()
    if n[0] == "":
        n[0] = 0
    if n[0] == "p" or n[0] == "P":
        ppp = n[0]
        print "1îNê∂âΩêl?",
        n[0] = raw_input()
        if n[0] == "":
            n[0] = 0

    n[0] = int(n[0])

if n[0] == "p" or n[0] == "P":
        ppp = n[0]
        print "1îNê∂âΩêl?",
        n[0] = raw_input()
        if n[0] == "":
            n[0] = 0

if n[0] != "p" and n[0] != "P" and n[0] != "strict" and n[0] != "mild" and n[0] != "Mild":
    
    n[0] = int(n[0])


print "2îNê∂âΩêl?",
n[1] = raw_input()
if n[1] == "":
    n[1] = 0
n[1] = int(n[1])

print "3îNê∂âΩêl?",
n[2] = raw_input()
if n[2] == "":
    n[2] = 0
n[2] = int(n[2])

print "4îNê∂âΩêl?",
n[3] = raw_input()
if n[3] == "":
    n[3] = 0
n[3] = int(n[3])
print "OBGâΩêl?",
n[4] = raw_input()
if n[4] == "":
    n[4] = 0
n[4] = int(n[4])

print "çáåvÇ¢Ç≠ÇÁ?",
price = input()
totalp = 0

if ppp == "p" or ppp == "P":
    print"àÍîNê∂Ç¢Ç≠ÇÁ?",
    k = input()
    pricemod = price - (k * n[0])
else:
    pricemod = price

#àÍîN500ÉpÉ^Å[Éì
maxg = 0
if n[4] != 0:
    maxg  = 4
elif n[3] != 0:
    maxg = 3
elif n[2] != 0:
    maxg = 2
elif n[1] != 0:
    maxg = 1

i = 1

j = 0
nsum = n[1] + n[2] + n[3] + n[4]
ave = pricemod / nsum

p =4*[0]
temp = 0
while i <= maxg:
    if n[i] != 0:
        N[j] = n[i]
        paa[j] = str(i+1) + "îNê∂"
        if i == 4:
            paa[j] = "OBG"
        j += 1
        i += 1
        
    else:
        i += 1
j -= 1
def funca():
    while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0:
                            
                                break
                            p[1] = p[1] - 100
                       
                                                                 
                        break
                    else:
                        while True:
                                               
                            difn = difn + N[1]
                            if difn > 0:
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0:
                            
                                break
                            p[0] = p[0] + 100
                        
                        break

def wasshoi(x, y, z):
    if j == 1:
        temp = ave * x
        p[1] = temp + (100 - (temp  % 100))
        temp = ave * 0.9
        p[0] = temp - (temp  % 100)

        totalp = (p[1] * N[j]) + (p[0] * N[j-1])
        
        dif = totalp - pricemod
        difn = dif / 100
        while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0:
                            
                                break
                            p[1] = p[1] - 100
                       
                                                                 
                        break
                    else:
                        while True:
                                               
                            difn = difn + N[1]
                            if difn > 0:
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0:
                            
                                break
                            p[0] = p[0] + 100
                        
                        break
        totalp = (p[1] * N[j]) + (p[0] * N[j-1])  + (k * n[0])
        print "åv: %1.f"  % totalp  + "â~"
        print"~~~~~~~~~~"
        print str(paa[j]) + ": %1.f"  % p[1]  + "â~"
        print str(paa[j-1]) + ": %1.f"  % p[0]  + "â~"
        temp = p[1] * N[j]
        print" "
        print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
        temp = p[0] * N[j-1]
        print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
        print"ÇæÇﬂÅH"
        a = raw_input()
        if a == "ÇæÇﬂ":
            temp = ave * y
            p[1] = temp + (100 - (temp  % 100 ))
            temp = ave * 0.8
            p[0] = temp - (temp  % 100)
            totalp = (p[1] * N[j]) + (p[0] * N[j-1]) + (k * n[0])
            
            dif = totalp - price
            difn = dif / 100
            while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0:
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0: 
                            
                                break
                            p[1] = p[1] - 100
                       
                                                                 
                        break
                    else:
                        while True:
                                               
                            difn = difn + N[1]
                            if difn > 0: 
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0:
                            
                                break
                            p[0] = p[0] + 100
                        
                        break
            totalp = (p[1] * N[j]) + (p[0] * N[j-1]) + (k * n[0])
            print "åv: %1.f"  % totalp  + "â~"
            print"~~~~~~~~~~"
            print str(paa[j]) + ": %1.f"  % p[1]  + "â~"
            print str(paa[j-1]) + ": %1.f"  % p[0]  + "â~"
            temp = p[1] * N[j]
            print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
            temp = p[0] * N[j-1]
            print" "
            print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
            print"ÇæÇﬂÅH"
            a = raw_input()
            if a == "ÇæÇﬂ":
                temp = ave * z
                p[1] = temp + (100 - (temp  % 100 ))
                temp = ave * 0.7
                p[0] = temp - (temp  % 100)
                totalp = (p[1] * N[j]) + (p[0] * N[j-1])  + (k * n[0])
                
                dif = totalp - price
                difn = dif / 100
                while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0: 
                            
                                break
                            p[1] = p[1] - 100
                       
                                                                 
                        break
                    else:
                        while True:
                                               
                            difn = difn + N[1]
                            if difn > 0: 
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0:
                            
                                break
                            p[0] = p[0] + 100
                        
                        break
                totalp = (p[1] * N[j]) + (p[0] * N[j-1]) + (k * n[0])
                print "åv: %1.f"  % totalp  + "â~"
                print"~~~~~~~~~~"
                print str(paa[j]) + ": %1.f"  % p[1]  + "â~"
                print str(paa[j-1]) + ": %1.f"  % p[0]  + "â~"
                temp = p[1] * N[j]
                print" "
                print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
                temp = p[0] * N[j-1]
                print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
            else:
                print("Ç®Ç§")
        else:
            print("Ç®Ç§")
    if j == 2:
        temp = ave * x
        p[2] = temp + (100 - (temp  % 100))
        p[1] = ave + (100 - (ave  % 100 ))
        temp = ave * 0.9
        p[0] = temp - (temp  % 100)
        totalp = (p[2] * N[j]) + (p[1] * N[j-1]) + (p[0] * N[j-2])
       
        dif = totalp - pricemod
        difn = dif / 100
        while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0: 
                            
                                break
                            p[1] = p[1] - 100
                        
                            difn = difn - N[2]
                            if difn < 0: 
                            
                                break
                            p[2] = p[2] - 100
                                                                 
                        break
                    else:
                        while True:
                        
                            difn = difn + N[2]
                            if difn > 0: 
                            
                                break
                            p[2] = p[2] + 100
                        
                            difn = difn + N[1]
                            if difn > 0: 
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0: 
                            
                                break
                            p[0] = p[0] + 100
                        
                        break

                     
        totalp = (p[2] * N[j]) + (p[1] * N[j-1]) + (p[0] * N[j-2]) + (k * n[0])
        print "åv: %1.f"  % totalp  + "â~"
        print"~~~~~~~~~~"
        print str(paa[j]) + ": %1.f"  % p[2]  + "â~"
        print str(paa[j-1]) + ": %1.f"  % p[1]  + "â~"
        print str(paa[j-2]) + ": %1.f"  % p[0]  + "â~"
        temp = p[2] * N[j]
        print" "
        print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
        temp = p[1] * N[j-1]
        print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
        temp = p[0] * N[j-2]
        print str(paa[j-2]) + "ëSëÃ: %1.f"  % temp  + "â~"
        print"ÇæÇﬂÅH"
        a = raw_input()
        if a == "ÇæÇﬂ":
            temp = ave * y
            p[2] = temp + (100 - (temp  % 100))
            p[1] = ave + (100 - (ave  % 100 ))
            temp = ave * 0.8
            p[0] = temp - (temp  % 100)
            
            totalp = (p[2] * N[j]) + (p[1] * N[j-1]) + (p[0] * N[j-2])  + (k * n[0])
            
            dif = totalp - pricemod
            difn = dif / 100
            while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0: 
                            
                                break
                            p[1] = p[1] - 100
                        
                            difn = difn - N[2]
                            if difn < 0: 
                            
                                break
                            p[2] = p[2] - 100
                                                                 
                        break
                    else:
                        while True:
                        
                            difn = difn + N[2]
                            if difn > 0: 
                            
                                break
                            p[2] = p[2] + 100
                        
                            difn = difn + N[1]
                            if difn > 0: 
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0: 
                            
                                break
                            p[0] = p[0] + 100
                        
                        break
    
            totalp = (p[2] * N[j]) + (p[1] * N[j-1]) + (p[0] * N[j-2])  + (k * n[0])
            print "åv: %1.f"  % totalp  + "â~"   
            print"~~~~~~~~~~"
            print str(paa[j]) + ": %1.f"  % p[2]  + "â~"
            print str(paa[j-1]) + ": %1.f"  % p[1]  + "â~"
            print str(paa[j-2]) + ": %1.f"  % p[0]  + "â~"
            temp = p[2] * N[j]
            print" "
            print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
            temp = p[1] * N[j-1]
            print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
            temp = p[0] * N[j-2]
            print str(paa[j-2]) + "ëSëÃ: %1.f"  % temp  + "â~"
            print"ÇæÇﬂÅH"
            a = raw_input()
            if a == "ÇæÇﬂ":
                temp = ave * z
                p[2] = temp + (100 - (temp  % 100))
                p[1] = ave + (100 - (ave  % 100 ))
                temp = ave * 0.7
                p[0] = temp - (temp  % 100)
                
                totalp = (p[2] * N[j]) + (p[1] * N[j-1]) + (p[0] * N[j-2]) 
                
                dif = totalp - pricemod
                difn = dif / 100
                while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0: 
                            
                                break
                            p[1] = p[1] - 100
                        
                            difn = difn - N[2]
                            if difn < 0: 
                            
                                break
                            p[2] = p[2] - 100
                                                                 
                        break
                    else:
                        while True:
                        
                            difn = difn + N[2]
                            if difn > 0: 
                            
                                break
                            p[2] = p[2] + 100
                        
                            difn = difn + N[1]
                            if difn > 0: 
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0: 
                            
                                break
                            p[0] = p[0] + 100
                        
                        break

            



                totalp = (p[2] * N[j]) + (p[1] * N[j-1]) + (p[0] * N[j-2]) + (k * n[0])
                print "åv: %1.f"  % totalp  + "â~"
                print"~~~~~~~~~~"
                print str(paa[j]) + ": %1.f"  % p[2]  + "â~"
                print str(paa[j-1]) + ": %1.f"  % p[1]  + "â~"
                print str(paa[j-2]) + ": %1.f"  % p[0]  + "â~"
                print" "
                temp = p[2] * N[j]
                print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
                temp = p[1] * N[j-1]
                print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
                temp = p[0] * N[j-2]
                print str(paa[j-2]) + "ëSëÃ: %1.f"  % temp  + "â~"
            else:
                print("Ç®Ç§")

        else:
            print("Ç®Ç§")
    if j == 3:
        temp = ave * x
        p[3] = temp + (100 - (temp  % 100))
        temp = ave * 1.1
        p[2] = temp + (100 - (temp  % 100))
        temp = ave * 0.9
        p[1] = temp - (temp  % 100 )
        temp = ave * 0.8
        p[0] = temp - (temp  % 100)
        
        totalp = (p[3] * N[j]) + (p[2] * N[j-1]) + (p[1] * N[j-2]) + (p[0] * N[j-3])
        
        dif = totalp - pricemod
        difn = dif / 100   
        while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0: 
                            
                                break
                            p[1] = p[1] - 100
                        
                            difn = difn - N[2]
                            if difn < 0: 
                            
                                break
                            p[2] = p[2] - 100
                        
                            difn = difn - N[3]
                            if difn < 0: 
                            
                                break
                            p[3] = p[3] - 100
                        
                        break
                    else:
                        while True:
                            difn = difn + N[3]
                            if difn > 0: 
                            
                                break
                            p[3] = p[3] + 100
                        
                            difn = difn + N[2]
                            if difn > 0: 
                            
                                break
                            p[2] = p[2] + 100
                        
                            difn = difn + N[1]
                            if difn > 0: 
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0: 
                            
                                break
                            p[0] = p[0] + 100
                        
                        break
        totalp = (p[3] * N[j]) + (p[2] * N[j-1]) + (p[1] * N[j-2]) + (p[0] * N[j-3]) + (k * n[0])
        print "åv: %1.f"  % totalp  + "â~"
        print"~~~~~~~~~~"
        print str(paa[j]) + ": %1.f"  % p[3]  + "â~"
        print str(paa[j-1]) + ": %1.f"  % p[2]  + "â~"
        print str(paa[j-2]) + ": %1.f"  % p[1]  + "â~"
        print str(paa[j-3]) + ": %1.f"  % p[0]  + "â~"
        print" "
        temp = p[3] * N[j]
        print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
        temp = p[2] * N[j-1]
        print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
        temp = p[1] * N[j-2]
        print str(paa[j-2]) + "ëSëÃ: %1.f"  % temp  + "â~"
        temp = p[0] * N[j-3]
        print str(paa[j-3]) + "ëSëÃ: %1.f"  % temp  + "â~"
        
        
        print"ÇæÇﬂÅH"
        a = raw_input()
        
        if a == "ÇæÇﬂ":
            temp = ave * y
            p[3] = temp + (100 - (temp  % 100))
            temp = ave * 1.15
            p[2] = temp + (100 - (temp  % 100))
            temp = ave * 0.85
            p[1] = temp + (100 - (temp  % 100 ))
            temp = ave * 0.7
            p[0] = temp - (temp  % 100)
            
            totalp = (p[3] * N[j]) + (p[2] * N[j-1]) + (p[1] * N[j-2]) + (p[0] * N[j-3])
            
            dif = totalp - pricemod
            difn = dif / 100
            while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                                break
                            p[0] = p[0] - 100
                            difn = difn - N[1]
                            if difn < 0: 
                                break
                            p[1] = p[1] - 100
                            difn = difn - N[2]
                            if difn < 0: 
                                break
                            p[2] = p[2] - 100 
                            difn = difn - N[3]
                            if difn < 0: 
                                break
                            p[3] = p[3] - 100
                        break
                    else:
                        while True:
                            difn = difn + N[3]
                            if difn > 0: 
                                break
                            p[3] = p[3] + 100
                            difn = difn + N[2]
                            if difn > 0: 
                                break
                            p[2] = p[2] + 100
                            difn = difn + N[1]
                            if difn > 0: 
                                break
                            p[1] = p[1] + 100
                            difn = difn + N[0]
                            if difn > 0: 
                                break
                            p[0] = p[0] + 100
                        break
            totalp = (p[3] * N[j]) + (p[2] * N[j-1]) + (p[1] * N[j-2]) + (p[0] * N[j-3]) + (k * n[0])
            print "åv: %1.f"  % totalp  + "â~"
            print"~~~~~~~~~~"
            print str(paa[j]) + ": %1.f"  % p[3]  + "â~"
            print str(paa[j-1]) + ": %1.f"  % p[2]  + "â~"
            print str(paa[j-2]) + ": %1.f"  % p[1]  + "â~"
            print str(paa[j-3]) + ": %1.f"  % p[0]  + "â~"
            temp = p[3] * N[j]
            print" "
            print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
            temp = p[2] * N[j-1]
            print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
            temp = p[1] * N[j-2]
            print str(paa[j-2]) + "ëSëÃ: %1.f"  % temp  + "â~"
            temp = p[0] * N[j-3]
            print str(paa[j-3]) + "ëSëÃ: %1.f"  % temp  + "â~"
            print"ÇæÇﬂÅH"
            a = raw_input()
            if a == "ÇæÇﬂ":
                temp = ave * z
                p[3] = temp + (100 - (temp  % 100))
                temp = ave * 1.15
                p[2] = temp + (100 - (temp  % 100))
                temp = ave * 0.85
                p[1] = temp + (100 - (temp  % 100 ))
                temp = ave * 0.7
                p[0] = temp - (temp  % 100)
               
                totalp = (p[3] * N[j]) + (p[2] * N[j-1]) + (p[1] * N[j-2]) + (p[0] * N[j-3])
                
                dif = totalp - pricemod
                difn = dif / 100
                while True:
                
                    if difn == 0:
                        break
                    elif difn > 0:
                        while True:
                            difn = difn - N[0]
                            if dif < 0: 
                            
                                break
                            p[0] = p[0] - 100
                        
                            difn = difn - N[1]
                            if difn < 0: 
                            
                                break
                            p[1] = p[1] - 100
                        
                            difn = difn - N[2]
                            if difn < 0: 
                            
                                break
                            p[2] = p[2] - 100
                        
                            difn = difn - N[3]
                            if difn < 0: 
                            
                                break
                            p[3] = p[3] - 100
                        
                        break
                    else:
                        while True:
                            difn = difn + N[3]
                            if difn > 0: 
                            
                                break
                            p[3] = p[3] + 100
                        
                            difn = difn + N[2]
                            if difn > 0: 
                            
                                break
                            p[2] = p[2] + 100
                        
                            difn = difn + N[1]
                            if difn > 0: 
                            
                                break
                            p[1] = p[1] + 100
                        
                            difn = difn + N[0]
                            if difn > 0: 
                            
                                break
                            p[0] = p[0] + 100
                        
                        break

                totalp = (p[3] * N[j]) + (p[2] * N[j-1]) + (p[1] * N[j-2]) + (p[0] * N[j-3]) + (k * n[0])
                print "åv: %1.f"  % totalp  + "â~"
                print"~~~~~~~~~~"
                print str(paa[j]) + ": %1.f"  % p[3]  + "â~"
                print str(paa[j-1]) + ": %1.f"  % p[2]  + "â~"
                print str(paa[j-2]) + ": %1.f"  % p[1]  + "â~"
                print str(paa[j-3]) + ": %1.f"  % p[0]  + "â~"
                print" "
                temp = p[3] * N[j]
                print str(paa[j]) + "ëSëÃ: %1.f"  % temp  + "â~"
                temp = p[2] * N[j-1]
                print str(paa[j-1]) + "ëSëÃ: %1.f"  % temp  + "â~"
                temp = p[1] * N[j-2]
                print str(paa[j-2]) + "ëSëÃ: %1.f"  % temp  + "â~"
                temp = p[0] * N[j-3]
                print str(paa[j-3]) + "ëSëÃ: %1.f"  % temp  + "â~"
            else:
                print("Ç®Ç§")

        else:
            print("Ç®Ç§")

if mode == "strict":
    if maxg == 4: 
        wasshoi(3, 5, 7)
    else: 
        wasshoi(2, 3, 3)
elif mode == "mild" or mode == "Mild":
    if maxg == 4: 
        wasshoi(1.2, 1.4, 1.6)
    else: 
        wasshoi(1.05, 1.1, 1.15)
else:
    if maxg == 4: 
        wasshoi(1.6, 1.8, 2.0)
    else: 
        wasshoi(1.1, 1.2, 1.3)


print "1îNê∂" + ": %1.f"  % k + "â~"