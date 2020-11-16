def printPhoneBook (message, data):
    print(message)
    for contact in data:
        print(format(contact,"15s"), format(data[contact],">15s"))
    print()

def printSortedPhoneBook(message, data):
    print(message)
    sortedNames = list(data.keys())
    sortedNames.sort()
    for contact in data:
        print(format(contact,'15s'), format(data[contact],'>15s'))
    print()

def addContacts(data):
    contactsToAdd = input('enter new contact: ')
    while contactToAdd != '':
        numberToAdd = input('enter number for ' + contact + ': ')
        #add the contact
        if contactToAdd in data: #contact is already in the phone book
            overwriteEntry = input(contactToAdd + 'already exists in the phone book, overwrite entry? (y/n)')
            if overwriteEntry.strip().lower() == 'y':
                data[contactToAdd] = numberToAdd #adds or updates the entry in the dictionary
            
        else: #new entry into the phone book
            data[contactToAdd] = numberToAdd #adds or updates the entry in the dictionary
            
        contactToAdd = input('\nenter new contact: ')

def searchByNumber(data):
    textToFind = input('enter text to find: ')
    while textToFind != '':
        #go to work finding 'textToFind' in the dictionary
        contacts = list(data.keys())
        foundMatch = False
        for contact in contacts:
            if data[contact].find(textToFind) > -1:
                print(contact)
                foundMatch = True
            #else:
                #print(textToFind, 'is not in the contact list')
        if foundMatch == False: #or if not foundMath
            print(textToFind, 'is not in the contact list')

        textToFind = input('enter next text to find: ')
        
        
phoneBook = {"tom's office" : "7-3337", "CSci Office" : "7-4107", "UND" : "777-4321"}

#print (phoneBook)
printPhoneBook("initial contacts", phoneBook)

printSortedPhoneBook('sorted initial contacts', phoneBook)

addContacts(phoneBook)

printSortedPhoneBook('sorted contacts after add' , phoneBook)

searchByNumber(phonebook)
