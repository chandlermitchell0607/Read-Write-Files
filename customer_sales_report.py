import csv
sales = open("sales.csv", "r")
csv_file = csv.reader(sales)
newfile = open("salesreport.csv", "w")
next(csv_file)
newfile.write("Customer ID, Total\n")
total = 0
CustID = "250"
for rec in csv_file:
    if CustID == rec[0]:
        total = float(rec[3]) + float(rec[4]) + float(rec[5]) + total
    else:
        newfile.write(f"{CustID},{total:.2f}\n")
        CustID = rec[0]
        total = float(rec[3]) + float(rec[4]) + float(rec[5])
newfile.write(f"{CustID},{total:.2f}\n")  