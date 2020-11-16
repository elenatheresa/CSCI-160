theList = []
honorPoints = {}
honorPoints = {'A' : 4,'B' : 2}
print(honorPoints)
honorPoints['C'] = 2
print(honorPoints)
honorPoints['B'] = 3
print('After Fixing B: ', honorPoint)
honorPoints['F'] = 0
print(honorPoints)
honorPoints['D'] = 1
print(honorPoints)

print('honor points for an A' , honorPoints['A'])
grade = input('what grade do you expect for this class? ')
while grade != '':
    if grade in honorPoints:
        print('you will earn', honorPoints[grade] * 4, 'honor points from this class\n\n')
    else:
        print('please enter a valid grade\n\n')

    grade = input('what grade do you expect for another class? ')

for grade in honorPoints:
    
