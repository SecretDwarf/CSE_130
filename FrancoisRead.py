#1. Name:
#     Jacob Briggs
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program is ment to convert decimal numbers into Francois counting.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was checking my work. At first my code wrote to a JSON file and it was alot easier to check it because I didn't have to write every number into a trace table I could just add them and countinue.
# 5. How long did it take for you to complete the assignment?
#      I worked on this assignment off and on for a cumalative hour and a half.

def Francois(wantedIndex):
    index2 = 1
    index1 = 2
    currentIndex = 2
    Francois = [2, 1]
    count = 1

    if wantedIndex < 0 and (wantedIndex - 1) != -1: 
        print("Francois counting starts at 1. Please try again")
    else:
        while int(currentIndex) <= int(wantedIndex):
            newValue = index1 + index2
            Francois.append(newValue)
            index1 = index2
            index2 = newValue
            currentIndex += 1
            count += 1
            assert count > 0 and index2 > index1
    
    print(f'This program took {count} iterations.')
    return Francois[wantedIndex]


wantedIndex = int(input("What number in Francois do you want to see? "))
assert type(wantedIndex) == int

while wantedIndex < 0:
    wantedIndex = int(input("Please enter a positive number to see in Francois:  "))
if wantedIndex == 0:
    output = 0
else:
    output = Francois(wantedIndex - 1)
print(f" The decimal number {wantedIndex} is {output} in Francois counting.")