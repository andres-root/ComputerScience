#!/usr/bin/python3


class Unit(object):

    def __init__(self, value, grad):
        self.value = value
        self.grad = grad

    def get(self):
        return self
