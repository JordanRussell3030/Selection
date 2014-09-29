#Jordan Russell
#29/09/14
#Selection revision task 4

print("This program will display the largest of your three numbers.")
number_one = float(input("Please input your first number: "))
number_two = float(input("Please input your second number: "))
number_three = float(input("Please input your third number: "))

if (number_one > number_two and number_one > number_three):
    print("Your largest number is {0}.".format(number_one))
elif (number_two > number_one and number_two > number_three):
    print("Your largest number is {0}.".format(number_two))
#improving program to task 6
elif (number_three > number_one and number_three > number_two):
    print("Your largest number is {0}.".format(number_three))
    
    
                   
