import json

wantedIndex = input("What is the largest number in Francois do you want your Json file to be written to? ")

index2 = 1
index1 = 2
currentIndex = 2

Francois = [2, 1]
while int(currentIndex) <= int(wantedIndex):
    newValue = index1 + index2
    Francois.append(newValue)
    index1 = index2
    index2 = newValue
    currentIndex += 1

json_data = json.dumps(Francois)
with open(f"FrancoisJson/{wantedIndex}francois.json", "w") as outfile:
	outfile.write(json_data)

print(f"Francois counting to {wantedIndex}: /n{Francois}")