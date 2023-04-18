
# breakfast, lunch , dinner , drinks
# (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan
# All menu items should have weight,
# preparation time in minutes, calories, and price.

from typing import KeysView , Union, Tuple


class Menu:
    MENU_ITEMS = {
        "Breakfast": [{
            "name" :"Sandwich with sausage",
            "price": 2.50,
            "calories": 150,
            "prep_time": 10

        },
        {
            "name": "Bacon",
            "price": 1.50,
            "calories": 150,
            "prep_time": 10
        },
        {
            "name": "Egg sandwich",
            "price": 2.50,
            "calories": 250,
            "prep_time": 10
        }],
        "Lunch": [{
            "name": "Roasted chicken",
            "price": 5.50,
            "calories": 550,
            "prep_time": 10
        },
        {
            "name": "Meatballs",
            "price": 5.50,
            "calories": 550,
            "prep_time": 10
        },
        {
            "name": "Pork roast",
            "price": 5.50,
            "calories": 550,
            "prep_time": 10
        }],
        "Dinner": [{
            "name": "Steak",
            "price": 20.50,
            "calories": 550,
            "prep_time": 10
        },
        {
            "name": "Pasta with salmon",
            "price": 15.50,
            "calories": 550,
            "prep_time": 10
        },
        {
            "name": "Whole chicken",
            "price": 50.00,
            "calories": 550,
            "prep_time": 10
        }],
        "Drinks": [{
            "name": "Coffee",
            "price": 2.50,
            "calories": 150,
            "prep_time": 5
        },
        {
            "name": "Tea",
            "price": 2.00,
            "calories": 150,
            "prep_time": 5
        },
        {
            "name": "Fizzy drink",
            "price": 3.50,
            "calories": 150,
            "prep_time": 5
        }],
        "Special_menu": [{
            "name": "Chef's vegetarian dish",
            "price": 2.50,
            "calories": 250,
            "prep_time": 10
        },
        {
            "name": "Chef's vegan dish",
            "price": 2.50,
            "calories": 250,
            "prep_time": 10
        }]
    }

    def get_all_menu_names(self) -> dict[int,str]:
        x = 1
        menu_names = {}
        for name in self.MENU_ITEMS:
            menu_names[x]= name
            x += 1
        return menu_names

if __name__ == "__main__":
    menu = Menu()
    print(type(menu.get_all_menu_names()))
