from menu_manager import MenuManager

def load_manager(): 
    instance = MenuManager()
#    print("hey")
    return instance
    
def show_user_menu(): 
    choice_user  = input("(a) Add an item\n(d) Delete an item\n(v) View the menu\n(x) Exit\n>>>")
    if choice_user == "a": 
        add_item_to_menu()
    elif choice_user == "d":
        remove_item_from_menu()
    elif choice_user == "v": 
        show_restaurant_menu()
    elif choice_user == "x": 
        manager = load_manager()
        manager.save_to_file()
    
def add_item_to_menu(): 
    name   = input("Please add the name\n>>> ")
    price  = input("Please add the price\n>>> ")
    spice  = input("Please add the spice level\n>>> ")
    gluten = input("Please add the gluten index (Just give True or False answer)\n>>> ")
    print("Great, your new item was added!")
    manager = load_manager()
    manager.add_item(name, price, spice, gluten)
    manager.save_to_file()
            
def remove_item_from_menu(): 
    name = input("Please write the name of the item you want to remove\n>>> ")
    manager = load_manager()
    manager.remove_item(name)
    manager.save_to_file()
    
def show_restaurant_menu(): 
    with open("menu.json", "r") as f: 
        menu = json.load(f)
        for item in menu["items"]:
            print(item["name"],"it cost: ", item["price"])

#def update_item_from_menu():    
    
    

load_manager()
show_user_menu()   
show_restaurant_menu()     