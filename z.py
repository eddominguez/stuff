#! python3

import sys
import pyperclip

#stores zoom room numbers
#each class is represented by their number

#change the datasets for your own use
#datasets as follows
zoomRoom = {'class number' : 'zoom room' }

#zoom passwords are stored here.     
zoomPasswords = {''class number': 'zoom passwprd }

#if the user only executes the script and does not give a class number
#along with it, the program terminates

if len(sys.argv) < 2:
    print('follow this guideline to use the script: ')
    print('z.py [classNum]')
    sys.exit()
    
#looks for the class number entered by the user
classNum = sys.argv[1]

if classNum in zoomRoom:
    pyperclip.copy(zoomRoom[classNum])
    print('zoom room for '+ classNum + ' copied to clipboard.')
    yesToCopy  = input('Do you need the password? Enter y to copy it: ')
    
    if yesToCopy == 'y'  and classNum in zoomPasswords:
        pyperclip.copy(zoomPasswords[classNum])
        print('password has been copied')
    elif yesToCopy == 'n':
        print('no password has been copied')
else:
    print('there is no acc named ' + classNum)
    
