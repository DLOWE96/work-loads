#Write a program that constantly asks user to enter a number! Until number is -1

input_sum = 0
input_collection = 0

while True:
    number = int(input("Please enter a positive or negative number or -1 to finish: "))
    if number == -1:
        break

    input_sum += number
    input_collection += 1

print(f"The sum of entered numbers: {input_sum} and the total numbers collected: {input_collection} ")

# Calculate the average of all valid numbers other than -1 and 0
# I need some assistance in understanding how the mean() function works
# I feel using the mean function in this case would make the code look nicer

sum_average = input_sum/input_collection

print(sum_average)

# The Task 4 walkthrough helped me a great deal with this task.
# It also helped me to format my print outs in a much better looking way (ln15)
