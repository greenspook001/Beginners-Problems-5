#The first problem I did
mumsList = {7 , 6, 23, 8, 18, 8, 7.2, 85, 915, 12}
print(f"Biggest number = {max(mumsList)}")
print(f"The avverage is = {sum(mumsList) // len(mumsList)}")
print(f"Smallist number = {min(mumsList)}")

#The second problem I did
stringslist = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

count = 0

for string in stringslist:
    if string[0].lower() == string[-1].lower():
        count += 1

print("Number of strings with the same character at start and end:", count)

#The third problem I did
pesto = []
otherfoods = []

for person in range(8):
    favourite_food = input("what's your favourite food? ")
    if favourite_food == 'pesto':
        pesto.append(favourite_food)
    else:
        otherfoods.append(favourite_food)

print(f"Number of 'pesto' mentioned in pesto: {len(pesto)}")
for _ in range(len(pesto)):
    print("I like petso")

print("List of other foods: ", otherfoods)

#The fourth problem I did
cereal_list = []

while True:
    cereal = input("What cereal do you like? ")
    if cereal.lower() == "weetbix" or cereal.lower() == "sultana and bran":
        break
    cereal_list.append(cereal)

for cereal in cereal_list:
    print(cereal)
