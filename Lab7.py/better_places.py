import copy

# Template for each visited place
visited_places_template = {
    "city": "",
    "country": "",
    "dates": [],
}

def main():
    my_visited_places = []

    # Ask how many cities the user wants to add
    num_cities = int(input("How many cities do you want to add? "))

    for i in range(num_cities):
        print(f"\n--- City {i+1} ---")
        # Make a deep copy of the template
        place = copy.deepcopy(visited_places_template)

        place["city"] = input("Enter city name: ")
        place["country"] = input("Enter country name: ")

        times = int(input(f"How many times have you visited {place['city']}? "))

        for j in range(times):
            year = input(f"Enter the year of visit {j+1}: ")
            place["dates"].append(year)

        # Save this place in the list
        my_visited_places.append(place)

    # Show the final result
    print("\nYour visited places:")
    for place in my_visited_places:
        print(f"{place['city']}, {place['country']} → Years visited: {', '.join(place['dates'])}")


if __name__ == "__main__":
    main()
