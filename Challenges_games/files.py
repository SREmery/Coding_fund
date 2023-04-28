# Exercie - open a new text file called teams.txt, and add the names of 5 sports teams.
# read and display the names of the 1st and 4th team in the file. .strip()
# edit the files so that the top lin e is replaced with "this is a new line"
# print out the edited file, line by line.



file = open("teams.txt", "w")
teams = ["tennis", "ball", "racket", "sing", "footy"]
for i in teams:
    newline = i + "\n"
    file.write(newline)
file.close()

file = open("teams.txt", "r")
lines = file.readlines()
print(lines[0].strip())
print(lines[3].strip())
file.close()

file = open("teams.txt", "r")
lines = file.readlines()
file.close()
lines[0] = "This is a new line"

file = open("teams.txt", "w")

for i in range(len(lines)):
    if i == len(lines)-1:
        file.write(lines[i])
    else: 
        file.write(lines[i].strip() + "\n")

file.close()

file = open("teams.txt", "r")
for line in file:
    print(line.strip())

file.close()

# with statement - closes automatically 

with open("filename.txt", "w") as file:
    for n in range(1, 11):
        newline = "this is a new line" + "" + str(n) + "\n"
        file.write(newline)

