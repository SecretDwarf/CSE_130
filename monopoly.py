PA_hotel_loop = True
while PA_hotel_loop == True:
    color_group = input('Are all the properties in the green group owned? ')
    if color_group == 'n' or color_group == 'no':
        print('you cannot build a hotel without owning all of the properties. ')
        PA_hotel_loop = False
        break
    
    money = int(input("How much monopoly money do you have? "))
    if money < 200:
        print('you cannot build with less than $200')
        PA_hotel_loop = False
        break        

    pennsylvania = int(input("What is on Pennsylvania Avenue?\n0)nothing 1)one house 2)two houses 3)three houses 4)four houses 5)a hotel "))

    if pennsylvania == 5:
        print('you cannot build an additional hotel')
    
    north_carolina = int(input("What is on North Carolina Avenue?\n0)nothing 1)one house 2)two houses 3)three houses 4)four houses 5)a hotel "))

    if north_carolina == 5 and pennsylvania == 4:
        print("Swap North Carolina's hotel with Pennsylvania's four houses.")
        PA_hotel_loop = True
        break

    pacific = int(input("What is on Pacific Avenue?\n0)nothing 1)one house 2)two houses 3)three houses 4)four houses 5)a hotel "))

    if pacific == 5 and pennsylvania == 4:
        print("Swap Pacific's hotel with Pennsylvania's four houses")
        PA_hotel_loop = True
        break
    
    nc_build = max(4 -north_carolina, 0)
    pacific_build = max(4 - pacific, 0)
    p_build = max(4 -north_carolina, 0)

    money_needed = (nc_build + pacific_build + p_build) * 200
    if money < money_needed:
        print('you cannot build a hotel')
        PA_hotel_loop = False
        break

    possible_houses = int(input("How many houses are there to purchase? "))
    needed_houses = max(nc_build + pacific_build - p_build, 0)
    if needed_houses <= possible_houses:
        print(f"this will cost ${money_needed}.")
        print(f"{nc_build} houses to North Carolina,")
        print(f"{pacific_build} houses to Pacific,")
        print(f"and put one hotel on Pennsylvania")
        PA_hotel_loop = True
        break

if PA_hotel_loop == True:
    print("You can put your hotel on Pennsylvania Avenue.")
else: 
    print("You were unable to build a hotel this turn")