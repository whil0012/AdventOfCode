import unittest
import NamedPropertyItem
import GetNamedPropertyItemsFromFile


class TestAdventOfCodeDay14(unittest.TestCase):
    def get_reindeer_description_parts(self, reindeer_description):
        return [x.strip() for x in reindeer_description.split(" ")]

    def get_reindeer_comet(self):
        return NamedPropertyItem.named_property_item(name="Comet", speed=14, flight_duration=10, rest_duration=127)

    def get_reindeer_dancer(self):
        return NamedPropertyItem.named_property_item(name="Dancer", speed=16, flight_duration=11, rest_duration=162)

    def test_get_reindeer_from_description_WhenInvoked_ReturnsReindeerName(self):
        reindeer_parts = self.get_reindeer_description_parts("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        actual = get_reindeer_from_description(reindeer_parts)
        self.assertEqual(actual.name, "Comet")

    def test_get_reindeer_from_description_WhenInvoked_ReturnsSpeed(self):
        reindeer_parts = self.get_reindeer_description_parts("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        actual = get_reindeer_from_description(reindeer_parts)
        self.assertEqual(actual.speed, 14)

    def test_get_reindeer_from_description_WhenInvoked_ReturnsFlightDuration(self):
        reindeer_parts = self.get_reindeer_description_parts("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        actual = get_reindeer_from_description(reindeer_parts)
        self.assertEqual(actual.flight_duration, 10)

    def test_get_reindeer_from_description_WhenInvoked_ReturnsRestDuration(self):
        reindeer_parts = self.get_reindeer_description_parts("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        actual = get_reindeer_from_description(reindeer_parts)
        self.assertEqual(actual.rest_duration, 127)

    def test_get_reindeer_distance_WhenCometFor1000Seconds_Returns1120km(self):
        reindeer_comet = self.get_reindeer_comet()
        actual = get_reindeer_distance(reindeer_comet, 1000)
        self.assertEqual(actual, 1120)

    def test_get_reindeer_distance_WhenDancerFor1000Seconds_Returns1056km(self):
        reindeer_dancer = self.get_reindeer_dancer()
        actual = get_reindeer_distance(reindeer_dancer, 1000)
        self.assertEqual(actual, 1056)


reindeer_description_index_name = 0
reindeer_description_index_speed = 3
reindeer_description_index_flight_duration = 6
reindeer_description_index_rest_duration = 13


def get_reindeer_from_description(reindeer_description_parts):
    name = reindeer_description_parts[reindeer_description_index_name]
    speed = int(reindeer_description_parts[reindeer_description_index_speed])
    flight_duration = int(reindeer_description_parts[reindeer_description_index_flight_duration])
    rest_duration = int(reindeer_description_parts[reindeer_description_index_rest_duration])
    return NamedPropertyItem.named_property_item(name=name, speed=speed, flight_duration=flight_duration, rest_duration=rest_duration)


def get_reindeer_distance(reindeer, flight_time):
    reindeer_segment_time = reindeer.flight_duration + reindeer.rest_duration
    full_segments_flown = flight_time // reindeer_segment_time
    full_segments_time_in_air = full_segments_flown * reindeer.flight_duration
    remaining_time = flight_time % reindeer_segment_time
    remaining_time_in_air = min(remaining_time, reindeer.flight_duration)
    return (full_segments_time_in_air + remaining_time_in_air) * reindeer.speed


def main():
    reindeer = GetNamedPropertyItemsFromFile.get_named_property_items_from_file("input/day_14.txt", get_reindeer_from_description)
    max_distance = max([get_reindeer_distance(x, 2503) for x in reindeer])
    print("max distance: ", max_distance)


if __name__ == "__main__":
    main()
