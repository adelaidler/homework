
import sys

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
#len to find length of string
print(len(Belgium))
Belgium2 = len(Belgium)

#wasnt able to replace whole string with -
if Belgium2 in range(0,90):
   print(Belgium.replace(str(Belgium), "-"))
#replace , with :
Belgium3 = Belgium.replace(",", ":")
print(Belgium3)

#elims eliminates selected object
elims = Belgium3.split(":")
print(elims[1])
print(elims[3])

#print(int("___") changes string to number
print(int(elims[1]))
print(int(elims[3]))
#now changed to number so add two elims together
addition_answer = int(elims[1]) + int(elims[3])
print("The Population of Belgium added to the Population of Brussels is:")
print(addition_answer)

