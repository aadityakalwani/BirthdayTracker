# ciao
# may the coding begin

birthdays = {
    "Bhavya": "January 1st, 2006"
            }


while True:
    name = input("At any time, you can press q to quit.\nEnter a name: ")

    if name.lower == "q":
        break

    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")

    else:
        print(f"{name} is not in this dictionary.")
        bday = input("Enter their birthday: ")
        birthdays[name] = bday
        print("Birthdays database and dictionary updated.")

# while True:
#     print("Enter a name: (blank to quit)")
#     name = input()
#     if name == '':
#         break
# if name in birthdays:
#     print(birthdays[name] + ' is the birthday of ' + name)
# else:
#     print('I do not have birthday information for ' + name)
#     print('What is their birthday?')
#     bday = input()
#     birthdays[name] = bday
#     print('Birthday database updated.')
