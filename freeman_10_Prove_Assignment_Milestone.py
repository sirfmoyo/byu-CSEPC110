"""
Author          :       Freeman Moyo
Course          :       CSEPC 110
Assignment      :       09 Prove: Assignment Milestone for week 10
Created         :       13 November 2022
Modified        :       20 November 2022
"""


import sys
print('Welcome to the Shopping Cart Program!')
shop_list ={}
def repeat():
    menu = input('Please select one of the following:\n 1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit\n: ')

    if menu == '1':
        while True:
          shop_item = input('Please enter name of item to buy and press "ENTER"\n: ')
          item_price = float(input('Please enter price of ' + shop_item.upper() + ' to buy and press "ENTER"\n: '))
          print(shop_item.capitalize() + ' has been to the cart')
          item_price = "{:.2f}".format(item_price)
          shop_list[shop_item] = item_price
          check = input("Do you want to add another item to the cart or quit?\nEnter A to add another item or M to view main menu or or Q key to quit\n: ")
          if check.upper() == "A":  # to add to cart
              continue
          elif check.upper() == "M": #go back to the top
            repeat()
            # continue
          # print("Bye...")
          elif check.upper() == "Q":  # to quit
              print('The contents of the shopping cart are:')
              for i, (key, value) in enumerate(shop_list.items(), start=1):
                  print(i, key, value)
                  values = shop_list.values()
                  for key, value in shop_list.items():
                      shop_list[key] = float(value)
                  total = sum(values)
                  print('The total price of the items in the shopping cart is $', end=" ")
                  print(total)
              break #exit
          else:
              print('Invalid prompt')
              break

          # repeat()
    elif menu == '2':
        print('The contents of the shopping cart are:')
        for i, (key, value) in enumerate(shop_list.items(), start=1):
            print(i, key, value)
        repeat()

    elif menu == '3':
        while True:
            remove_item = input('Do you want to remove anything from the list? Y/N: ')

            print('The contents of the shopping cart are:')
            for i, (key, value) in enumerate(shop_list.items(), start=1):
                print(i, key, value)

            remove_item = remove_item.capitalize()
            print(remove_item)

            while remove_item != 'N':
                selection = int(input('Please select the number of the item to remove\n: '))
                selection = selection - 1
                print(selection)

                keys = list(shop_list.keys())
                print('Your item ' + keys[selection].upper() + ' will be removed from the list')

                shop_list.pop(keys[selection])
                print('Your new contents of the shopping cart are:')
                for i, (key, value) in enumerate(shop_list.items(), start=1):
                    print(i, key, value)
                print('Now going back to the main menu')
                print()
                repeat()
    elif menu == '4':
        print('Your final contents of the shopping cart are:')
        for i, (key, value) in enumerate(shop_list.items(), start=1):
            print(i, key, value)
        values = shop_list.values()
        for key, value in shop_list.items():
            shop_list[key] = float(value)


        total = sum(values)
        print('The total price of the items in the shopping cart is $', end=" ")
        print(total)
        repeat()
    elif menu == '5':
        print('Thank you, goodbye.')
        sys.exit()
    else:
        print('You selected a wrong option.')
        repeat()

repeat()