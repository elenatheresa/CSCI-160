import FileUtils

def printSongs(title, songList):
    print(title)
    for song in songList:
        print(' ', song)
    print()

def addSongs(songList):
    #print('songList id ', id(songList))
    newTitle = input('enter title for new song: ')
    while newTitle != '':
        newArtist = input('enter artist for new song: ')
        songList.append(newArtist + ' - ' + newTitle)

        newTitle = input('enter title for the new song: ')

    songList.sort()

def saveSongs(songList,fileName):
    outfile = open(fileName,'w')
    for song in songList:
        outfile.write(song + '\n')
    outFile.close()

def readSongs(songList, fileName):
    inFile = open(fileName, 'r')
    songList.clear() #make sure that the list we are given is empty
    for song in inFile:
        song = song.strip() #remove the line feed at the end of the input
        songList.append(song)

    songList.sort()
    inFile.close()

def readSongs2(songList):
    songList = []
    inFile = open(fileName, 'r')
    #songList.clear() #make sure that the list we are given is empty
    for song in inFile:
        song = song.strip() #remove the line feed at the end of the input
        songList.append(song)

    songList.sort()
    inFile.close()
    return songList #we created here so i need to return it to where the function was called

def searchForSongs(songList):
    songTofile = input('enter title for song to find: ')
    while newTitle != '': #or while not(newTitle == '':
        #look for the song
        if songToFind in songs: #performs a linear search on the list
            print('found',songToFind, 'in the list')
        else:
            print('unable to find',songToFind, 'in the list')
            
        songToFind = input('enter title for song to find: ')

def searchForSongs2(songList):
    songTofile = input('enter title for song to find: ')
    while newTitle != '': #or while not(newTitle == '':
        #look for the song
        soungFound = False 
        for song in songList: #give me each song, one at a time
            if song.lower() == songToFind.lower(): #does the current song match the search test?
                print('found',songToFind,'in the list\n')
                soundFound = True
                break
            
        if not songFound:
                print('unable to find',songToFind,'in the list\n')

        songToFind = input('enter title for song to find: ')
    
def searchForPartialMatches(songList):
    textToFind = input('enter text for song to find: ')
    while textToFind != '': #or while not(newTitle == '':
        #look for the song
        for song in songList:
            if songfind(textToFind) > -1:
                print('   found',song)
                numOfMatches = numOfMatches + 1


        if numOfMatches == 0:
            print('unable to find any songs containing', textToFind)
        else:
            print('Found', numOfMatches,'of matches for', textToFind)

        textToFind = input('enter title for song to find: ')
    
#create a list for MP3 collection
fileName = FileUtils.selectOpenFile("Select data file", "Opening data file")
#songs = []
#readSongs(songs, fileName)
#or
songs = readSongs2(fileName)
          
'''          
#read the songs from a file and place into the list 
songs.append('Styx - Mr Roboto')
songs.append('Bon Jovi - Living on a Prayer')
songs.append('Neil Diamomd - Sweet Caroline')
songs.append("Journey - Don't Stop Believing")
'''
          
printSongs('Initial list', songs)
#print('songs id',id(songs))
addSongs(songs)

printSongs('after adding songs', songs)

searchForSong2(songs)

#save the songs from a list and place into a file
#fileName = FileUtils.selectSaveFile("select data file", "saving data file")
saveSongs(songs)


