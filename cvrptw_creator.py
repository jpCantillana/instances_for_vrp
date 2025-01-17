from random import randint
from math import sqrt, ceil
from sys import float_info
from statistics import mean
import numpy as np

import vrptw_creator

class Stop(vrptw_creator.Stop):
    def add_capacity(self, cap):
        self.capacity = cap

class Instance(vrptw_creator.Instance):
    def set_vehicle_capacity(self, cap):
        self.vehicleCapacity = cap