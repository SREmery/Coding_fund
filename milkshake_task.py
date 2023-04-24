budget = int(input("What is your budget?:  "))

shakes = {"chocolate": 1, "strawberry": 2, "banana": 3, "mixed": 4} 

while True:
    print("shake options: ")
    for option, price in shakes.items():
        print(f"{option}. £{price}")
       
    choice = (input("Please choose between 1 - 4 (enter Q to quit):  "))

    if choice.upper() == "Q":
        print("Barman: I wish you well in your search for love!")
        break
    
    if choice not in shakes:
       print("invalid")
       continue
    

    price = shakes[choice]
    if price > budget:
      print("kicked out")
      break
    

    print("Enjoy!")
    budget -= price
    print(f"remaining budget: £", {budget})


