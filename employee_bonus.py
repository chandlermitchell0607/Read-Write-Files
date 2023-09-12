import csv
employees = open("EmployeePay.csv", "r")
csv_file = csv.reader(employees)
next(csv_file)
for rec in csv_file:
    bonus = int(rec[3]) * (float(rec[4])+1)
    total = int(rec[3]) + bonus
    print(f" First Name: {rec[1]}\n Last Name: {rec[2]}\n Salary: ${rec[3]}\n Bonus: ${bonus:,.2f}\n Total Pay: ${total:,.2f}")
    input()
