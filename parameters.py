#!/usr/bin/env python3
import interface
import nodeSystem.NodeSystem as ns
class Parameters:
    def __init__(self, n, mask_procent, vac_procent, mortality_rate):
       self.mask_procent = mask_procent
       self.vac_procent = vac_procent
       self.mortality_rate = mortality_rate


def get_population():
    return interface.get_population()

def get_vaccinated():
    return interface.get_vaccinated()

def get_masks():
    return interface.get_masks()

def get_iterations():
    return interface.get_iterations()

def get_mortality_rate():
    return interface.get_mortality_rate()

def get_node_radius():
    return ns.get_radius()

def get_node_speed():
    """returns 1,2 array of x and y speeds"""
    return ns.get_speed()

def get_node_size():
    return ns.get_size()

def get_infection_risk():
    return ns.get_infection_risk()

def get_infection_period():
    return ns.get_infection_period()

def get_immune_period():
    return ns.get_immune_period()
