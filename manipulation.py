str_manip = (input("Please enter a sentence" + " "))   

print(len(str_manip))

#remember to create new strings with casted variables.

str_last = str_manip[-1]

str_manip_2 = str_manip.replace(str_last,"@")

print(str_manip_2[:-4:-1])

print(str_manip_2[0:3:1] + str_manip_2[-2:])





