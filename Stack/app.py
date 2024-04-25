# files = open("requirements.txt")

# with open("requirements.txt", "r", encoding="utf-8") as file:
#     print(file.read())
#     file.close()


#creates a new file and add the folowing data
# new_guests = ["Sam", "Danielle", "Jacob"]

# with open("guests.txt", "w") as guests:
#     for i in new_guests:
#         guests.write(i + "\n")

# guests.close()

# checked_out=["Andrea", "Manuel", "Khalid"]
# temp_list=[]

# with open("guests.txt", "r") as guests:
#     for g in guests:
#         temp_list.append(g.strip())

# with open("guests.txt", "w") as guests:
#     for name in temp_list:
#         if name not in checked_out:
#             guests.write(name + "\n")

# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)



# import os
# print(os.getcwd())