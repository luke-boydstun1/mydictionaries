person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# print(person)

# print the name of the second child

# print(person["children"][1])

# print the name of the cat

# print(person["pets"]["cat"])

# iterate through all children and print each one

for i in person["children"]:
    print(i)

# print the pets in this format:
# type of pet: dog name of pet: fido

for key in person["pets"]:
    name = person["pets"][key]
    print("type of pet: {key} | name of pet:{name} ")
