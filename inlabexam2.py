'''
elena corpus
csci 160
tuesday 5 -7 pm
storing golf scores
'''

fileName = open('golfscores.txt','w')

scoreOfHole = input('enter the score of the hole between 1 - 10: ')
for holes in range(1,9):
    num = int(scoreOfHole)
    if num >= 1 and num <= 10:
        fileName.write(scoreOfHole + '\n')

    scoreOfHole = input('enter the score of the hole between 1 - 10: ')

fileName.close()


