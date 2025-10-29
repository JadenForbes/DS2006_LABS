visited_places = {
"city": "",
"country": "",
"date": "",
}
my_visited_places = []
for i in range(0, 2):
# Make a copy of the dictionary template:
    places = visited_places.copy()
    places["city"] = input("Enter city name: ")
    places["country"] = input("Enter country name: ")
    places["date"] = input("Enter the year: ")
    my_visited_places.append(places)
    print(my_visited_places)