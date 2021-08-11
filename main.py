# ciao
# may the coding begin

import json

with open("birthdays.json") as f:
    birthdays = json.load(f)

while True:

    name: str = input("At any time, you can press q to quit.\nEnter a name: ").lower()

    if name.lower() == "q":
        print("You have quit this loop.")
        break

    if name in birthdays:
        print(f"{name}'s birthday is on {birthdays[name]}")

    else:
        new_birthday = input(f"{name} is not in this dictionary.\nEnter their birthday: ")
        birthdays.setdefault(name, new_birthday)
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
