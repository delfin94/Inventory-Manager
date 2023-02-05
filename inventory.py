#========The beginning of the class==========
class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost


    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as shoe_data:
            read_data = shoe_data.readlines()
            for index in range(1, len(read_data)):  # Starts looping from the second line
                read_split = read_data[index].strip().split(",")
                shoe_list.append(Shoes(read_split[0], read_split[1], read_split[2], float(read_split[3]), int(read_split[4])))
    except FileNotFoundError:
        print("The file is not found.")


"""
The function above pulls the data from the database (text file) and stores it in a local list to be manipulated.
"""

def capture_shoes():
    country = input("Enter the country of origin: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the name of the shoe: ")
    cost = float(input("Enter the cost of the shoe: "))
    quantity = int(input("Enter the quantity of the shoe: "))
    shoe_list.append(Shoes(country, code, product, cost, quantity))


"""
The function above allows the user to enter in a new shoe object.
"""

def view_all():
    for shoe in shoe_list:
        print(shoe)


"""
The function above prints out the entire list.
"""

def re_stock():
    min_quantity = min([shoe.quantity for shoe in shoe_list])  # Finds the minimum quantity
    for shoe in shoe_list:
        if shoe.quantity == min_quantity:  # Finds the minimum quantity shoe
            re_stock_shoe = shoe  # Puts the least quantity shoe object into the new variable to manipulate
            break
    choice = input(f"Do you want to re-stock {re_stock_shoe.product}? (Y/N) ")
    if choice.lower() == "y":
        quantity = int(input("Enter the quantity to re-stock: "))
        re_stock_shoe.quantity += quantity
        with open("inventory.txt", "w") as file:
            file.write("country,code,product,cost,quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


"""
The function above finds the lowest stock. Ask if we want to restock it. If yes, then adds goes on to ask how much
 we would like to stock up. Adds the old value with the new restock amount to give our new stock value.
"""

def seach_shoe(code):
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)


"""
The function above prints out the object with the specific SKU number you enter.
"""

def value_per_item():
    total_value = 0
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        total_value += value
        print(f"Value of {shoe.product}: {value}")
    print(f"Total value: {total_value}")


"""
The function above, loops through entire list and takes the cost of each shoe object, so that it can calculate the value
of each item. This function also returns the total inventor stock value.
"""

def highest_qty(shoe_list):
    highest_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity > highest_shoe.quantity:
            highest_shoe = shoe
    print(f"{highest_shoe.product} are on sale!")


"""
The function above, places the first object into a variable (highest_shoe). Loops through all list and compares the quantity of each item
with the one stored in the variable. If the quantity is higher then, the object in the variable will be replaced. After
the loop has finished running, it prints out the shoes with the most quantity.
"""

#==========Main Menu=============
def main():
    while True:
        print("1. Read shoes data from file")
        print("2. Capture a new shoe")
        print("3. View all shoes")
        print("4. Restock shoes")
        print("5. Search for a shoe")
        print("6. Value per item")
        print("7. Highest quantity shoe")
        print("8. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            view_all()
        elif choice == 4:
            re_stock()
        elif choice == 5:
            code = input("Enter shoe code: ")
            seach_shoe(code)
        elif choice == 6:
            value_per_item()
        elif choice == 7:
            highest_qty(shoe_list)
        elif choice == 8:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()