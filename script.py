destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]


# Inputs location from destinations and returns output of that location
def get_destination_index(destination):
    destination_index = [i for i in range(len(destinations)) if destination == destinations[i]]

    return destination_index[0]


print(get_destination_index("Paris, France"))


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)


attractions = []
for place in range(5):
    attractions.append([])
print(attractions)


def add_attraction(destination):
    try:
        destination_index = get_destination_index(destination)
        return destination_index
    except IndexError:
        print("That destination doesn't exist!")



print(add_attraction("Pari France"))
