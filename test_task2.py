from floodsystem.stationdata import build_station_list

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.utils import sorted_by_key
import random


def test_task2B():
    """Test for 1B
       Ensure the sorted list in distance is (1)same length (2)sorted"""
    
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8

    stations_over_threshold = stations_level_over_threshold(stations,tol)

    sorted_over_thresholds = sorted_by_key(stations_over_threshold,1,reverse=True)
    temp = 99999

    for test_station in sorted_over_thresholds:
        assert test_station[1] <= temp
        temp = test_station[1]

    

    # test_task2B_stations = []
    # for i in range (500):
    #     N = random.randint(0,999)
    #     test_task2B_stations.append([i,random.randint(0,N),random.randint(N,999),random.randint(0,999)])
    # #print(test_task2B_stations)

    # MonitoringStation 

    # for station in test_task2B_stations:
    #     latest_level.append(random.randint(0,999))
    

test_task2B()

def test_task2C():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    N=10

    stations_over_threshold = stations_highest_rel_level(stations,N)

    assert(len(stations_over_threshold)==N)

    sorted_over_thresholds = sorted_by_key(stations_over_threshold,1,reverse=True)
    temp = 99999

    for test_station in sorted_over_thresholds:
        assert test_station[1] <= temp
        temp = test_station[1]



