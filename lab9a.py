'''
elena corpus
CSCI 160
tuesday 5 - 7 pm
program to create a text file that contains a sequence of test scores
'''
'''
fileName = open('testscores.txt','w')
fileName2 = open('testscores2.txt','w')
fileName3 = open('testscores3.txt','w')

print('Enter the scores, press enter to quit: ')
scores = input('scores: ')
fileName = open('testscores.txt','w')
scores.split(' ')
fileName.write(scores)

newFile = input("create a new file? ")
while newFile != 'no':
    if newFile == 'yes':
        scores = input('scores: ')
        scores.split()
        fileName2.write(scores)
    elif newFile == 'Yes':
        scores = input('scores: ')
        scores.split(' ')
        fileName3.write(scores)
    else:
        fileName.close()
        fileName2.close()
        fileName3.close() 
    newFile = input("create a new file? ")



fileName.close()
fileName2.close()
fileName3.close()
'''

fileName = open('testscores.txt','w')
fileName.write(str(1) + '\n')
fileName.write(str(23) + '\n')
fileName.write(str(34) + '\n')
fileName.write(str(47) + '\n')
fileName.write(str(95) + '\n')
fileName.write(str(96) + '\n')
fileName.write(str(78) + '\n')
fileName.write(str(81) + '\n')
fileName.write(str(92) + '\n')
fileName.write(str(63) + '\n')
fileName.write(str(74) + '\n')
fileName.write(str(95) + '\n')
fileName.write(str(100) + '\n')
fileName.close()








