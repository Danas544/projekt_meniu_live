# Cafeteria project : Create an live menu and payment system (a.k.a console program) :

# First the program should ask if table was reserved/ not (Providing your full name) . And then if not would assign you a table
# (there is a specific number single, double or family tables) . After table is assigned to you, system should show how many free
# tables are and how which are reserved/occupied. The system must be able to show name/surname of the person of the reserved table
# (CLI option : enter reserved table nuber ; OUTCOME: Name/Surname/Time Reserved)
# After assigning table, system should show different menu options for breakfast, lunch , dinner , drinks
# (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan must be included too in the special menu. All menu items should have weight,
# preparation time in minutes, calories, and price.
# I have to have an option to change the order before the payment section. Thus I can delete, add more, update amount of the same order.
# I should be able to choose whatever I want from all menus in one ordering. After I finish, I need to see what I chosen, the full payable amount
# and approx waiting time for the food to be served
# Add an option to add tips (% from the full cost) to the final bill.
# After the payment , system should generate the receipt (logging).

# pirma rasai varda patikrinam ar yra rezervaves jei yra rezervaves soriukas toks staliukas rezervuotas atsilaisvintu apie 18val
# rezervuojam tam laikui ar pasirenkam kita stala? pasirinkus varianta tipo jau sedam i vieta (padaveja turi galimybe pasitikrinti pagal staliuko numeri ar rezervuots
# jei rezervuotas parodo name, surname , laika)
# duoda pasirinkti zmogui 4 variantus meniu , pusryciai , pietus , vakariene , gerimai, specialus meniu(veganams)
# prie kiek vieno patiekalo turi buti: svori , per kiek laiko pagamina , kalorijos , kaina.
# klientas turi tureti galimybe užsisakyti , bet jei dar nesumokejas pakeisti užsakyma , pvz prideti kitu patiekalu , pakeisti kieki , istrinti patiekala
# kaip baigia spaudzia paziureti uzsakyma ir parodo ka susidejo i krepseli su pavadinimu kiekiu , kaina bendra suma krc ir kiek laiko reikės laukti maisto.
# pavalgius ir norint susimokėti yra galimybe pridėti tipsui padavejui (savo nuožiura) arba 5 , 10 , 20 , 50%
# ir pasirinkti apmokėjimo buda , jei kortele tiksli suma , jei grynais duoda pasirinkti kiek duoda
# kvite matosi , patiekalai kiek , kaina , bendra suma , kiek tipsu dave jei dave, bendra suma su tips , kiek dave pinigu jei grynais
# kiek grazos turime duoti, jei kortele tai viskas zjbys kortele 50 viso 50
import tables
import meniu
import time as sleep
da

print("Hello, welcome to my restaurant")
print("Choose: \n 1. Reserve a table \n 2. Check reservation \n 3. I arrived \n 4. Exit")

start = True
reserve_table = tables.ReservTable()
while start:
    try:
        choice = int(input())
    except ValueError:
        choice = None

    if choice == 1:
        name = str(input("Vardas: "))
        surname = str(input("Pavardė: "))
        while True:
            try:
                table = int(input('1. single, 2. double, 3. family: '))
            except:
                table = None
            if table == 1:
                table = "Single table"
                break
            elif table == 2:
                table = "Double table"
                break
            elif table == 3:
                table = "Family table"
                break
            else:
                print("Yra tik trys pasirinkimai 1,2 arba 3")
        while True:
            while True:
                try:
                    time = input("formatas (2023-03-28 12:00), Rezervacijos laikas: ")
                    time = time + ":00"
                    break
                except:
                    print("Blogai ivestas laikas")
                    print("Laiko formatas (2023-03-28 12:00)")



            status, info = reserve_table.book_table(name= name, surname= surname, time= time, table_name= table)
            if status == False:
                print(info)
            else:
                print(info)
                sleep.sleep(1)
                customer_info = reserve_table.get_table_info_by_customer_surname(customer_surname= surname)
                print(f' Table: {customer_info[1]} \n Name: {customer_info[0]["name"]} \n Surname: {customer_info[0]["surname"]} \n Time: {customer_info[0]["time"]} \n')
                sleep.sleep(1)
                print("Choose: \n 1. Reserve a table \n 2. Check reservation \n 3. I arrived \n 4. Exit")
                break


    elif choice == 2:
        while True:
            surname = str(input("Pavardė: "))
            customer_info = reserve_table.get_table_info_by_customer_surname(customer_surname=surname)
            if type(customer_info) == str:
                print(customer_info)
            else:
                print(f' Table: {customer_info[1]} \n Name: {customer_info[0]["name"]} \n Surname: {customer_info[0]["surname"]} \n Time: {customer_info[0]["time"]} \n')
                sleep.sleep(1)
                print("Choose: \n 1. Reserve a table \n 2. Check reservation \n 3. I arrived \n 4. Exit")
                break
    elif choice == 3:
        print('I arrived')
        menu = meniu.Menu()
        menu_names = menu.get_all_menu_names()
        print("Choose: \n")
        for keys,names in menu_names.items():
            print(f"{keys}. {names}")

        choice = int(input())



        print("Choose: \n 1. Reserve a table \n 2. Check reservation \n 3. I arrived \n 4. Exit")
    elif choice == 4:
        print("GoodBye")
        start = False
    else:
        print("There are try choices 1, 2, 3 or 4")










