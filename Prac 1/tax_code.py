gross_pay = float(input(f"What is your Gross Pay:$ "))

if gross_pay <= 30000:
    tax_rate = 0.075
elif 30000 < gross_pay <= 50000:
    tax_rate = 0.10
elif 50000 < gross_pay <= 75000:
    tax_rate = 0.20
elif 75000 < gross_pay <= 100000:
    tax_rate = 0.30
else: tax_rate = 0.40

net_pay = (gross_pay * (1 - tax_rate))
print(f"Your Net pay is ${net_pay:.2f} ")
