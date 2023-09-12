import csv
customers = open("customers.csv", "r")
csv_file = csv.reader(customers)
newfile = open("customer_country.csv", "w")
next(csv_file) #this skips a row
total = 0
newfile.write("Full Name, Country\n")
for rec in csv_file:
    newfile.write(f"{rec [1]} {rec [2]}, {rec [4]}\n")
    total += 1
print(f"The total number of customers is {total}")   # input() #see one record at a time
newfile.close()