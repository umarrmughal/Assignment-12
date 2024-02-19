shopping_list = {
    "Fruits": "Apples" ,
    "Vegetables": "potato",
    "Dairy": "Milk" ,
    "Meat": "Chicken",
    "Grains": "Bread",
    "Pantry Staples": "Salt"
}
user = input("check, add, remove: ").lower()
def add():
    key = input("enter category:")
    value = input("enter item:")
    shopping_list[key] = value
    return shopping_list

def remove():
    remove = input("enter category name:")
    del shopping_list[remove]
    return shopping_list

def check():
    shopping_list
    return shopping_list

if user == "check" :
    print(check())
elif user == "add":
    print(add())
elif user == "remove":
    print(remove())
