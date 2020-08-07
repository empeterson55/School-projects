#Compound interest calculator

P = float(input("Principal investment amount : "))

r = float(input("Annual interest rate : "))

n = float(input("Number of times interest is compounded per year : "))

t = float(input("Number of years the money is invested or borrowed : "))

A = P * (1 + (r/100/n))**(n*t)

print("The Principal amount would grow to : $", A)

