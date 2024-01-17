#allison wisher, lab2b
#prompt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output. The last line should print the number of computers in the file

#import
import csv 

totalRecords = 0 

with open() as csvfile:

    file = csv.reader("week2/hw/lab2b.csv")

    for rec in file:

        #----------values for field one---------
        
        if rec[0] == "D":
            compType = "Desktop"
        elif rec[0] == "L":
            compType = "Laptop"
        else: 
            compType = "-ERROR-"

        #--------storing value for var rep field 2--------- 
            
        if rec[1] == "DL": 
            manu = "Dell"
        elif rec[1] == "HP":
            manu = rec[1]
        elif rec[1] == "GW":
            manu = "Gateway"
        else: 
            manu = "-ERROR-"

        #------storeing for field2, field3, field4, field5--------
        
        processor = rec[2]
        ram = rec[3]
        hdd1 = rec[4]
        numHdd = rec[5]
        

        #final printed message for eatch machine

        print(rec)
        print(f"{compType} {manu} {processor} {ram} {hdd1} {numHdd} {os} {year}")