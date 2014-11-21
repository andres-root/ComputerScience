#!/usr/bin/python3

# App Modules
from .gates import AddGate, MultiplyGate


class Circuit(object):

    def __init__(self):
        self.mulg0 = MultiplyGate()
        self.mulg1 = MultiplyGate()
        self.addg0 = AddGate()
        self.addg1 = AddGate()
