# ciao
# may the coding begin

import numpy as np

birthdays = {
    "Bhavya": "January 1st, 2006"
            }


while True:

    name = input("At any time, you can press q to quit.\nEnter a name: ")

    if name.lower == "q":
        break

    # Load
    read_dictionary = np.load("main.py", allow_pickle=True).item()
    print(read_dictionary[name])  # displays "bday"

    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")

    else:
        print(f"{name} is not in this dictionary.")
        bday = input("Enter their birthday: ")
        birthdays[name] = bday
        print("Birthdays database and dictionary updated.")
        # save dict:
        np.save("main.py", birthdays)

# import numpy as np
#
# # Save
# dictionary = {'hello':'world'}
# np.save('my_file.npy', dictionary)
#
# # Load
# read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item()
# print(read_dictionary['hello']) # displays "world"
