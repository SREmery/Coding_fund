def getIncomeTax(salary):
    if salary <= 11850:
        return 0
    elif salary >= 11851 or salary <= 34500:
        return (salary * 20) / 100 
    elif salary >= 34501 or salary <= 150000:
        return(salary * 40) / 100
    elif salary > 150000:
        return(salary * 45) / 100
        
salary = 100000
tax_amount = getIncomeTax(salary)
print("Tax amount for salary £{} is £{}".format(salary,tax_amount))
   
