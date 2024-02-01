#Allison Wisher
#1/31/2024
#Fourth Wing Dragon Data Base -> Midterm

#menu Function

#variable names: dragonName, namePronounce, nickName, meaning, color, type, riderFname, riderLname
#def menu():

#---- print colums ----
#print(f"{rec[0]:14}\t{rec[1]:16}\t{rec[2]:8}\t{rec[3]:14}\t{rec[4]:8}\t{rec[5]:14}\t{rec[6]:10}\t{rec[7]:14}")


#---- MAIN CODE ----
dragonName = []
namePronounce = []
nickName = []
meaning = []
color = []
dragonType = [] 
riderFname = []
riderLname = []
#---- MAIN HEADER PRINT ----
print("-----------------------------------------------------------------------------------")
print("\t\t\tWelcome to the Basgiath War College Dragon Encyclopedia")
print("-----------------------------------------------------------------------------------")

import csv
with open("midtermIndividual/dragon.csv") as csvFile:
    #Reade from File
    
    file = csv.reader(csvFile)

    for rec in file:
        dragonName.append(rec[0])
        namePronounce.append(rec[1])
        nickName.append(rec[2])
        meaning.append(rec[3])
        color.append(rec[4])
        dragonType.append(rec[5])
        riderFname.append(rec[6])
        riderLname.append(rec[7])
        

        #dragonName.append(rec[0])

#---- Disconect from csv ----
        
#header:
print("")