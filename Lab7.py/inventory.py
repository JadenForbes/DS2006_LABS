# inventory_manager.py

inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "kiwi": 60,
    "cherry": 40
}


def show_menu():
    print("\n******** Inventory Manager ********")
    print("(1) Add stock for an item")
    print("(2) Remove stock for an item")
    print("(3) Check stock of a specific item")
    print("(4) View all items in stock")
    print("(0) Exit")
    print("***********************************")


def add_stock(item: str, amount: int):
    if item in inventory:
        inventory[item] += amount
        print(f"Added {amount} {item}(s). New stock: {inventory[item]}")
    else:
        print(f"{item} is not in inventory.")


def remove_stock(item: str, amount: int):
    if item in inventory:
        if inventory[item] >= amount:
            inventory[item] -= amount
            print(f"Removed {amount} {item}(s). New stock: {inventory[item]}")
        else:
            print(f"Not enough {item}s in stock to remove {amount}. Current stock: {inventory[item]}")
    else:
        print(f"{item} is not in inventory.")


def check_stock(item: str):
    if item in inventory:
        print(f"{item.capitalize()} stock: {inventory[item]}")
    else:
        print(f"{item} is not in inventory.")


def view_all():
    print("\nCurrent Inventory:")
    for item, qty in inventory.items():
        print(f"- {item.capitalize()}: {qty}")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                item = input("Enter item name: ").strip().lower()
                amount = int(input("Enter quantity to add: "))
                add_stock(item, amount)
            case "2":
                item = input("Enter item name: ").strip().lower()
                amount = int(input("Enter quantity to remove: "))
                remove_stock(item, amount)
            case "3":
                item = input("Enter item name: ").strip().lower()
                check_stock(item)
            case "4":
                view_all()
            case "0":
                print("Exiting Inventory Manager. Goodbye!")
                break
            case _:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
