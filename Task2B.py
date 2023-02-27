
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_within_radius
from flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key



def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8

    stations_over_threshold = stations_level_over_threshold(stations,tol)
    #print(stations_over_threshold)

    # Print these stations
    #stations_over_threshold.sort(key=stations_over_threshold[1],reverse=True)
        
    sorted_over_thresholds = sorted_by_key(stations_over_threshold,1,reverse=True)

    for station in sorted_over_thresholds:
        print("{}, {}".format(
            station[0], station[1]))
   
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
