from random import randint
from math import sqrt, ceil
from sys import float_info
from statistics import mean
import numpy as np

# Class Stop: a stop is an geographic object that can contain multiple properties
class Stop(object):
    def __init__(self, id, xcoord, ycoord):
        self.id = id
        self.xcoord = xcoord
        self.ycoord = ycoord
    def add_demand(self, demand):
        self.demand = demand
    def add_timeWindow(self, earliest_arrival, latest_departure):
        self.earliest_arrival = earliest_arrival
        self.latest_departure = latest_departure
    def add_serviceTime(self, service_time):
        self.service_time = service_time

# Class Instance: this is the class that defines an instance
class Instance(object):
    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.vehicles      = 0
        self.stops     = []
    def set_vehicles(self, n):
        self.vehicles = n
    def add_stop(self, id, xcoord, ycoord):
        stop = Stop(id, xcoord, ycoord)
        self.stops.append(stop)

class Scenario(object):
    def __init__(self, width=100, height=100):
        self.width = width
        self.height= height
        self.clusters = [(width/2, height/2, "no-dist")]
        self.depots = []
    def set_location_distribution(self, cluster, distr_name):
        '''
        For a given position of the clusters in the scenario (by default at least 1), define the distribution.
        Allowed distributions:
        - Bivariate normal ("bivN")
        - Univariate double normal ("uniN")
        - Univariate double uniform ("uniU")
        '''
        self.clusters[cluster][2] = distr_name
    def add_depot(self, x, y, dist="no-dist"):
        '''
        Allowed distributions:
        - no-dist: just the given position
        - central: close to the given position
        - annular: some distance from the given position
        - satellite: closer to the borders
        '''
        self.depots.append((x,y, dist))