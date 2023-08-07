class ROI:
    def __init__(self):
        self.form = {
            'Income': {},
            'Expenses': {},
            'Total Investments': {}
        }
#<---------------Total Income--------------->
        self.total_income = 0
        self.rental_income = 0
        self.laundry = 0
        self.storage = 0
        self.misc = 0
#<---------------Total Expenses--------------->
        self.total_expenses = 0
        self.tax = 0
        self.insurance = 0
        self.electric = 0
        self.water = 0
        self.sewage = 0
        self.gas = 0
        self.HOA = 0
        self.lawn_snow = 0
        self.vacancy = 0
        self.repairs = 0
        self.capitalexp = 0
        self.prop_management = 0
        self.mortgage = 0
#<---------------Total Investment--------------->
        self.total_investment = 0
        self.down_payment = 0
        self.closing_costs = 0
        self.rehab = 0
#<---------------ROI--------------->
        self.cashflow = 0
        self.annual_cashflow = 0
        self.ROI = 0

    def make_edits(self):
        while True:
            print("""Thank you for using the ROI Calculator. Please choose from the options below:\n
            \t- 'Edit' To make changes.
            \t- 'Clear' to start over with a fresh form
            \t- 'Done'
            """)
            to_do = input("What would you like to do?: ").lower()
            if to_do == 'edit':
                print()
                print("Section - Income: ")
                print("-----------------")
                for k, v in self.form['Income'].items():
                    print(f"\t~{k}: {v}")
                print(f"Total: {self.total_income}")
                print()
                print("Section - Expenses: ")
                print("-------------------")
                for k, v in self.form['Expenses'].items():
                    print(f"\t~{k}: {v}")
                print(f"Total: {self.total_expenses}")
                print()
                print("Section - Total Investments: ")
                print("---------------------------")
                for k, v in self.form['Total Investments'].items():
                    print(f"\t~{k}: {v}")
                print(f"Total: {self.total_investment}")
                while True:
                    while True:
                        Section = input("What section would you like to make a change in?: ").title()
                        if Section in self.form:
                            break
                        else:
                            continue
                    while True:
                        Key = input(f"What field in {Section} would you like to change?: ").title()
                        if Key in self.form[Section]:
                            break
                        else:
                            continue
                    Value = int(input(f"What is the new Value for {Key}?: "))
                    if Section == 'Income':
                        self.total_income -= self.form[Section][Key]
                        self.form[Section][Key] = Value
                        self.total_income += self.form[Section][Key]
                    if Section == 'Expenses':
                        self.total_expenses -= self.form[Section][Key]
                        self.form[Section][Key] = Value
                        self.total_expenses += self.form[Section][Key]    
                    if Section == 'Total Investments':
                        self.total_investment -= self.form[Section][Key]
                        self.form[Section][Key] = Value
                        self.total_investment += self.form[Section][Key]    
                    print(f"{Section} - {Key} has been updated to {Value}.")
                    to_do = input("Would you like to change more? Y/N: ").lower()
                    if to_do == 'y':
                        continue
                    elif to_do =='n':
                        break
                if to_do == 'n':
                    self.calc_ROI()
            elif to_do == 'clear':
                self.form.clear()
                if not self.form:
                    print('The form is empty. Please run the program again to generate a new form.')
                break
            elif to_do == 'done':
                break

    def calc_ROI(self):
        self.cashflow = self.total_income - self.total_expenses
        self.annual_cashflow = self.cashflow * 12
        self.ROI = self.annual_cashflow / self.total_investment * 100
        print()
        print("Section - Income: ")
        print("-----------------")
        for k, v in self.form['Income'].items():
            print(f"\t~{k}: {v}")
        print(f"Total: {self.total_income}")
        print()
        print("Section - Expenses: ")
        print("-------------------")
        for k, v in self.form['Expenses'].items():
            print(f"\t~{k}: {v}")
        print(f"Total: {self.total_expenses}")
        print()
        print("Section - Total Investments: ")
        print("---------------------------")
        for k, v in self.form['Total Investments'].items():
            print(f"\t~{k}: {v}")
        print(f"Total: {self.total_investment}")
        print()
        print(f"Cash Flow: {self.cashflow}")
        print(f"Annual Cash Flow: {self.annual_cashflow}")
        print(f"Your ROI is {self.ROI:.1f}% per year for this property. ")

    def calc_income(self):
        print()
        print("Section - Income: ")
        print("-----------------")
        self.rental_income = int(input("\t~Rental income: "))
        self.total_income += self.rental_income
        self.form["Income"]['Rental Income'] = self.rental_income
        self.laundry = int(input("\t~Laundry: "))
        self.total_income += self.laundry
        self.form["Income"]['Laundry'] = self.laundry
        self.storage = int(input("\t~Storage: "))
        self.total_income += self.storage
        self.form["Income"]['Storage'] = self.storage
        to_do = input("Do you have other forms of Income? Y/N (Misc): ")
        if to_do == 'y':
            while True:
                name = input("What is the name of this other source of income?: ").title()
                self.misc = int(input(f"\t~{name}: "))
                self.total_income += self.misc
                self.form["Income"][name.title()] = self.misc
                to_do = input("Do you want to add more? Y/N: ")
                if to_do == 'y':
                    continue
                if to_do == 'n':
                    break
        elif to_do == 'n':
            return

    def calc_expenses(self):
        print()
        print("Section - Expenses: ")
        print("-------------------")
        self.tax = int(input("\t~Tax: "))
        self.total_expenses += self.tax
        self.form['Expenses']['Tax'] = self.tax
        self.insurance = int(input("\t~Insurance: "))
        self.total_expenses += self.insurance
        self.form['Expenses']['Insurance'] =  self.insurance
        self.electric = int(input("\t~Electric: "))
        self.total_expenses += self.electric
        self.form['Expenses']['Electric'] = self.electric
        self.water = int(input("\t~Water: "))
        self.total_expenses += self.water
        self.form['Expenses']['Water'] = self.water
        self.sewage = int(input("\t~Sewage: "))
        self.total_expenses += self.sewage
        self.form['Expenses']['Sewage'] = self.sewage
        self.gas = int(input("\t~Gas: "))
        self.total_expenses += self.gas
        self.form['Expenses']['Gas'] = self.gas
        self.HOA = int(input("\t~HOA: "))
        self.total_expenses += self.HOA
        self.form['Expenses']['Hoa'] = self.HOA
        self.lawn_snow = int(input("\t~Lawn/Snow: "))
        self.total_expenses += self.lawn_snow
        self.form['Expenses']['Lawn/snow'] = self.lawn_snow
        self.vacancy = int(input("\t~Vacancy: "))
        self.total_expenses += self.vacancy
        self.form['Expenses']['Vacancy'] = self.vacancy
        self.repairs = int(input("\t~Repairs: "))
        self.total_expenses += self.repairs
        self.form['Expenses']['Repairs'] = self.repairs
        self.capitalexp = int(input("\t~Capital Expenses: "))
        self.total_expenses += self.capitalexp
        self.form['Expenses']['Capital Expenses'] = self.capitalexp
        self.prop_management = int(input("\t~Property Management: "))
        self.total_expenses += self.prop_management
        self.form['Expenses']['Property Management'] = self.prop_management
        self.mortgage = int(input("\t~Mortgage: "))
        self.total_expenses += self.mortgage
        self.form['Expenses']['Mortgage'] = self.mortgage

    def calc_total_investments(self):
        print()
        print("Section - Total Investments:")
        print("----------------------------")
        self.down_payment = int(input("\t~Down Payment: "))
        self.total_investment += self.down_payment
        self.form['Total Investments']['Down Payment'] = self.down_payment
        self.closing_costs = int(input("\t~Closing costs: "))
        self.total_investment += self.closing_costs
        self.form['Total Investments']['Closing Costs'] = self.closing_costs
        self.rehab = int(input("\t~Rehab: "))
        self.total_investment += self.rehab
        self.form['Total Investments']['Rehab'] = self.rehab
        


def main():
    roi = ROI()
    while True:
        print("---------------------------------------------")
        print('|\tWelcome to the ROI Calculator       |')
        print("---------------------------------------------")
        roi.calc_income()
        roi.calc_expenses()
        roi.calc_total_investments()
        roi.calc_ROI()
        roi.make_edits()
        break

main()
