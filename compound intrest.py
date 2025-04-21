def calculate_compound_intrest(principal,rate,time):
    rate_decimal = rate/100
    amount=principal*(1+rate_decimal)**time
    compound_intrest=amount=amount-principal
    return compound_intrest
principal=float(input("enter the principal amount:"))
rate=float(input("enter the annnual intrest rate (in percentage):"))
time=float(input("enter the number of periods:"))
intrest=calculate_compound_intrest(principal,rate,time)
print(f"the compound intrest is :{intrest:.2f}")
