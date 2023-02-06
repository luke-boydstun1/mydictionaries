"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 80%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json

infile = open("mydictionaries/school_data.json", "r")
schools = json.load(infile)
conferences = [372, 108, 107, 130]

# How many schools are in this list?
print(len(schools))
print()
for school in schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conferences:
        if school["Graduation rate  women (DRVGR2020)"] > 80:
            print("Univeristy Name: ", school["instnm"])
            print("Graduation Rate for Women: ",
                  school["Graduation rate  women (DRVGR2020)"], '\n')

for school in schools:
    if school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] != None:
        if school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
            print("Univeristy Name: ", school["instnm"])
            print("In-state off-campus cost: $" +
                  str(school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])+'\n')
