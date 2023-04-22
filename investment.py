interest_rate = (input("Your interest rate is calculated at 10%")) 
investment = (input("Your initial investment is £100"))
target_val = (input("Your target value is £1000"))

intr_rte = 10 
invm = 100
targ_val = 1000

years = 0 
while invm < targ_val:
    invm *= (1 + intr_rte / 100.0)
    years += 1

print(f"It will take {years} years for your investment to grow to £1000")

