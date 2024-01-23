#w3d1 Demo - text file and storing to 1D lists 

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
        print(f"{compType:8} \t{manu:8} \t{processor:10} \t{ram:6} \t{hdd1:6} \t{numHdd:6} \t{hdd2:6} \t{os:6} \t{year:6}")



#-- Disconected from file --

print("\n------------------------------------------------------------------------------------------------------------------")
print(f"TOTAL RECORDS: {totalRecords}")

#-- Process through the list to print machine data -- 

for index in range(0, totalRecords):
    #for index range(0, len(compType)): --> len(compType) returns the INTIGER count of values
    print(f"{compTypeList[index]:8} \t{manuList[index]:8} \t{processorList[index]:10} \t{ramList[index]:6} \t{hdd1List[index]:6} \t{numHddList[index]:6} \t{hdd2List[index]:6} \t{osList[index]:6} \t{yearList[index]:6}")

#-- process the list to : count the number of desctops --
desktopCount = 0
for index in range(0, len(compTypeList)):


    #look through the compTypeList to find "Desktop"
    if compTypeList[index] == "Desktop" and int(yearList[index]) <= 16:
        #if int(yearList[index]) <= 16 --> nested if works too
        desktopCount += 1 #adds 1 everytime "Desktop" is found

print(f"TOTAL DESKTOPS IN FILE: {desktopCount}")

# -- len() --> length function; when passed a (list) it returns an integer: # of values in list --


#-- process the list to : find avrage hdd1 size --

totalSize = 0 
countSize = 0

for index in range(0, len(hdd1List)):
    if hdd1List[index] == "001TB":
        totalSize += 1
    else:
        totalSize += 0.5

    countSize += 1

average = totalSize / countSize

print(f"AVG HDD#1 SIZE: {average:0.2f}TB or {average*1000:0.2f}GB")