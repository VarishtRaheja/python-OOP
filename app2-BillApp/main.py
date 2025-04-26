# Importing required libraries
import os.path
import webbrowser
from fpdf import FPDF as pdf
import re
import atexit

# Global variables
cpi = (341.468, 349.135, 370.199, 399.643, 412.857)
years = (2020, 2021, 2022, 2023, 2024)

# def adjusted_rent():
#     user_year = int(input("Enter the year: "))
#     adj_rent = rate.get(list(rate)[-1]) / rate.get(user_year) * total_rent
#     return adj_rent


rate = dict(zip(years, cpi))


# Creating a bill class
class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        rent = bill.amount * weight
        return rent


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, name1, flatmate2, bill):
        # Creating a pdf file
        read_pdf = pdf(orientation="P", unit="pt", format='A4')
        read_pdf.add_page()

        # Add icon
        read_pdf.image(name="house.png", w=60, h=60)

        # Insert title

        read_pdf.set_font(family="Times", size=24, style='B')
        read_pdf.cell(w=0, h=80, txt='Rent Due', border=0, align='C', ln=1)

        # Insert period and value

        read_pdf.set_font(family="Times", size=12)
        read_pdf.cell(w=100, h=40, txt='Period: ', border=1)
        read_pdf.set_font(family="Times", size=12, style='I')
        read_pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name1 name and amount

        read_pdf.set_font(family="Times", size=12)
        read_pdf.cell(w=100, h=40, txt=name1.name + ":", border=1)
        read_pdf.set_font(family="Times", size=12, style='I')
        read_pdf.cell(w=150, h=40, txt=str(round(name1.pays(bill=the_bill, flatmate2=flatmate2), 2)), border=1, ln=1)

        # Insert flatmate2 name and amount

        read_pdf.set_font(family="Times", size=12)
        read_pdf.cell(w=100, h=40, txt=flatmate2.name + ":", border=1)
        read_pdf.set_font(family="Times", size=12, style='I')
        read_pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill=the_bill, flatmate2=flatmate1), 2)), border=1,
                      ln=1)

        # Generating pdf output
        read_pdf.output(self.filename)
        webbrowser.open("file://" + os.path.realpath(self.filename))


# User input functions

total_rent = round(float(input("Enter your total rent for the month: ")), 2)
user_period = input("Enter the period of rent, (eg: December 2023): ").capitalize()
name1 = input("Enter the name of the first flatmate: ")
user_days_in_house1 = int(input(f"The number of days {name1} stays in the house: "))
name2 = input("Enter the name of the other flatmate: ")
user_days_in_house2 = int(input(f"The number of days {name2} stays in the house: "))

# Functions called

the_bill = Bill(amount=total_rent, period=user_period)
flatmate1 = Flatmate(name=name1, days_in_house=user_days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=user_days_in_house2)
pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
temp_user_year = re.findall(r'\d+', the_bill.period)
user_year = int("".join(map(str, temp_user_year)))

# Printing statements
print("The total rent for {} is: {:.2f} ".format(flatmate1.name, flatmate1.pays(bill=the_bill, flatmate2=flatmate2)))
print("The total rent for {} is: {:.2f} ".format(flatmate2.name, flatmate2.pays(bill=the_bill, flatmate2=flatmate1)))
pdf_report.generate(name1=flatmate1, flatmate2=flatmate2, bill=the_bill)
print("The rent of the period, {0}, is: {1}".format(the_bill.period, the_bill.amount))
adjusted_rent = rate.get(list(rate)[-1]) / rate.get(user_year) * total_rent
print("The adjusted rent for the current year is: {:0.2f}".format(adjusted_rent))



# CPI in 2024 / CPI in 2020 * 2020 USD value = 2024 USD value
# print("The rectangle area is: {0}".format(rectangle.area()))
