def tot_amount(units):
    if units<=100:
        rate=1.5
        amt=units*rate
    elif units<=200:
        rate1=1.5
        rate2=2.5
        amt=(rate1*units)+(rate2*(units-100))
    elif units<=300:
        rate1=1.5
        rate2=2.5
        rate3=3.5
        amt=(rate1*100)+(rate2*100)+(rate3*(units-200))
    fixed_rate=50
    tot_amount=amt+fixed_rate
    return tot_amount
units=float(input("Enter total amount of units Consumed:"))
tot=tot_amount(units)
print("Electricity bill:$",tot)
