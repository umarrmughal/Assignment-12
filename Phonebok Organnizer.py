phonebook = {
    "ali":9233445,
    "umar":9234343,
    "usama":9235455,
    "tayyab":9243944,
    "abdullah":9212311,
    "huzaifa":9223434}

def add_contacts():
    x = phonebook
    key = input("contact Name:")
    value = int(input("contact Number:"))
    phonebook[key] = value
    return x

def search_contacts():
    search = input("search contact:")
    search_contact = phonebook[search]
    if search in phonebook:
        return search_contact
    else:
        return "Not Found"

def update_contact():
    key = input("Enter contact Name:")
    value = input("enter contact Number:")
    updated_contact = {key:value}
    update = phonebook.update(updated_contact)
    return update,phonebook


user = input("(add ,update or search):").lower()

if user == "add":
    print( add_contacts() )
elif user == "search":
    print(search_contacts())
elif user == "update":
    print(update_contact())
    