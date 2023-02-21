import webbrowser

from fpdf import FPDF

class Bill:
    """
    Object containing data about bill,
    including amount and period of bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates flatmate who lives in flat and
    pays their share of bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = weight * bill.amount
        return to_pay

class PdfReport:
    """
    Creates PDF file including flatmate names, individual
    amounts due, and period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=12, style='B')
        pdf.cell(w=100, h=25, txt="Period:", border=0)
        pdf.cell(w=150, h=25, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln = 1)

        # Insert name and due amount of first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln = 1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)



the_bill = Bill(amount = 120, period = "April 2023")
bob = Flatmate(name="Bob", days_in_house=20)
david = Flatmate(name="David", days_in_house=25)

print("Bob owes: ", bob.pays(bill=the_bill, flatmate2=bob))
print("David owes: ", david.pays(bill=the_bill, flatmate2=david))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=bob, flatmate2=david, bill=the_bill)