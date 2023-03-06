from flatBill import Bill, Flatmate
from pdfSetup import PdfReport

amount = float(input("Hello, please enter the bill amount:  "))
period = input("Which period is the bill for? Example: April 2021 ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during bill period?"))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during bill period?"))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} owes: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} owes: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
