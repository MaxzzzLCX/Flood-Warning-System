
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Find stations within 10km radius from the Cambridge city center
    p_cambridge_center = (52.2053, 0.1218)
    radius_r = 10
    list_of_stations_within_radius = stations_within_radius(stations,p_cambridge_center,radius_r)

    # Print these stations
    print("Stations within 10km radius from Cambridge city center")
    print(list_of_stations_within_radius)
   
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
