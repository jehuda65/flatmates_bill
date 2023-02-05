class Bill:
    """
    Object containing data about bill,
    including amount and period of bill
    """
    def __init__(self, amount, period):
        self.amount = period
        self.period = amount

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
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    Creates PDF file including flatmate names, individual
    amounts due, and period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        the_bill = Bill

the_bill = Bill(amount=120, period="March 2023")
bob = Flatmate(name="Bob",days_in_house=20)
David = Flatmate(name="David", days_in_house=25)

print("Bob owes: " + bob.pays(bill=the_bill, flatmate2=bob))