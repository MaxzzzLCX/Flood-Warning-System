
from floodsystem.stationdata import build_station_list, update_water_levels
from flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.utils import sorted_by_key



def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    N=10



    stations_highest_relative_level = stations_highest_rel_level(stations,N)

    for station in stations_highest_relative_level:
        print("{}, {}".format(
            station[0], station[1]))
   
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
