'''
Author: Nithish Aravinthan
KUID: 3211410
Date: 3/3/2026
Lab: lab05
Last modified: 3/5/2026
Purpose: Perform operations on a string
'''


string = input("What is your string: ")
length = len(string)

is_manipulating = True

while is_manipulating:
    print("1) Shift left",
          "2) Shift right",
          "3) Reverse",
          "4) Mirror",
          "5) Exit", sep="\n")
    
    choice = input("\nchoice: ")
    if choice == "1":
        new_string = string[1:length]
        new_string = new_string + string[0]

        string = new_string

    elif choice == "2":
        new_string = string[0:length-1]
        new_string = string[length-1] + new_string

        string = new_string

    elif choice == "3":
        string = string[::-1]

    elif choice == "4":
        mid_index = length // 2
        lower_half = string[0:mid_index]
        upper_half = lower_half[::-1]

        mid_character = ""
        if (length % 2) == 1:
            mid_character = string[mid_index]

        string = lower_half + mid_character + upper_half

    elif choice == "5":
        is_manipulating = False

    else:
        print("Bad input: choice does not exist")

    print("\n" + string + "\n")
    print("="*72)
    print("")