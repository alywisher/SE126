#Allison Wisher
#1/31/2024
#Fourth Wing Dragon Data Base -> Midterm



#---- Main Code ----

import csv
with open("midtermIndividual/dragon.csv") as csvFile:
    #Reade from File
    
    file = csv.reader(csvFile)

    for rec in file:

        print(f"{rec[0]:14}\t{rec[1]:16}\t{rec[2]:8}\t{rec[3]:14}\t{rec[4]:8}\t{rec[5]:14}\t{rec[6]:10}\t{rec[7]:14}")

        #dragonName.append(rec[0])

#---- Disconect from csv ----
        
#header:
print("")