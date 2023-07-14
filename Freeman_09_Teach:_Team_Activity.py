"""
Name:       Freeman Moyo
Created:    10 November 2022
Modified: 
"""

"""

Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.

Once you have a list, have your program do the following:
Core Requirements

Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

    Compute the sum, or total, of the numbers in the list.

    Compute the average of the numbers in the list.

    Find the maximum, or largest, number in the list.


"""
import math 

number_list=[]
number=''
print('Please enter a list of numbers,\nenter each number and press ENTER\nwhen you no-longer have a number, please enter the number 0')

# only ask for input if the number entered is not 0
when number !=0:
    number=input('Please enter a number and press ENTER or 0 when you are done\n: ')
    
    # only append when the input is not 0
    # otherwise do not append 
    if number != 0:
        number_list.append(number)

# now using the math library 
