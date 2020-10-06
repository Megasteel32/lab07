# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Group 8: Anthony Matl, Landon Matak, Luca Maddaleni, Nathaniel Michaud
# Group:       8
# Section:     273
# Assignment:  Lab 7 Activity 6
# Date:        7 October 2020

valv = float(input('Enter Number of Widgets: '))
values = []
#getting widget inputs for each day
while valv >= 0:
    values.append(valv)
    valv = float(input('Enter number of Widgets: '))

#print(values)
num_inc = 0
num_dec = 0
next_value = values[0]
length = len(values)
interval = 1
day_variable = 1
day_num = 1
count = 0
for h in range(length - 1):
    for i in values:
        if interval < length:
            next_value = values[interval]
            #print('i', i)
            #print('next', next_value)
            if i < next_value:
                num_inc += 1
            elif i > next_value:
                num_dec += 1
            #print('interval', interval)
            interval += 1
            count+= 1
    day_variable += 1
    interval = day_variable
    #print(num_inc, 'numinc')
    #print('numdec', num_dec)
    #print('count', count)
    per_inc = num_inc / count * 100
    per_dec = num_dec / count * 100
    count = 0
    num_inc = 0
    num_dec = 0
    print('For {}-day intervals {:.1f}% were increasing and {:.1f}% were decreasing'.format(day_num, per_inc, per_dec))
    day_num += 1
if length == 1:
    print('Sorry no intervals can be made from one value :(')




