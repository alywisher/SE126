import csv

#initlize counting variables
total_records = 0

total_salaries = 0

#intilize empty list - 1 list per field 
names = []
ages = []
salaries = []

#connect to file

with open("week2/demo/example.csv") as unicorn:

    #read the file - acess
    file = csv.reader(unicorn)

    #go in and read the eatch record in the file

    for rec in file:
        # for every record found in file (entire row in field data)

        #display the data value in neat colums
        print(f"{rec[0]:10} \t{rec[1]:3} \t{rec[2]:10}")

        #store data from rec list (currently being read) to list 
        #adding data to a list --> .append() ; requires LIST NAME as string object

        names.append(rec[0]) #names
        ages.append(int(rec[1])) #ages
        salaries.append(float(rec[2])) #salaries 
 
        #keep literal count of number of records 
        total_records += 1 

        #keep running total of salaries
        total_salaries += float(rec[2])

#final displays
print(f"TOTAL RECORDS: {total_records} TOTAL SALARY: $ {total_salaries:.2f}")

#process the list to diplay the text file information
#process list --> for loop

for index in range(0, total_records): 
    #for each value in the range of 0 to number of values in total_records
    print(f"INDEX:{index} \t {names[index]} is {ages[index]} years old")

total_age = 0 

#processing a list to creat a total age value
for index in range(0, total_records):
    #add eatch age to a total age variable 
    total_age += ages[index]

#determin the avrage age, then display
avrage_age = total_age / total_records 
print(f"AVERAGE AGE:{avrage_age:.2f} ")

