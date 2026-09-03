# creating dictionaries for price and quantity of items 
stock = {
    "Rice": 60,
    "Eggs": 40,
    "Bread" : 20,
    "Wheat" : 50,
    "Sugar" : 30,
    "Oil": 10
}

price = {
    "Rice": 150,
    "Eggs": 55,
    "Bread" : 60,
    "Wheat" : 100,
    "Sugar" : 80,
    "Oil": 200
}

bills = [] # creating a list to store items, quantity and price per unit

def show_stock():
    print("\nAvailable stock:")
    for item in stock: # declairing a variable item to search through the stock dictionary 
        print(item,"-",stock[item], "units. \nPrice:", price[item])
    print()


def purchase_item():
    item = input("Enter the item name")
    if item not in stock:
        print("Item not found in stock.")
        return 
    
    qty = int(input("Enter the quantity."))
    if stock[item] >= qty:
        price_per_unit = price[item]
        bills.append((item, price_per_unit, qty))
        stock[item] -= qty
        print("Added to bill.")
    else:
        print("Desired quantity not in stock, only", stock[item], "available.")


def print_bill():
    if len(bills) == 0:
        print("No items purchased.") 
        return 


    print("\n----------Grocery Bill----------")
    total = 0 
    for item, price_per_unit, qty in bills:
        amount = qty * price_per_unit
        total = total + amount
        print(item, "x", qty, "@", price_per_unit, "=", amount) 

    print("Total Bill: ",total)
    print("----------------------------------")

#----------Main Menu----------

while True:
    print("1.Show Stock")
    print("2.Purchase Item")
    print("3.Print Bill")
    print("4.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_stock()
    elif choice == 2:
        purchase_item()
    elif choice == 3:
        print_bill()
    elif choice == 4:
        print_bill()
        break
