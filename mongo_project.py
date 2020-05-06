import pymongo
import os
import env

# MONGODB_URI = os.getenv("MONGO_URI")
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("Error accessing the database")
    if not doc:
        print("")
        print("Error! No results found.")
    return doc

def show_menu():
    print("")
    print('1. Add a record')
    print('2. Find a record by name')
    print('3. Edit a record')
    print('4. Delete a record')
    print('5. Exit')
    print('')
    
    option=input('Please select an option: ')
    return option

def add_record():
    print('')
    first = input('Enter first name > ')
    last = input('Enter last name > ')
    dob = input('Enter date of birth > ')
    gender = input('Enter gender > ')
    hair = input('Enter hair color > ')
    occupation = input('Enter occupation > ')
    nationality= input('Enter nationality > ')

    new_doc = { 'first': first.lower(), 'last': last.lower(), 'dob': dob, 'hair_color': hair, 'occupation': occupation, 'nationality': nationality }
    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")

def find_record():
    doc = get_record()
    if doc:
        print('')
        for k,v in doc.items():
            if k != '_id':
                print(k.capitalize()+": "+v.capitalize())

def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                if update_doc[k] == "":
                    update_doc[k] = v
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")

def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != '_id':
                print(k.capitalize()+": "+v.capitalize())
        print("")
        confirmation = input("Is this the document you want to delete? \nY or N? > ")
        print("")
        if confirmation == 'y':
            try:
                coll.delete_one(doc)
                print("Document was removed!")
            except:
                print("Error accesing database")
        else:
            print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            find_record()
        elif option == '3':
            edit_record()
        elif option == '4':
            delete_record()
        elif option == '5':
            conn.close()
            break
        else:
            print('Invalid input, please try again.')
        print('')

conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
