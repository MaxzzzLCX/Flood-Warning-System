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
    """This function takes in a list of stations and a given coordinate, p
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
