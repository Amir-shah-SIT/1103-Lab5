import json

def add_product():
    print("Add New Product")
    productIDinput = input("Product ID:").upper()
    productNameinput = input("Product Name: ")
    while True:
        try:
            productPriceinput = float(input("Price: "))
            break
        except ValueError:
            print("Enter only a number.")
    while True:
        try:
            productStockinput = int(input("Stock Quantity: "))
            break
        except ValueError:
            print("Enter only a integer.")
    newProduct = {
        "productID" : productIDinput,
        "productName" : productNameinput,
        "productPrice" : productPriceinput,
        "productStock" : productStockinput
    }
    print(inventory)
    inventory[productIDinput] = newProduct

    return

def update_stock():
        updateStockinput = input("Enter Product ID: ").upper()
        if updateStockinput in inventory:
            print("Product Found.")
            print("Name: " + inventory[updateStockinput]["productName"])
            print("Current Stock: "+ str(inventory[updateStockinput]["productStock"]))
            try:
                newstockInput = int(input("New Stock Quantity: "))
                inventory[updateStockinput]["productStock"] = newstockInput
                return 
            except ValueError:
                print("Please enter an integer.")
        else:
            print("Product not found.")

def search_product():
    print("Search Product")
    searchProductinput = input("Enter Product ID: ").upper()
    if searchProductinput in inventory:
        print("Product Found")
        print("---------------------------")
        print("ID: " + inventory[searchProductinput]["productID"])
        print("Name: " + inventory[searchProductinput]["productName"])
        print("Price: " + str(inventory[searchProductinput]["productPrice"]))
        print("Stock: " + str(inventory[searchProductinput]["productStock"]))

        print("---------------------------")
    else:
        print("Product not found:")
    return

def display_all():
    for Value in inventory.values():
        print("ID: " + Value["productID"] + " | Name: " + Value["productName"] + " | Price: $"+ str(Value["productPrice"]) + " | Stock: " + str(Value["productStock"]))
    print("\n")
    return

def mainMenuBanner():
    print("=========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=========================================\n")
        
def mainMenuOptions():
    print("\n------------------------")
    print("1. Display All Products")
    print("2. Add Products")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------\n")
    while True:
        try:
            mainMenuInput = int(input("Enter Option: "))
            if mainMenuInput > 0 and mainMenuInput < 7:
                return mainMenuInput
            else:
                print("please only enter a number between 1-6.")
        except ValueError:
            print("please only enter a number between 1-6.")

def load_inventory():
    try:
        with open('inventory.json', 'r', encoding='utf-8') as file:
            print("Inventory.json found.")
            print("Inventory loaded successfully.")
            loadedinventory = json.load(file)
            return loadedinventory
    except FileNotFoundError:
        with open("inventoryList.txt", "w+") as file:
            json.dump(inventory, file, indent=4)
            return {}

def save_inventory():
    with open("inventory.json", "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4, sort_keys=True)
    print("Inventory save successfully.\n")
mainMenuBanner()
inventory = load_inventory()
while True:
    menuInput = mainMenuOptions()
    print("\n")
    match menuInput:
        #Display product
        case 1:
            display_all()
            
        #Add Products
        case 2:
            add_product()
        #update Stock
        case 3:
            update_stock()
        #Search Product
        case 4:
            search_product()
        #save inventory
        case 5:
            print("saving now...")
            save_inventory()
        #quit
        case 6:
            print("Saving inventory before exiting...")
            save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program Terminated.")
            break
