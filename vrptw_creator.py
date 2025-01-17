from random import randint
from math import sqrt, ceil
from sys import float_info
from statistics import mean
import numpy as np

import vrp_creator

class Stop(vrp_creator.Stop):
    def add_time_window(self, earliest_arrival, latest_departure):
        self.earliestArrival = earliest_arrival
        self.latestDeparture = latest_departure
    def add_service_time(self, service_time):
        self.serviceTime = service_time

class Instance(vrp_creator.Instance):
    '''
    Set a unique time window for all available depots. Diferent kinds not supported
    '''
    def set_depot_time_window(self, earliest_arrival, latest_departure):
        self.depotEarliestArrival = earliest_arrival
        self.depotLatestDeparture = latest_departure