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

    def pays(self, bill):
        pass

class PdfReport:
    """
    Creates PDF file including flatmate names, individual
    amounts due, and period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass
