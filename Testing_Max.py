
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_within_radius
from flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.utils import sorted_by_key



def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    for station in stations:
        if station.name == "St Mary Bourne":
            print(station.typical_range,station.latest_level)
            print("station.typical_range[0]: ", station.typical_range[0])
            print("station.typical_range[1]: ", station.typical_range[1])
            print("calculated relative: ", (station.latest_level-station.typical_range[0])/(station.typical_range[1]-station.typical_range[0]))

   
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
