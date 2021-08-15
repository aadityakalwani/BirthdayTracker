# ciao
# may the coding begin

import json

with open("birthdays.json") as f:
    birthdays = json.load(f)

    begin_loop: str = input("At any time you can press q to quit.\n"
                            "type 'date' to search by date\n"
                            "type 'name' to search by name\n"
                            "Enter your command here: ").lower()

    if begin_loop.lower() == "q":
        print("You have quit this loop.")

    if begin_loop.lower() == "name":
        while True:
            name: str = input("This will search the dict for a person.\nEnter their name here: ")
            if name.lower() == "q":
                print("You have quit this loop.")
                break

            if name in birthdays:
                print("their name is in the dict.")
                print(f"{name}'s birthday is on {birthdays[name][0]}-{birthdays[name][1]}")

            else:
                new_birthday = input(f"{name} is not in this dictionary.\nEnter their birthday: ")
                if name.lower() == "q":
                    print("You have quit this loop.")
                    break
                birthdays.setdefault(name, new_birthday)

    if begin_loop.lower() == "date":
        print("You have chosen the 'date' option.\n"
              "This will now show all birthdays occurring in the month you select.\n")
        month: str = input("Enter a month:")

        print(f"{month} contains the birthdays of ")


# you can use for value in d.values() and for key, value in d.items() to make it use something else

# how to order/sort the dict:
# the key here is not to use a dictionary
# OrderedDict() I think?
# Convert the dict to a list of pairs (tuples), sort the list, then construct a dict out of it

# make it so that i can also input a date and it tells me if there is a birthday on that date
# as well as th next x amount of birthdays

# is it possible/how can i turn a number into a month of the year? (eg. 1 = "january", 4 = "april")
# yes, you can use the calender module or datetime
# the calendar module should have that @Aadi
