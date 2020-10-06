# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:         Nathaniel Michaud, Luca Maddaleni, Landon Matak, Anthony Matl
# Group:        8
# Section:      273
# Assignment:   Lab 7
# Date:         7 October 2020

# Introduction
print('\nEnter the prompted information for the golfing tournament cuts.')
print('Input a negative value for the Round 1 score to end the program.')

# Values and storages are created for information input.
n = 1
score = 1
scores = []
results = {}

# Takes in players with their scores and stores them.
while score >= 0:
    indv_score1 = int(input('\nEnter player {}\'s Round 1 score: '.format(n)))
    if indv_score1 >= 0:
        indv_score2 = int(input('Enter player {}\'s Round 2 score: '.format(n)))
        tot_score = indv_score1 + indv_score2
        scores.append(tot_score)
        player = str(input('Enter player {}\'s name: '.format(n)))
        results[player] = tot_score
        n += 1
    else:
        break

# The scores are sorted, and the median is found depending on if there's an even or odd amount of scores.
scores.sort()
if len(scores)%2 > 0:
    middle = int(len(scores)/2 +0.5)
    median = int(scores[middle-1])
else:
    middle = int(len(scores)/2)
    median = int((scores[middle] + scores[middle-1])/2)

# Result lists are created.
made = []
cut = []

# The players are sorted into who made and who didn't make the cut lists.
for player in results:
    if results.get(player) <= median:
        made.append(player)
    else:
        cut.append(player)

# The two lists are printed off as the results.
print('\n----------------------RESULTS----------------------')
print('\nPlayers who made the cut:')
for player in made:
    print(player)
print('(The above will move onto the next round.)')
print('\n---------------------------------------------------')
print('\nPlayers who did not make the cut:')
for player in cut:
    print(player)
print('(The above will not be moving onto the next round.)')
