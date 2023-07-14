"""
Name    :   Freeman Moyo
Date created :  10 November 2022
Modificattion date:

"""

"""
Ask the user for the names of their friends and append them to a list. 
Then, display each of the friends in the list. 
You should stop asking for friends when the user types "end".
"""

# i will create an empty list called variable
# ask user to name a friend
# add name of friend using the append command
# iterate through a while loop
# as long as friend name is not end

friends=[]
name = ''
while name !='end':
    name = input('Please write the name of your friend and press enter or write "end" of you are done\n: ')


    # here only append of the input is not 'end'
    # it had skipped me
    if name!='end':
        friends.append(name)

    #this will print the whole list
    print(friends)

    # so what i have to do is to iterate through the whole list
    # and print each friend separately

for i in friends:
    print(i)