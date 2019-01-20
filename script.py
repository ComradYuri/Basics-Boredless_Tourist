destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]


# Inputs string of location and returns index number of that location
def get_destination_index(destination):
    try:
        destination_index = [i for i in range(len(destinations)) if destination == destinations[i]]
        return destination_index[0]
    except IndexError:
        return "That location doesn't exist!"


# will print: 0
print(get_destination_index("Paris, France"))


# Will extract location from traveler list and return index of his location
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# An empty list of lists with the attractions of each location can be stored
attractions = []
for place in range(5):
    attractions.append([])
print(attractions)


# Adds attractions to the list attractions. Input is the string of the location and the to be added attraction.
# if the location exists it adds the attraction to the list of attraction in the correct location.
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index]
        return attractions_for_destination.append(attraction)

    except IndexError:
        return


# adding new attractions to attractions
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Paris, France", ["Montmartre", ["historical site"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", ""]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions[get_destination_index("Paris, France")])


# Input is the string of the destination and list with strings of interests.
# Returns attractions in destination that match interests
def find_attractions(destination, interests):
    # gets destination index
    destination_index = get_destination_index(destination)
    # gets list of attractions from the destination
    attractions_in_city = attractions[destination_index]
    # create new list that will store attractions of interest
    attractions_with_interest = []
    # creates list attraction_tags and loops trough it checking if it matches an interest from interests list
    for attraction in attractions_in_city:
        possible_attraction = attraction
        # extracts tags from attractions_in_city
        attraction_tags = attraction[1]
        # loops through inputted interests and appends possible_attractions to attractions_with_interest
        for interest in interests:
            # checks for matches between interests and possible attractions
            if interest in attraction_tags:
                # appends attraction (only attraction name, not tags because it takes index 0 from list)
                attractions_with_interest.append(possible_attraction[0])
    # returns updated attraction_with_interest list
    if len(attractions_with_interest) == 0:
        attractions_with_interest.append("""none. You possibly made a spelling error. 
If not there are no matches in our system""")
    return attractions_with_interest


la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)


# Input is a list of traveler information. Returns travelling advice.
def get_attractions_for_traveler(traveler):
    # get destination string
    traveler_destination = traveler[1]
    # get interest string
    traveler_interests = traveler[2]
    # get attraction list for traveler
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    # create the string that will be returned
    interest_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    # correctly sums the attractions with correct punctuation
    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            if traveler_attractions == ["""none. You possibly made a spelling error. 
If not there are no matches in our system"""]:
                interest_string += traveler_attractions[i] + "."
            else:
                interest_string += "the " + traveler_attractions[i] + "."
        else:
            interest_string += "the " + traveler_attractions[i] + ", "
    return interest_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument', 'historical sit']])
print(smills_france)
