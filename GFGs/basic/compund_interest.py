#compund interest

def compound_interest(principal,rate,time):
    amount = principal*pow((1+rate/100),time)
    CI = amount - principal
    print("compound intererst is",CI)
    
compound_interest(1000,7.25,2)
