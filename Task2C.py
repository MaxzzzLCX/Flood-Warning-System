
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.utils import sorted_by_key



def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    N=10



    stations_highest_relative_level = stations_highest_rel_level(stations,N)

    for station in stations_highest_relative_level:
        print("{}, {}".format(
            station.name, station.relative_water_level()))
   
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
