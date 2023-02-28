# Task 2B 
# Submodule Flood


from .stationdata import build_station_list
from .station import MonitoringStation
from .utils import sorted_by_key




def stations_level_over_threshold(stations, tol):
    stations_over_threshold = []
    for station in stations:
        #print("Test: ",station.latest_level)
        if type(station.relative_water_level()) == float and station.typical_range_consistent(): 
            if station.relative_water_level() > tol:
                stations_over_threshold.append((station.name,station.relative_water_level()))
                
    return stations_over_threshold

def stations_highest_rel_level(stations, N):
    def rel_lvl(station):
        return station.relative_water_level()
    stations_highest_rel_lvl = []
    for station in stations:
        #print("Test: ",station.latest_level)
        if type(station.relative_water_level()) == float and station.typical_range_consistent():
            stations_highest_rel_lvl.append(station)
    stations_highest_rel_lvl.sort(reverse = True, key = rel_lvl)
    return stations_highest_rel_lvl[:N]
