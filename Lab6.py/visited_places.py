# visited_places.py

def show_menu():
    print("******************************************************************")
    print("********************* My Travel List ****************************")
    print("******************************************************************")
    print("*                                                                *")
    print("* Please choose one of the following options:                    *")
    print("*                                                                *")
    print("* (1) Add a new city to the list of visited cities.              *")
    print("* (2) View your list of visited cities.                          *")
    print("* (3) Sort the list of visited cities.                           *")
    print("* (4) Show the number of visited cities.                         *")
    print("* (5) Remove a given city from the list of visited cities.       *")
    print("* (6) Remove all cities from the list of visited cities.         *")
    print("* (7) Save the list of visited cities to a file.                 *")
    print("* (0) Exit                                                       *")
    print("******************************************************************")


def add_city(cities: list[str]) -> None:
    city = input("Enter the name of the city: ").strip()
    if city:
        cities.append(city)
        print(f"{city} added to your travel list!")
    else:
        print("No city entered.")


def view_cities(cities: list[str]) -> None:
    if not cities:
        print("You have not added any cities yet.")
    else:
        print("\nYour visited cities:")
        for i, city in enumerate(cities, 1):
            print(f"{i}. {city}")


def sort_cities(cities: list[str]) -> None:
    cities.sort()
    print("Cities have been sorted alphabetically!")


def count_cities(cities: list[str]) -> None:
    print(f"You have visited {len(cities)} cities.")


def remove_city(cities: list[str]) -> None:
    city = input("Enter the name of the city to remove: ").strip()
    if city in cities:
        cities.remove(city)
        print(f"{city} removed from your travel list.")
    else:
        print(f"{city} not found in your travel list.")


def clear_cities(cities: list[str]) -> None:
    cities.clear()
    print("All cities have been removed from your travel list.")


def save_to_file(cities: list[str]) -> None:
    filename = "visited_cities.txt"
    with open(filename, "w") as file:
        for city in cities:
            file.write(city + "\n")
    print(f"Your travel list has been saved to {filename}!")


def main():
    cities = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_city(cities)
            case "2":
                view_cities(cities)
            case "3":
                sort_cities(cities)
            case "4":
                count_cities(cities)
            case "5":
                remove_city(cities)
            case "6":
                clear_cities(cities)
            case "7":
                save_to_file(cities)
            case "0":
                print("Goodbye! Safe travels!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
