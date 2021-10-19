#last edit was 13/07/19

#for a really specific use case. Rolling for results in a forum game
#required input from a random number generator, and that number determined a user's results

#petal count
p = 0
#rose gem
rg = 0
#sapphire gem
sg = 0
#emerald gem
eg = 0
#peridot gem
pg = 0
#garnet gem
gg = 0
#sunset gem
ssg = 0
#pearl
pea = 0
#sun coin
scoin = 0
#butterflies
blue = 0
orange = 0
pink = 0
purple = 0
green = 0
red = 0
yellow = 0

#for ease
total3p = 0
total4p = 0
total5p = 0

listo = [p,rg, sg, eg, pg, gg, ssg,pea,scoin,blue,orange,pink,purple,green,red,yellow]
listo2 = [" petals,"," rose quartz gem,"," sapphire gem,"," emerald gem,",
          " peridot gem,"," garnet gem,"," sunset gem,"," pearl,"," sun coin,",
          " blue butterfly,"," orange butterfly,"," pink butterfly,",
          " purple butterfly,"," green butterfly,"," red butterfly,",
          " yellow butterfly"]
total = 0

while True:
    num = int(input("Number: "))
    if num == 0:
        break
    if num == 101:
        print("-----------------------------")
    if num == 111:
        '''while total <= 16:
            if listo[total] != 0:
                print(str(listo[total]) + listo2[total])
                total = total + 1
            else:
                total = total + 1'''
        print(str(p) + " petals,",
              str(rg) + " rose quartz gem,",
              str(sg) + " sapphire gem,",
              str(eg) + " emerald gem,",
              str(pg) + " peridot gem,",
              str(gg) + " garnet gem,",
              str(ssg) + " sunset gem,",
              str(pea) + " pearl,",
              str(scoin) + " sun coin,",
              str(blue) + " blue butterfly,",
              str(orange) + " orange butterfly,",
              str(pink) + " pink butterfly,",
              str(purple) + " purple butterfly,",
              str(green) + " green butterfly,",
              str(red) + " red butterfly,",
              str(yellow) + " yellow butterfly,")
        print(" ")
        print("Total num of 3 petals: " + str(total3p))
        print("Total num of 4 petals: " + str(total4p))
        print("Total num of 5 petals: " + str(total5p))
        print(" ")
        print(" ")
        total = 0
        p = 0
        rg = 0
        sg = 0
        eg = 0
        pg = 0
        gg = 0
        ssg = 0
        pea = 0
        scoin = 0
        blue = 0
        orange = 0
        pink = 0
        purple = 0
        green = 0
        red = 0
        yellow = 0
        total3p = 0
        total4p = 0
        total5p = 0
    if 1 <= num <= 5:
        print("1 rose quartz gem")
        print(" ")
        rg = rg + 1
    if 6 <= num <= 10:
        print("1 sapphire gem")
        print(" ")
        sg = sg + 1
    if 11 <= num <= 15:
        print("1 emerald gem")
        print(" ")
        eg = eg + 1
    if 16 <= num <= 20:
        print("1 peridot gem")
        print(" ")
        pg = pg + 1
    if 21 <= num <= 25:
        print("1 garnet gem")
        print(" ")
        gg = gg + 1
    if num == 26:
        print("1 sunset gem")
        print(" ")
        ssg = ssg + 1
    if num == 27:
        print("1 pearl")
        print(" ")
        pea = pea + 1
    if 28 <= num <= 35:
        print("1 sun coin")
        print(" ")
        scoin = scoin + 1
    if 36 <= num <= 40:
        but = int(input("Butterfly: "))
        if 1 <= but <= 15:
            print("Blue")
            print(" ")
            blue = blue + 1
        if 16 <= but <= 30:
            print("Orange")
            print(" ")
            orange = orange + 1
        if 31 <= but <= 45:
            print("Pink")
            print(" ")
            pink = pink + 1
        if 46 <= but <= 60:
            print("Purple")
            print(" ")
            purple = purple + 1
        if 61 <= but <= 75:
            print("Green")
            print(" ")
            green = green + 1
        if 76 <= but <= 90:
            print("Red")
            print(" ")
            red = red + 1
        if 91 <= but <= 100:
            print("Yellow")
            print(" ")
            yellow = yellow + 1
    if 41 <= num <= 55:
        print("5 petals")
        print(" ")
        p = p + 5
        total5p = total5p + 1
    if 56 <= num <= 75:
        print("4 petals")
        print(" ")
        p = p + 4
        total4p = total4p + 1
    if 76 <= num <= 100:
        print("3 petals")
        print(" ")
        p = p + 3
        total3p = total3p + 1
