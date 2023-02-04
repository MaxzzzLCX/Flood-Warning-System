
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Part 1: Find all the rivers that are associated with the list of stations
    # Output the first 10 in alphabetical order
    set_of_rivers = rivers_with_station(stations)
    print("Number of rivers: ", len(set_of_rivers))
    print(set_of_rivers[:10])

    # Part 2: Create a dictionary that maps river to a list of stations
    dictionary_river_to_stations = stations_by_river(stations)
    # Output the stations that are associated with River Aire, River Cam, and River Thames
    print("River Aire: \n", sorted(dictionary_river_to_stations["River Aire"]),"\n")
    print("River Cam: \n", sorted(dictionary_river_to_stations["River Cam"]),"\n")
    print("River Thames: \n", sorted(dictionary_river_to_stations["River Thames"]),"\n")
    
   
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
