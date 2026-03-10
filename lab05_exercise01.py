'''
Author: Nithish Aravinthan
KUID: 3211410
Date: 3/3/2026
Lab: lab05
Last modified: 3/5/2026
Purpose: Interactive grocery list allowing user to add and remove items,
    and see entire list
'''


grocery_list = []
is_shopping = True

while is_shopping:
    print("Welcome to your Shopping List!")
    print("1) Add item",
          "2) Check off item",
          "3) Print list",
          "4) Exit", sep="\n")
    choice = input("Enter a choice: ")
    if choice == "1":
        item = input("What will you add to the list?: ")
        grocery_list.append(item)
        
    elif choice == "2":
        entered_index = int(input("Which item will you check off?: "))
        index = entered_index - 1
        item = grocery_list[index]
        grocery_list[index] = item[0] + ("-"*(len(item)-2)) + item[-1]

    elif choice == "3":
        print("Here is your list: ")
        for index, item in enumerate(grocery_list):
            print(f"\t{index+1}) {item}")

    elif choice == "4":
        is_shopping = False
        print("Goodbye!")

    else:
        print("Bad input: choice does not exist")

    print("")
    print("="*72)
    print("")
    
