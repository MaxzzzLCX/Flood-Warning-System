# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

# import the tool that is used to calculate the distance between two given points of long. and lat.
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    """Task 1B
       This function takes in a list of stations and a given coordinate, p
       It returns a list of tuples: including stations with their distance from p
    """

    stations_distances = []
  
    for station in stations:
        """For every station in the list, calculate its distance from p
           Store the station with the distance in a list "stations_distances"
        """
        distance = haversine(station.coord,p)
        stations_distances.append((station.name,distance))

    return sorted_by_key(stations_distances,1) # Sort by the second entry (distance from p)


def stations_within_radius(stations, centre, r):
    """Task 1C
       This function takes in a list of stations, a given centre, and a radius r
       It returns a list with all stations within a radius r from the center
    """

    stations_within_radius = []

    for station in stations:
        distance = haversine(station.coord,centre)
        if distance <= r:
            stations_within_radius.append(station.name)
    
    return sorted_by_key(stations_within_radius,0)


def rivers_with_station(stations):
    """Task 1D (1)
       This function takes in a list of stations
       It returns a non-duplicate set of rivers associated with the list of stations
    """

    set_of_rivers_with_station = set()

    for station in stations:
        set_of_rivers_with_station.add(station.river)
    
    return sorted_by_key(set_of_rivers_with_station,0)

def stations_by_river(stations):
    """Task 1D (2)
       This function takes in a list of stations
       It returns a dictionary that maps river names to a list of station objects
    """

    dictionary_of_rivers_to_stations = {}

    for station in stations:
        # If this river is already in the dictionary, add the station to the list associated with the river
        # If the river is new, add an new entry to the dictionary
        if station.river in dictionary_of_rivers_to_stations:
            dictionary_of_rivers_to_stations[station.river].append(station.name)
        else:
            dictionary_of_rivers_to_stations[station.river] = [station.name]
    
    return dictionary_of_rivers_to_stations