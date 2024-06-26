# <!-- Introduction

# Welcome to the Contact Management System project! In this project, you will apply 
# your Python programming skills to create a functional command-line-based application
#  that simplifies the management of your contacts. The Contact Management System 
#  will empower you to add, edit, delete, and search for contacts with ease, all 
#  while reinforcing your understanding of Python dictionaries, file handling, 
#  user interaction, and error handling.


# Project Requirements

# Your task is to develop a Contact Management System with the following features:

#     User Interface (UI):

#         Create a user-friendly command-line interface (CLI) for the Contact Management System.

#         Display a welcoming message and provide a menu with the following options:

#         Welcome to the Contact Management System!

#         Menu:
#         1. Add a new contact
#         2. Edit an existing contact
#         3. Delete a contact
#         4. Search for a contact
#         5. Display all contacts
#         6. Export contacts to a text file
#         7. Import contacts from a text file
#         8. Quit

#     Contact Data Storage:
#         Use nested dictionaries as the main data structure for storing contact information.
#         Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
#         Store contact details within the inner dictionary, including:
#             Name
#             Phone number
#             Email address
#             Additional information (e.g., address, notes).

#     Menu Actions:
#         Implement the following actions in response to menu selections:
#             Adding a new contact with all relevant details.
#             Editing an existing contact's information (name, phone number, email, etc.).
#             Deleting a contact by searching for their unique identifier.
#             Searching for a contact by their unique identifier and displaying their details.
#             Displaying a list of all contacts with their unique identifiers.
#             Exporting contacts to a text file in a structured format.
#             Importing contacts from a text file and adding them to the system.

#     User Interaction:
#         Utilize input() to enable users to select menu options and provide contact details.
#         Implement input validation using regular expressions (regex) to ensure 
#         correct formatting of contact information.

#     Error Handling:
#         Apply error handling using try, except, else, and finally blocks to manage 
#         unexpected issues that may arise during execution.

#     GitHub Repository:
#         Create a GitHub repository for your project.
#         Commit your code to the repository regularly.
#         Create a clean and interactive README.md file in your GitHub repository.
#         Include clear instructions on how to run the application and explanations of its features.
#         Provide examples and screenshots, if possible, to enhance user understanding.
#         Include a link to your GitHub repository in your project documentation.

#     Optional Bonus Points
#         Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.
#         Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.
#         Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.
#         Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.
#         Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.

# Project Submission

#     Upon completion, submit your project, including all source code files and the README.md file in your GitHub repository, to your instructor or designated platform.

# Project Tips

#     Begin by designing a simple, intuitive user interface that aligns with the provided menu options.
#     Test your code iteratively as you implement each feature to identify and address any potential bugs or issues.
#     Collaborate with fellow learners, seek assistance, and remember that learning is a collaborative effort.

# By successfully completing this project, you will not only enhance your Python programming skills but also have a practical Contact Management System to streamline your contact management tasks. Get ready to create a valuable tool for yourself and others!

# Happy coding! 📇🐍 -->


import re
import os
import json

print("\nWelcome to the Contact Management System!")

contacts = {
    "janemansfield@gmail.com": {"name": "Jane Mansfield", "phone": "123-543-6432", "address": "34 Urban Parkway"},
    "bobdingle@hotmail.com": {"name": "Bob Dingle", "phone": "904-123-6516", "address": "99 Street Avenue"},
    "guyFieri@aol.ca": {"name": "Guy Fieri", "phone": "934-654-1253", "address": "100 Diner Street"}
}

def addContact(email):
    global contacts
    print("Ok, lets add a new contact for you!")

    name = input("\nWhat's your contacts name?\n").strip()
    phone= input("\nWhat's your contacts phone number?\n").strip()
    address= input("\nWhat's your contact's address?\n").strip()
    if email not in contacts:
        contacts[email] = {"name": name, "phone": phone, "address": address}
    else:
        print(f"Sorry, you already have a contact listed for the email address {email}")

    print(f"Awesome! Your new contact '{contacts[email]}' has been added!\n")
    dispContacts()


