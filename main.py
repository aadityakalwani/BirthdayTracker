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
        print("You have quit.")

    if begin_loop.lower() == "name":
        while True:
            name: str = input("This will search the dict for a person.\nEnter their name here: ")
            if name in birthdays:
                print(f"{name}'s birthday is on {birthdays[name]}")

            else:
                new_birthday = input(f"{name} is not in this dictionary.\nEnter their birthday: ")
                birthdays.setdefault(name, new_birthday)

                # this is all the code that i used to run in this else statement
                # now its a lot shorter using the set and get

                # bday = input("Enter their birthday: ")
                #
                # if bday.lower() == "q":
                #     print("You have quit this loop.")
                #     break
                #
                # birthdays[name] = bday
                # with open("birthdays.json", "w") as f:
                #     json.dump(birthdays, f, indent=2)
                # print("Birthdays database and dictionary updated.")

# how to order/sort the dict:
# the key here is not to use a dictionary
# OrderedDict() I think?
# Convert the dict to a list of pairs (tuples), sort the list, then construct a dict out of it

# make it so that i can also input a date and it tells me if there is a birthday on that date
# as well as th next x amount of birthdays
