# 1. Name:
#      Jacob Briggs
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This is a basic authentication program that reads data from a json file.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was making the video short. After a few tries I started copy and pasting the information which was way better.
# 5. How long did it take for you to complete the assignment?  
#     about an hour and a half maybe two hours. 

import json

json_string = json.dumps('Lab02.js')

with open('Lab02.json', 'r') as file:
    json_string = file.read()

json_dictionary = json.loads(json_string)
username_list = json_dictionary["username"]
password_list = json_dictionary["password"]

i = 0
end_loop = False

input_user = input('Username: ')
input_password = input('Password: ')

while end_loop == False:
    if username_list[i] == input_user:
        end_loop = True
    else:
        if i >= 11:
            end_loop = True
        i += 1

if username_list[i] == input_user and password_list[i] == input_password:
    print('You are authenticated!')
else:
    print('You are not authorized to use the system.')