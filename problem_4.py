
base_salary = float(input("enter base salary: "))
experience = float(input("enter your work experience: "))
if experience <= 5:
    pf = 0.12
else:
    pf = 0.24

net_salary = base_salary - (base_salary * pf)
print("net salary recieved after deduction:",net_salary)
