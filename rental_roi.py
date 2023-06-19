class rentalProperty():
    def __init__(self):
        self.property_name = input('Please enter the name of the property.')
        self.rental_income = float(input("What is the expected rental income per month in dollars? "))
        self.laundry_income = float(input("On this property, what is the expected laundry income per month in dollars? "))
        self.storage_income = float(input("On this property, what is the expected storage income per month in dollars? "))
        self.misc_income = float(input("Enter any other miscelaneous income for this property (if none, enter 0): "))
        self.total_income = self.rental_income + self.laundry_income + self.storage_income + self.misc_income
        print(f'Your total estimated income on this property is ${self.total_income}')
        print("Now we'll calculate your expenses on the property.")
        self.tax = float(input("What is the expected property tax per month in dollars? "))
        self.insurance = float(input("What is the expected insurance cost per month? "))
        self.utilities_y = input("Will you as the owner be resposible for monthly utilities like water and electric? (type 'Yes' or 'No') ")
        if self.utilities_y.lower() == 'yes' or self.utilities_y.lower() == 'y':
            self.electric = float(input("What is the expected electric cost per month in dollars? "))
            self.water = float(input("What is the expected water cost per month in dollars? "))
            self.sewer = float(input("What is the expected sewer cost per month in dollars? "))
            self.garbage = float(input("What is the expected garbage cost per month in dollars? "))
            self.gas = float(input("What is the expected gas cost per month in dollars? "))
            self.utilities = self.electric + self.water + self.sewer + self.garbage + self.gas
            print(f'Your total estimated utilities expenses are ${self.utilities}')
        else:
            self.utilities = 0   
        self.hoa = float(input("What is the expected HOA fee per month in dollars? "))
        self.lawn_snow = float(input("What are the expected lawncare and/or snow removal costs per month in dollars? "))
        self.vacancy = float(input("How much will you save per month to cover expenses on the property when it is vacant? "))
        self.repairs = float(input("How much will you save per month for repairs on the property? "))
        self.cap_expenditures = float(input("How much will you save per month for capital expenditures on the property? "))
        self.prop_manage = float(input("What are the expected costs per month for a property manager? "))
        self.mortgage = float(input("What is the monthly mortgage payment per month in dollars? "))
        self.total_expenses = self.tax + self.insurance + self.utilities + self.hoa + self.lawn_snow + self.vacancy + self.repairs + self.cap_expenditures + self.prop_manage + self.mortgage
        print(f'Your total monthly expenses on the property are estimated to be ${self.total_expenses}\n')
        self.cash_flow = self.total_income - self.total_expenses
        print(f'Given the figures you have entered, your monthly cashflow on this property is expected to be ${self.cash_flow}')
        if self.cash_flow <= 0:
            print('Your income will not cover your expenses. This may not be a good investment. If you believe this is an error, please check your figures and run the program again.')
            return
        print('Now we will calculate your expected Cash on Cash Return on Investment (ROI).')
        self.down_payment = float(input("What is your expected down payment on the property in dollars? "))
        self.closing_costs = float(input("What are the expected closing costs on the property? "))
        self.rehab = float(input("What is the expected rehab budget on the property? "))
        self.misc_other = float(input("Enter any other initial investment costs here: "))
        self.total_investment = self.down_payment + self.closing_costs + self.rehab + self.misc_other
        print(f'Your total investment for this property is ${self.total_investment}')
        self.annual_cashflow = 12 * self.cash_flow
        print(f"Your annual cashflow on the {self.property_name} property is ${self.annual_cashflow}\n")
        self.coc_roi_percent = 100 * (self.annual_cashflow / self.total_investment)
        print(f"Finally, the figure you've been waiting for. Your Cash on Cash Return on Investment (ROI) percentage is {self.coc_roi_percent}%")

           

print("Welcome to the Rental Property Return on Investment Calculator")

new_property = rentalProperty()




