
def addContactInfo (contacts, name, mobile = '', home = '', work = '', email = ''):
    contacts[name] = {}
    contacts[name]['mobile'] = mobile
    contacts[name]['home'] = home
    contacts[name]['work'] = work
    contacts[name]['email'] = email
    
contacts = {}
addContactInfo(contacts, 'Tom', '741-1232', '746-1234', '777-3337', 'thomas.stokke@und.edu')
addContactInfo(contacts, 'lucas', '123-4567' , '' , '' , 'lucas.something@und.edu')
addContactInfo(contacts, 'haleh' , email = 'haleh@und.edu', mobile = ' 215-6789')

print(contacts)
