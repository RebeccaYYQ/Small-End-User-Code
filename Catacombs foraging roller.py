#last edit was 25/09/19

#for a really specific use case. Rolling for results on a forum game.

import random

#----Functions
#to generate another result
def other_result():
  #roll for one of them
  tempnum = random.randint(1,4)
  if tempnum == 1:
    #print("leaf")
    currency("leaf")
  elif tempnum == 2:
    #print("berry")
    currency("berry")
  elif tempnum == 3:
    #print("crystal")
    currency("crystal")
  elif tempnum == 4:
    #print("mushroom")
    currency("mushroom")
    
#to generate dust results
def dust_result():
  #roll
  tempnum = random.randint(1,2)
  if tempnum == 1:
    #print("fire dust")
    currency("fire")
  elif tempnum == 2:
    #print("ice dust")
    currency("ice")
  
#calculate currency rolls
def currency(item):
  #50% chance of currency. If one, then yes currency
  cur = random.randint(1,2)
  if cur == 1:
    cur_num = random.randint(1,10)
    #print("currency true")
    
  #store the result, no currency
  if cur == 2:
    if item == "leaf":
      result.append(" tangy leaf [img]https://cdn.discordapp.com/attachments/356166901644263425/608477696267386881/tangy_leaf.png[/img]! [+7 EXP]")
    elif item == "berry":
      result.append("sweet berries [img]https://cdn.discordapp.com/attachments/356166901644263425/608480776949858309/Sweet_Berries.png[/img]! [+7 EXP]")
    elif item == "crystal":
      result.append("shield crystal [img]https://cdn.discordapp.com/attachments/356166901644263425/613020240153935883/shield_crystal.png[/img]! [+7 EXP]")
    elif item == "mushroom":
      result.append("hearty mushroom [img]https://cdn.discordapp.com/attachments/356166901644263425/608475669487288331/Healthy_Mushroom.png[/img]! [+7 EXP]")
    elif item == "fire":
      result.append("firesprite dust [img]https://cdn.discordapp.com/attachments/356166901644263425/609225970058264592/firesprite.png[/img]! [+7 EXP]")
    elif item == "ice":
      result.append("freezesprite dust [img]https://cdn.discordapp.com/attachments/356166901644263425/609225944393056266/freezesprite.png[/img]! [+7 EXP]")
    
  #store the result, yes currency
  elif cur == 1:
    if item == "leaf":
      result.append(" tangy leaf [img]https://cdn.discordapp.com/attachments/356166901644263425/608477696267386881/tangy_leaf.png[/img] and " + str(cur_num) + " currency! [+7 EXP]")
    elif item == "berry":
      result.append("sweet berries [img]https://cdn.discordapp.com/attachments/356166901644263425/608480776949858309/Sweet_Berries.png[/img] and " + str(cur_num) + " currency! [+7 EXP]")
    elif item == "crystal":
      result.append("shield crystal [img]https://cdn.discordapp.com/attachments/356166901644263425/613020240153935883/shield_crystal.png[/img] and " + str(cur_num) + " currency! [+7 EXP]")
    elif item == "mushroom":
      result.append("hearty mushroom [img]https://cdn.discordapp.com/attachments/356166901644263425/608475669487288331/Healthy_Mushroom.png[/img] and " + str(cur_num) + " currency! [+7 EXP]")
    elif item == "fire":
      result.append("firesprite dust [img]https://cdn.discordapp.com/attachments/356166901644263425/609225970058264592/firesprite.png[/img] and " + str(cur_num) + " currency! [+7 EXP]")
    elif item == "ice":
      result.append("freezesprite dust [img]https://cdn.discordapp.com/attachments/356166901644263425/609225944393056266/freezesprite.png[/img] and " + str(cur_num) + " currency! [+7 EXP]")
    
#-----------------------------mainline----------------------------------

result = []
name_list = []

#Instructions
print("Catacombs Foraging Roller!")
print("")
print("Instructions:")
print(" - Enter the cat's name and level. Please be aware of repeating cat names - this program does not check for duplicates.")
print(" - THIS IS IMPORTANT: Enter 'done' instead of a cat's name when finished, AND enter a number between 0-10 for the cat level. The 'done' is case-sensitive, and the level must be within that range else the program will break and you will have to refresh the page.")
print(" - Again, enter 'done' and a number between 0-10 for the level input to finish the program.")
print("")
print("Once that is done, the results should be displayed, which you can then copy and paste!")
print("")

name = input("Cat name: ")
lvl = int(input("Cat level: "))
num = 0


while name != "done":
  name_list.append(name)
  num = num + 1
  dust = False
  
  #random numbers according to level
  if lvl == 0:
    lvlran = random.randint(1,100)
  elif lvl == 1:
    lvlran = random.randint(1,75)
  elif lvl == 2:
    lvlran = random.randint(1,50)
  elif lvl == 3:
    lvlran = random.randint(1,40)
  elif lvl == 4:
    lvlran = random.randint(1,30)
  elif lvl == 5:
    lvlran = random.randint(1,25)
  elif lvl == 6:
    lvlran = random.randint(1,20)
  elif lvl == 7:
    lvlran = random.randint(1,15)
  elif lvl == 8:
    lvlran = random.randint(1,10)
  elif lvl == 9:
    lvlran = random.randint(1,7)
  elif lvl == 10:
    lvlran = random.randint(1,5)
  
  #print("random number as a result of level: " + str(lvlran))
  
  #if the random number result is 1, give dust. Else generate another outcome
  if lvlran == 1:
    dust_result()
  else:
    other_result()
  
  #get inputs again
  print("")
  name = input("Cat name: ")
  lvl = int(input("Cat level: "))
  
#print the results
print("")
print("[center]【﻿ＦＯＲＡＧＩＮＧ　ＲＥＳＵＬＴＳ】[/center]")
print("[list][list][size=85]")
for i in range(num):
  print(name_list[i] + " recieves a " + result[i])
print("[/size][/list][/list]")
