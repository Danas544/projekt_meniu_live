from tables import str_to_time
from datetime import datetime
def choose_input() -> int:
    while True:
        print("Choose: \n 1. Reserve a table \n 2. Check reservation \n 3. I arrived \n 4. Exit")
        try:
            choice = int(input())
        except ValueError:
            print("There are try choices 1, 2, 3 or 4")
            continue
        if choice not in [1,2,3,4] or choice == str:
            print("There are try choices 1, 2, 3 or 4")
            continue
        return choice


def choose_table() -> str:
    while True:
        table = int(input('1. single, 2. double, 3. family: '))
        if table not in [1,2,3]:
            print("There are try choices 1, 2, 3")
            continue
        if table == 1:
            table = "Single table"
        elif table == 2:
            table = "Double table"
        elif table == 3:
            table = "Family table"
        return table

def choose_time() -> "datetime":
    while True:
        time = input("formatas (2023-03-28 12:00), Rezervacijos laikas: ")
        time = time + ":00"
        try:
            time = str_to_time(time)
        except ValueError:
            print("Blogai ivestas laikas")
            continue
        return time
