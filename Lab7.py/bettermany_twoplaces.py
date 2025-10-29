import copy
visited_places = {
"city": "",
"country": "",
"dates": [],
}
my_visited_places = []
for i in range(0, 2):
# Make a deep copy of the template for this player
    places = copy.deepcopy(visited_places)
    places["city"] = input("Enter city name: ")
    places["country"] = input("Enter country name: ")
    times = input("How many times you visited?")
for j in range(0, int(times)):
    year = input(f"Enter the year of the {j+1} time you went there: ")
    places["dates"].append(year)
    my_visited_places.append(places)
    print(my_visited_places)