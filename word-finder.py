import json

filename = input("Please enter file name: ")

with open(f"Lab06{filename}.json", "r") as file:
	data_text = file.read()
	data_json = json.loads(data_text)
	data = data_json["array"]

i_first = 0
i_last = len(data) -1
found = False
word = input("What are you looking for? ")
count = 0

while i_first <= i_last and found == False:
	count += 1
	i_middle = (i_first + i_last) // 2
	if data[i_middle] < word:
		i_first = i_middle + 1
	elif data[i_middle] > word:
		i_last = i_middle -1
	else: 
		found = True

if found == True:
	print(f"{word} was found in the given file.")
else:
	print(f"{word} was not found.")
print(f"Number of loops: {count}")
