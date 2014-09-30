#Jordan Russell
#30/09/14
#Selection development task 3

print("This program will calculate your gross pay.")
hours_worked = int(input("Please input the amount of hours you have worked this week: "))
rate_of_pay = float(input("Please input your hourly rate of pay: "))
extra_pay = (hours_worked - 40) * 1.5

if hours_worked <= 40:
    print("This week your pay is {0}.".format(rate_of_pay * hours_worked))


elif hours_worked > 40:
          print("This week your pay is {0}.".format(rate_of_pay * hours_worked + extra_pay))
else:
    print("That is invalid.")
    
