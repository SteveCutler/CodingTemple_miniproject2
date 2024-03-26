

repo url: https://github.com/SteveCutler/CodingTemple_miniproject2

Welcome to my contact management Python app:

When you open the program, you will be prompted to pick a menu option:

    #         1. Add a new contact
    #         2. Edit an existing contact
    #         3. Delete a contact
    #         4. Search for a contact
    #         5. Display all contacts
    #         6. Export contacts to a text file
    #         7. Import contacts from a text file
    #         8. Quit

For ease of use the app has been pre-programmed with a number of contacts already, as well as set up to load and import contacts to various files which already exist.

These functions are pretty self explanatory but lets go into a bit of detail for each menu options.

    1. Add a new contact
When you select 'add a contact' you're prompted for the email of the new contact (each contact is listed under its email address).
Then you're prompted for the name, phone number and address. Once entered succesfully your contact is added to your contacts list!

    2. Edit an existing contact
'Edit contact' prompts you for the name of the contact you'd like to edit. The program searches through the contact list for a matching name.
If it finds a contact matching the name you're then asked which piece of data you'd like to edit for the corresponding contact.

    3. Delete a contact
'Delete contact' similarly prompts you for the name fo the contact. It searches through your contacts and if it finds the corresponding contact
it removes it from your contact list

    4. Search for a contact
'Search contact' asks you for the name of the contact, when it finds the correct contact it displays all the relevant information.
    
    5. Display all contacts
'Display all contacts' displays a list of your contacts along with their personal details.
    
    6. Export contacts to a text file
'Export contacts' dumps your the info from your contact list into a text file in json format - for ease of readability.
    
    7. Import contacts from a text file
'Import contacts' loads data listed in json format from a text file and appends it to the current contents of your contact list.
    
    8. Quit
Quits the program!

