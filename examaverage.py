maths = 999
english = 999
ict = 999

while (maths < 0 or maths >100):
    maths = int(input("Enter maths mark between 0-100: "))

while (english < 0 or english >100):
    english = int(input("Enter english mark between 0-100: "))
    
while (ict < 0 or ict >100):
    ict = int(input("Enter ict mark between 0-100: "))

average = (maths + english + ict) / 3

if average >= 65:
    result = "pass"
else:
    result = "fail"

print(f"Average mark: {average}: {result}")