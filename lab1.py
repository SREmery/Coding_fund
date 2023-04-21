print('Hello World!')

username = 'bob'
age = 32
print(username, 'is', age, 'years old')

weight = float(input("enter weight:"))
unit = input("K (kgs) or L (Lbs):")

if unit.upper() == "k":
    converted = weight / 0.45 
    print("Weight in Lbs: ", converted)
else:
    converted = weight * 0.45
    print("weight in kgs: ", converted) 

counter = 0 

while counter < 5: 
    name = input("please enter a name: ")
    print(name + "is great!")
    counter += 1