def editContact(name):
    global contacts
    foundContact = False

    for contact, info in contacts.items():
        for entry, value in info.items():
            if value.lower() == name.lower():
                editContact = contact
                foundContact = True
                break
    if foundContact:
        print(f"\nOk, what information would you like to change about {editContact}?")
        changeCategory = input("Please enter: email, name, address, phone - or leave blank to return to menu\n").strip()
        if changeCategory:        
            if changeCategory == "name":
                newName = input("\nWhat would you like to change the name to?\n").strip()
                contacts[editContact]["name"] = newName
                print(f"succesfully change the name of {editContact} to {newName}")
                
            elif changeCategory == "email":
                newEmail = input("\nWhat would you like to change the email to?\n").strip()
                contacts[newEmail] = contacts[editContact]
                print(f"succesfully change the email of {editContact} to {newEmail}")
                del contacts[editContact]
                
            elif changeCategory == "address":
                newAddress = input("\nWhat would you like to change the address to?\n").strip()
                contacts[editContact]["address"] = newAddress
                print(f"succesfully change the address of {editContact} to {newAddress}")

            elif changeCategory == "phone":
                newPhone = input("\nWhat would you like to change the phone number to?\n").strip()
                contacts[editContact]["phone"] = newPhone
                print(f"succesfully change the phone number of {editContact} to {newPhone}")

            else:
                print("Please make sure you make a valid selection from the menu!")
    else:
        print(f"Sorry, I couldn't find a contact named '{name}'")

def delContact(name):
    global contacts
    foundContact = False

    for contact, info in contacts.items():
        for entry, value in info.items():
            if value.lower() == name.lower():
                delContact = contact
                foundContact = True
                break
    if foundContact:
        print(f"removing {contacts[delContact]}")
        del contacts[delContact]
    else:
        print(f"Sorry, I couldn't find a contact named '{name}'")
    
def searchContact(name):
    RetrieveContact = ""

    for contact, info in contacts.items():
        for entry, value in info.items():
            if value.lower() == name.lower():
                RetrieveContact = contact 
                break
    if bool(RetrieveContact) == True:
        print(f"found '{name}':")
        print(f"  - {RetrieveContact}")
        for key, value in contacts[RetrieveContact].items():
            print(f"  - {value}")
    else:
        print(f"Sorry, I couldn't find a contact named '{name}'")

def dispContacts():
    print(f"\nHere are all your contacts:\n")

    for contact, info in contacts.items():
        print(f"{contact}:")
        for name, value in info.items():
            print(f"  - {value}")
            

def exportContact():
    print("Ok! Exporting your contacts to file...\n")
    with open("Files/Output/ContactsExports.txt", "w") as file:
        json.dump(contacts, file, indent=4)
        
        
def importContact():
    global contacts
    print("Ok! Importing contacts from file...\n")
    with open('Files/Input/contactsImport.txt', 'r') as file:
        newContacts = json.load(file)
        contacts.update(newContacts)
    print("\nHere is your updated Contact List:\n")
    dispContacts()



def main():
    while True:

        print("\nPlease make a selection from the following menu:\n1 - Add a new contact\n2 - Edit an existing contact\n3 - Delete a contact\n4 - Search for a contact\n5 - Display all contacts\n6 - Export contacts to a text file\n7 - Import contacts from a text file\n8 - Quit")
        try:
            command = int(input("\nEnter the number of the command you would like to select\n").strip())
        except:
            print("Please ensure you make a valid selection!\n")
        else:
            if command > 0 and command <= 8:
                commandStr = str(command)
               
                if commandStr == "1":
                    #1. Add a contact
                    print("Ok lets add a new contact to your contacts list!")
                    email = input("What's your new contact's email address?").strip()
                    
                    addContact(email)
                    
                if commandStr == "2":
                    #2. Edit an existing contact
                    print("\nOk, lets delete a contact")
                    name = input("Enter the name of the contact you'd like to edit:\n").strip()
                    editContact(name)

                if commandStr == "3":
                    #3. Delete a contact
                    print("\nOk, lets delete a contact")
                    name = input("Enter the name of the contact you'd like to delete:\n").strip()
                    delContact(name)
                    
                if commandStr == "4":
                    #4. Search for a contact
                    print(f"\nOk let's find a contact...")
                    name = input("What's the name of the person you're looking for:")
                    searchContact(name)
                    
                if commandStr == "5":
                    #5. Display all contacts
                    dispContacts()

                if commandStr == "6":
                    #6. Export contacts to a text file
                    exportContact()
                    
                if commandStr == "7":
                    #7. Import contacts from a text file
                    importContact()
                    
                if commandStr == "8":
                    #8. Quit
                    print("\nYou selected 8!")
                    print("Thanks for using the Contact Management Service!")
                    break
            else:
                print("Make sure you enter a number between 1 and 8!")

main()