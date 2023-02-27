# Task 2B 
# Submodule Flood


from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key



stations_over_threshold = []



def stations_level_over_threshold(stations, tol):
    for station in stations:
        #print("Test: ",station.latest_level)
        if type(station.relative_water_level()) == float and station.typical_range_consistent(): 
            if station.relative_water_level() > tol:
                stations_over_threshold.append((station.name,station.relative_water_level()))
                
    return stations_over_threshold

def stations_highest_rel_level(stations, N):
    stations_over_threshold = stations_level_over_threshold(stations, 0.8)
    sorted_over_threshold = sorted_by_key(stations_over_threshold,1,reverse=True)
    return sorted_over_threshold[:N]
