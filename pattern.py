#creating patterns in python is fun, but difficult with just 1 for loop.
#remember to always use another variable when working backwards.
#creating 2 seperate printed loops, 1 going forwards and 1 going backwards,
#will give you an equal pattern, range changes for where you want loop to start.

pattern = 1
star_pattern = "*"
for pattern in range(0,5):
    print(star_pattern)
    star_pattern = star_pattern + "*"
        
star_pattern = "*****"
for pattern in range(1,5):
    backwards_pattern = 5 - pattern        
    print(star_pattern[0:backwards_pattern])
        











    