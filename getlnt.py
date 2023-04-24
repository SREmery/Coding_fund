min = 1
max = 100
attempts = 0

while attempts <3:
    value = int(input(f"enter an integer between {min} and {max}: "))
    if min <= value <= max:
        print(f"correct value: {value}") 
        break
    else:
        print("try again")
    
    attempts += 1
if attempts == 3:
    print("None")