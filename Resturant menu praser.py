import pyttsx3
resturant_menu = {
    "appitizers":{
    "Garlic bread": {"description":"Freshly baked bread with garlic butter","price":5.00},
    "Chicken Wings": {"description": "Choice of Buffalo, BBQ, or Teriyaki sauce", "price": 9.00}
    },

    "salad":{
        "greek salad":{"description":"Chopped tomatoes, cucumbers, olives, feta cheese, and red onion with vinaigrette dressing","price":10.00},
        "grilled chicken salad":{"description":"Grilled chicken breast on a bed of mixed greens with tomatoes, cucumbers, and carrots","price":14.00},    
    },
    "entrees":{
        "Chicken alfredo":{"description":"Fettuccine pasta with creamy Alfredo sauce and grilled chicken","price":17.00},
        "Vegetarian Burger": {"description": "Black bean and quinoa burger on a whole wheat bun with lettuce, tomato, and onion", "price": 14.00}
    },
    "drinks":{
        "soft drink":{"description":"coke,pepsi,sprite etc","price":2.00},
        "Coffee":{"description":"latte,regular,cappucino etc","price":3.00}
    },
    "desert":{
        "Chocolate Cake": {"description": "Rich chocolate cake with chocolate ganache", "price": 7.00},
        "Cheesecake": {"description": "New York-style cheesecake with whipped cream and berries", "price": 8.00}
    }
}
print(resturant_menu)

def customize_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.setProperty('volume',0.4)
    
    return engine

engine = customize_engine()
engine.say(resturant_menu)
engine.runAndWait()

def search_category():
    key = input("Enter Category:")
    x = resturant_menu[key]
    key1 = input("Enter item name:")
    y = resturant_menu[key][key1]    
    return x,y

print(search_category())
