"""
Assignment:     03 Prove: Milestone - Meal Price Calculator
    author:     Freeman Moyo
    Date created: 30 September 2022
    Date modified: 
"""

"""
Ask the user for the following:

    The price of a child's meal (floating point)

    The price of an adult's meal (floating point)

    The number of children (integer)

    The number of adults (integer)

    The sales tax rate (floating point)

Then, complete the following steps:

    Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the 
    price of their meal, and multiplying the number of adults by the price of their meal 
    and adding those two values together.

    Display the subtotal.
"""

print('Good day to you, I hope you are happy and doing great')
print('I am an interactive Bot, I am here to compute the price of your meals after including sales tax')
print('Thank you for your time, please follow the prompts as they come')
print()
child_meal = input('Please enter the price of the child\'s meal and press enter\n:US$ ')
adult_meal = input('Please enter the price of the adult\'s meal and press enter\n:US$ ')
drink_price =  input('Please enter the price of drinks and press enter\n:US$ ')
children_number = input('Please enter the number of  children and press enter\n: ')
adult_number = input('Please enter the number of  adults and press enter\n: ')
drink_number = input('Please enter the number of drinks needed and press enter\n: ')
salestax =  input('Please enter the sales tax rate and press enter\n: % ')

children_total = (float(child_meal)*int(children_number)) 
adult_total = (float(adult_meal)*int(adult_number))
drink_total = (float(drink_price) * int(drink_number))
subtotal = ("%.2f" % (children_total + adult_total + drink_total))
total_tax = ("%.2f" % (float(subtotal) * float(salestax) / 100))
grand_total = ("%.2f" % (float(subtotal) + float(total_tax)))

# here we prompt the user if they want to pay a tip
# the tip value (tip_amount) is set to $0, just in case the person does not want to pay the tip
# however if the person pays the tip, the tip value will change
tip_amount=float(0)
tip = input('Would you like to give the waiter a tip?\Y/N: ')
if tip == 'Y':
    print('Thank you very much for the tip')
    tip_amount=input('Please enter the ip amount and press enter\nUS$: ')
else:
	print('Ok, thank you')

print('The subtotal price is US$' + str(subtotal))
print('The total sales tax is US$' + str(total_tax))
print('The tip is US$' + str(tip_amount))

# we then add the amount of the tip here 
total_payable = ("%.2f" % (float(grand_total) + float(tip_amount)))
print('The total payable amount is US$' + str(total_payable))
total_amount = input('Please enter the total amount you are paying and press enter\n:US$ ')
change = ("%.2f" % (float(total_amount) - float(total_payable)))
print()
print('Your change is US$' + str(change))
print('Thank you so much for using our interactive Bot, hoping to meet you soon.')