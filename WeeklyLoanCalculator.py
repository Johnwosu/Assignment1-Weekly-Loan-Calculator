#---Weekly Loan Calculator--->

#--Inputs will get the following:---
# 1. The Loan 
# 2. The interest rate (%)
# 3. The number of years for the repayment

#---Calculations!----
# 1. Get the weekly interest rate from the anual
# 2. Apply the amortization formular

#---Output-----

#--Inputs---------#
amountOfLoan = float(input("Enter the amount of loan: "))
annualInterestRate = float(input("Enter the interest rate (%): "))
numberOfYears = int(input("Enter the number of years: "))

#--Calculations--
weeklyInterestRate = (annualInterestRate / 100) / 52

#--Amortization formula---

U