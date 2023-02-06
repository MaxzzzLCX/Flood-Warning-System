
from Task1B import stations_by_distance
from Task1C import stations_within_radius
from Task1D import rivers_with_station
from Task1D import stations_by_river


def test_task1B():
    """Test for 1B
       Ensure the sorted list in distance is (1)same length (2)sorted"""
    stations = build_station_list()
    task1B_test_stations = stations_by_distance(stations,(52.2053,0.1218))
    assert len(stations) == len(task1B_test_stations)

    x = task1B_test_stations[0]
    for station in task1B_test_stations:
        assert station[1]<=x
        x = station[1]

def test_task1C():
    """Test for 1C
       Ensure all the stations are within the radius of 10km"""
    
    stations = build_station_list()
    task1C_test_stations = stations_within_radius(stations,(52.2053, 0.1218),10)
    
    for station in task1C_test_stations:
        for target in stations:
            if station == target.name:
                assert haversine(target.coord,(52.2053, 0.1218)) <= 10

def test_task1D():
    """Test for 1D
       (1)Ensure lists of all rivers associated with stations has # of station >= 1
       (2)Ensure all stations associated with rivers have the attribute of the corresponding river
    """
    
    stations = build_station_list()

    task1D_test1_stations = rivers_with_station(stations)

    for rivers in task1D_test1_stations:
        found = False
        for target in stations:
            if target.river == rivers:
                found = True
        assert found == True


    task1D_test2_stations = stations_by_river(stations)

    for stations in task1D_test2_stations["River Aire"]:
        for target in stations:
            if stations == target.name:
                assert target.river == "River Aire"