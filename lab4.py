# Part 1

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,
        11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,
        35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

for age in ages:
    print(age)

for age in ages:
    age += 1
    len(ages)
    print(age)

for age in ages:
    if age < 16 or age > 65:
        ages.remove(age)
        print(age)
    
count = 0
for age in ages:
    if age >= 16 and age <= 25:
        count += 1
        print("Number of 16-25 year olds is:", count)

# part 2


while True:
    print("Time Calculator")
    print("1. Add 2 date-times")
    print("2. Find the difference between 2 date-times")
    print("3. Convert to Hours")
    print("4. Convert tp Minutes")
    print("5. Convert Minutes to -date-time")
    print("6. Convert Hours to date-time")
    print("7. Exit")

    choice = int(input("Enter an option:  "))
   

    if choice == "1":
        while True:
            date_time1 = input("Enter time 1 (in format DD:HH:MM):  ")
            t1 = date_time1.split(":")
            if len(t1) == 3:
               break

# Was not able to complete unfortunately! :(


