import sqlite3
from sqlite3.dbapi2 import connect
from rout import Rout

connection = sqlite3.connect('routs.db')

c = connection.cursor()

# c.execute("""CREATE TABLE routs (
#             name text,
#             grade text,
#             setter text,
#             complete int,
#             attempts int,
#             notes text
#             )""")

def insertRout(rout):
    with connection:
        c.execute("INSERT INTO routs VALUES (:name, :grade, :setter, :complete, :attempts, :notes)",
        {'name': rout.name, 'grade': rout.grade, 'setter': rout.setter, 'complete': rout.complete, 'attempts': rout.attempts, 'notes': rout.notes})

def getAllRouts():
    c.execute("SELECT * FROM routs")
    return c.fetchall()

def getOneRout(name):
    c.execute("SELECT * FROM routs WHERE name = :name", {'name': name})
    return c.fetchone()

def updateName(name, newName):
    with connection:
        c.execute("UPDATE routs SET :valueToUpdate = :newName WHERE name = :name",
                    {'name': name, 'newName': newName})

def updateGrade(name, grade):
    with connection:
        c.execute("UPDATE routs SET grade = :grade WHERE name = :name",
                    {'name': name, 'grade': grade})

def updateSetter(name, setter):
    with connection:
        c.execute("UPDATE routs SET setter = :setter WHERE name = :name",
                    {'name': name, 'setter': setter})

def updateComplete(name, complete):
    with connection:
        c.execute("UPDATE routs SET complete = :complete WHERE name = :name",
                    {'name': name, 'complete': complete})

def updateAttempts(name, attempts):
    with connection:
        c.execute("UPDATE routs SET attempts = :attempts WHERE name = :name",
                    {'attempts': attempts, 'name': name})

def updateNotes(name, notes):
    with connection:
        c.execute("UPDATE routs SET notes = :notes WHERE name = :name",
                    {'name': name, 'notes': notes})

def removeRout(name):
    with connection:
        c.execute("DELETE FROM routs WHERE name = :name",
                    {'name': name})

def displayOneRout(name):
    print('')
    rout = getOneRout(name)
    print('Name: ' + rout[0])
    print('Grade: ' + rout[1])
    print('Setter: ' + rout[2])
    if (rout[3] == 0):
        print('Complete: No')
    else:
        print('Complete: Yes')
        if (rout[4] == 1):
            print('Attempts: Flashed')
        else:
            print('Attempts: ' + str(rout[4]))
    print('Notes: ' + rout[5])

def displayAllRouts():
    routs = getAllRouts()
    for rout in routs:
        displayOneRout(rout[0])
        print('')

def getRoutFromUser():
        print('Enter rout Name: ')
        name = input()
        print('Enter rout Grade: ')
        grade = input()
        print('Enter rout Setter: ')
        setter = input()
        print('Have you finished the rout? 1 = yes 0 = no : ')
        complete = input()
        if complete == '1':
            print('How many attempts?: ')
            attempts = input()
        else:
            attempts = 0
        print('Enter any rout notes')
        notes = input()
        newRout = Rout(name, grade, setter, complete, attempts, notes)
        return newRout

running = 1

while running == 1:
    print('')
    print('Select Action')
    print('1: Show all Routs')
    print('2: Show 1 Rout')
    print('3: Add new Rout')
    print('4: Edit Rout')
    print('5: Delete Rout')

    selection = input()
    if selection == '1':
        print('')
        displayAllRouts()
    
    elif selection == '2':
        print('')
        print('Enter Rout Name: ')
        displayOneRout(input())

    elif selection == '3':
        print('')
        insertRout(getRoutFromUser())
        print('')
        print('Rout Added')

    elif selection == '4':
        print('')
        print('Enter Rout Name:')
        name = input()
        print('')
        print('What to Edit?: ')
        print('1: Name')
        print('2: Grade')
        print('3: Setter')
        print('4: Complete Status')
        print('5: Attempts')
        print('6: Notes')        
        dataToEdit = input()

        if dataToEdit == '1':
            print('')
            print('New name: ')
            updateName('name', name, input())
            print('')
            print('Name Updated')

        elif dataToEdit == '2':
            print('')
            print('New grade: ')
            updateGrade(name, input())
            print('')
            print('Grade Updated')

        elif dataToEdit == '3':
            print('')
            print('New Setter: ')
            updateSetter(name, input())
            print('')
            print('Setter Updated')

        elif dataToEdit == '4':
            print('')
            print('Have you finished the rout? 1 = yes 0 = no : ')
            updateComplete(name, input())
            print('')
            print('Complete Status updated')

        elif dataToEdit == '5':
            print('')
            print('New number of attempts: ')
            updateAttempts(name, input())
            print('')
            print('Attempts Updated')

        elif dataToEdit == '6':
            print('')
            print('New Notes: ')
            updateNotes(name, input())
            print('')
            print('Notes Updated')        

    elif selection == '5':
        print('')
        print('Name of Rout to delete: ')
        routToDelete = input()
        removeRout(routToDelete)
        print('')
        print(routToDelete + ' has been deleted')

connection.close()