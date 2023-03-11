
# Jacob Briggs
# Lab 08 Sort

# Description:
# This program will sort a selection of data
#
#  The hardest part:
# The hardest part of this lab was working on it before and while I am at BPA State. 
# Unfortunately with the busy schedule, sharing a room, and traveling I won't be able to record my video of this until Monday the 27th.
# Luckily much of this project follows our past work with the Word Finder.

# How long did this assignment take?
# This assignment probably took a cumalative hour and a half of focused time. I worked on it off an on.

import json

def my_sort(list):
    
    for item in list:
        assert type(item) == type(list[0])
    
    i_pivot = len(list) - 1
    i_check = i_pivot
    counter = 0
    while i_pivot > 0:
        assert i_pivot > 0 and i_pivot < len(list)
        for i in range(i_pivot): 
            counter +=1
            assert i_check >= -1 and i_check <= i_pivot 
            if i_check > -1:
                if list[i_check] > list[i_pivot]:
                    temp = list[i_pivot]
                    list[i_pivot] = list[i_check]
                    list[i_check] = temp
                    i_check = i_pivot
                i_check -= 1
            else:
                i_pivot -= 1
                i_check = i_pivot
    print(counter, len(list))

file_name = input("Please enter the name of the file: ")



with open(f"Lab08.{file_name}.json", 'r') as file:
    data = file.read()
    json_list = json.loads(data)
    list = json_list["array"]
    print("Before Sorted: ")
    print(list)
    my_sort(list)
    print("After Sorted: ")
    print(list)

for i in range(1, len(list)):
    assert list[i-1] <= list[i]