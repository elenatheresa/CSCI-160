import FileUtils

def saveSongs(songList, fileName):
    outfile = open(filename, 'w')
    for song in songList:
        outfile.write(song + '\n')
        #or
        #outfile.write(songs)
        #outFile.write('\n')
    outfile.close()

def printSongs(title, songList):
    print(title)
    for song in songList:
        print(' ', songList)
    print()

def addSongs(songList):
    #print('songList id ', id(songList))
    newTitle = input('enter title for new song: ')
    while newTitle != '':
        newArtist = input('enter artist for new song: ')
        songList.append(newArtist + ' - ' + newTitle)

        newTitle = input('enter title for the new song: ')
        

#create a list for MP3 collection
songs = []

#read the songs from a file and place into the list 
songs.append('Styx - Mr Roboto')
songs.append('Bon Jovi - Living on a Prayer')
songs.append('Neil Diamomd - Sweet Caroline')
songs.append("Journey - Don't Stop Believing")

printSongs('Initial list', songs)
#print('songs id',id(songs))
addSongs(songs)

printSongs('after adding songs', songs)

#save the songs from a list and place into a file
fileName = FileUtils.selectSaveFile("select data file", "saving data file")
saveSongs(songs)

