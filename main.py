# ciao
# may the coding begin

birthdays = {
    "Bhavya": "January 1st, 2006"
            }


while True:

    name = input("At any time, you can press q to quit.\nEnter a name: ")

    if name.lower() == "q":
        print("You have quit this loop.")
        break

    if name in birthdays:
        print(f"{name}'s birthday is on {birthdays[name]}")

    else:
        print(f"{name} is not in this dictionary.")
        bday = input("Enter their birthday: ")

        if bday.lower() == "q":
            print("You have quit this loop.")
            break

        birthdays[name] = bday
        print("Birthdays database and dictionary updated.")
