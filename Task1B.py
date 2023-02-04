
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Sort the stations in terms of their distance from p
    p_cambridge_center = (52.2053, 0.1218)
    stations_sorted_by_distance_p = stations_by_distance(stations,p_cambridge_center)

    # Print 10 closest and 10 furthest stations
    print("10 closes stations from Cambridge city center")
    print(stations_sorted_by_distance_p[:10])
    print("10 furthest stations from Cambridge city center")
    print(stations_sorted_by_distance_p[-10:])



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
