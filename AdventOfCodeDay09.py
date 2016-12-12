import unittest
import NamedPropertyItem
import itertools


class TestAdventOfCodeDay09(unittest.TestCase):
    def testFindShortestPath_TwoCities_ReturnsDistanceBetweenTwoCities(self):
        location_distance_pair1 = NamedPropertyItem.named_property_item(city1="London", city2="Dublin", distance=464)
        shortest_route_distance = calculate_shortest_route_distance([location_distance_pair1])
        self.assertEqual(shortest_route_distance, 464, "shortest route distance")

    def testFindShortestPath_ThreeCities_ReturnsShortestDistance(self):
        distance_london_dublin = NamedPropertyItem.named_property_item(city1="London", city2="Dublin", distance=464)
        distance_london_belfast = NamedPropertyItem.named_property_item(city1="London", city2="Belfast", distance=518)
        distance_dublin_belfast = NamedPropertyItem.named_property_item(city1="Dublin", city2="Belfast", distance=141)
        shortest_route_distance = calculate_shortest_route_distance([distance_dublin_belfast, distance_london_belfast, distance_london_dublin])
        self.assertEqual(shortest_route_distance, 605, "shortest route distance")

    def testFindLongestPath_ThreeCities_ReturnsLongestDistance(self):
        distance_london_dublin = NamedPropertyItem.named_property_item(city1="London", city2="Dublin", distance=464)
        distance_london_belfast = NamedPropertyItem.named_property_item(city1="London", city2="Belfast", distance=518)
        distance_dublin_belfast = NamedPropertyItem.named_property_item(city1="Dublin", city2="Belfast", distance=141)
        longest_route_distance = calculate_longest_route_distance([distance_dublin_belfast, distance_london_belfast, distance_london_dublin])
        self.assertEqual(longest_route_distance, 982, "longest route distance")


def get_unique_cities(city_distances):
    unique_cities = set()
    for city_distance in city_distances:
        if city_distance.city1 not in unique_cities:
            unique_cities.add(city_distance.city1)
        if city_distance.city2 not in unique_cities:
            unique_cities.add(city_distance.city2)
    return unique_cities


def get_distance(city1, city2, city_distances):
    for city_distance in city_distances:
        if (city1 == city_distance.city1) and (city2 == city_distance.city2):
            return city_distance.distance
        elif (city1 == city_distance.city2) and (city2 == city_distance.city1):
            return city_distance.distance


def calculate_route_distance(route, city_distances):
    route_distance = 0
    previous_city = None
    for next_city in route:
        if previous_city is not None:
            distance = get_distance(previous_city, next_city, city_distances)
            route_distance += distance
        previous_city = next_city
    return route_distance


def calculate_shortest_route_distance(city_distances):
    shortest_distance = 0
    unique_cities = get_unique_cities(city_distances)
    unique_cities_combinations = itertools.permutations(unique_cities)
    for unique_cities_combination in unique_cities_combinations:
        distance = calculate_route_distance(unique_cities_combination, city_distances)
        if (shortest_distance == 0) or (distance < shortest_distance):
            shortest_distance = distance
    return shortest_distance


def calculate_longest_route_distance(city_distances):
    longest_distance = 0
    unique_cities = get_unique_cities(city_distances)
    unique_cities_combinations = itertools.permutations(unique_cities)
    for unique_cities_combination in unique_cities_combinations:
        distance = calculate_route_distance(unique_cities_combination, city_distances)
        if distance > longest_distance:
            longest_distance = distance
    return longest_distance


def get_city_distance(city_distance_description):
    description_segments = [x.strip() for x in city_distance_description.split(" ")]
    return NamedPropertyItem.named_property_item(city1=description_segments[0], city2=description_segments[2], distance=int(description_segments[4]))


def get_city_distances_from_input_file(input_file_name):
    city_distances = []
    with open(input_file_name, "r") as input_file:
        for city_distance_description in input_file:
            city_distance = get_city_distance(city_distance_description)
            city_distances.append(city_distance)
    return city_distances


def main():
    city_distances = get_city_distances_from_input_file("input/day_09.txt")
    shortest_distance = calculate_shortest_route_distance(city_distances)
    longest_distance = calculate_longest_route_distance(city_distances)
    print("shortest distance: ", shortest_distance)
    print("longest distances: ", longest_distance)


if __name__ == "__main__":
    main()
