#allison wisher, lab2b
#prompt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output. The last line should print the number of computers in the file

#import
import csv 

#total counter for all records 

totalRecords = 0

#creat lists - one for eatch potetial feild in file

compTypeList = []
manuList = []
processorList = []
ramList = []
hdd1List = []
numHddList = []
hdd2List = []
osList = []
yearList = []

#--- Headers ---

print(f"\n{'TYPE':8} \t{'MANU':8} \t{'PROCCESOR':10} \t{'RAM':3} \t{'HDD 1':5} \t{'# HDD':5} \t{'HDD 2':6} \t{'OS':6} \t{'YEAR':6}")
print("--------------------------------------------------------------------------------------------------------------------------")

with open("week3/demo/lab2b.csv") as csvFile: 

    file = csv.reader(csvFile)

    for rec in file:

        #print(rec) #show as a list -> []

        #keep track of the rec count in the file 
        totalRecords += 1 

        #filter system
        #compType -- rec[0] 
        if rec[0] == "D":
            compType = "Desktop"
        elif rec[0] == "L":
            compType = "Laptop"
        else:
            compType = "*ERROR --*" +str(rec[0])

        #manu -- rec[1]
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu = "*ERROR --*" +str(rec[0])

        #-- preocessor / ram / hdd1 / numHdd - exact from file --
            
        processor = rec[2]
        ram = rec[3]
        hdd1 = rec[4]
        numHdd = rec[5]

        if rec[5] == "1":
            hdd2 = "---"
            os = rec[6]
            year = rec[7]
        elif rec[5] == "2":
            hdd2 = rec[6]
            os = rec[7]
            year = rec[8]
        else: 
            hdd2 = ("*ERROR -- ") +str(rec[5])
            os = ("ERROR")
            year = ("ERROR")
        

        #-- append respective values to the appropreate field list --
            
        compTypeList.append(compType)
        manuList.append(manu)
        processorList.append(processor)
        ramList.append(ram)
        hdd1List.append(hdd1)
        numHddList.append(numHdd)
        hdd2List.append(hdd2)
        osList.append(os)
        yearList.append(year)
        

        #final print
        #print(f"{compType:8} \t{manu:8} \t{processor:10} \t{ram:6} \t{hdd1:6} \t{numHdd:6} \t{hdd2:6} \t{os:6} \t{year:6}")



#-- Disconected from file --




#-- Process through the list to print machine data -- 

for index in range(0, totalRecords):
    #for index range(0, len(compType)): --> len(compType) returns the INTIGER count of values
    print(f"{compTypeList[index]:8} \t{manuList[index]:8} \t{processorList[index]:10} \t{ramList[index]:6} \t{hdd1List[index]:6} \t{numHddList[index]:6} \t{hdd2List[index]:6} \t{osList[index]:6} \t{yearList[index]:6}")

print(f"TOTAL RECORDS: {totalRecords}")