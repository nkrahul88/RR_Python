gpa = input('What is your Grade Point Average: ')
avg_per = input('Enter your average percentile: ')
gpa = float(gpa)
avg_per = float(avg_per)

if gpa >= .85 and avg_per >= .70:
    distiction = True
else:
    distiction = False

if distiction:
    print('Your are a Distinction student')
else:
    print('Sorry better luck next time !')
