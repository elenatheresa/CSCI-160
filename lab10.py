'''
elena corpus
csci160
tuesday 5 - 7
writing program that will clean up the data in this text file
'''

fileName = open('numbers.txt','r')

outputFile = open('number2.txt','w')

read_counter = 0
write_counter = 0

if fileName != '':
    for lines in fileName:
        #lines = fileName.read()
        read_counter = read_counter + 1
        num = int(lines)
        if num < 100 and num > 0:
            outputFile.writelines(str(lines))
            write_counter = write_counter + 1

    fileName.close()
    outputFile.close()
    
    print("Number of values read from the input file: ", read_counter)
    print("Number of values written to the output file: ", write_counter)
    
else:
    print("file does not exist")



