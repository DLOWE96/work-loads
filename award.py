#Recieve scores from user

swimming_time =int(input("How long did the swimming event take?"))
cycling_time = int(input("How long did the cycling event take?"))
running_time = int(input("How long did the running event take?"))

triathlon_time = (swimming_time + cycling_time + running_time)

print(triathlon_time)

#create calculation to find overall score using if-else-elif statement

if 0<=triathlon_time<=100 :
    print("Congratulations on winning the Honorary Colours Award")

elif 101<=triathlon_time<=105 :
    print("Congratulations on winning the Honorary Half Colours Award")

elif 106<=triathlon_time<=110 :
    print("Congratulations on winning the Honorary Scroll Award")
    
else :
    print("Sorry, you recieve no award, better luck next time")