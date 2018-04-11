#!/bin/python

import math

class ESC_ContourEstimator():
    def __init__(self, chain_code):
        self.chain_code = list(chain_code)
        self.n_e = self.determine_even()
        self.n_o = self.determine_odd()
        self.n_c = self.determine_corner()
    
    def determine_even(self):
        return (self.chain_code.count("0") + self.chain_code.count("2") +
                self.chain_code.count("4") + self.chain_code.count("6"))

    def determine_odd(self):
        return (self.chain_code.count("1") + self.chain_code.count("3") +
                self.chain_code.count("5") + self.chain_code.count("7"))

    def determine_corner(self):
        count = 0
        prev = self.chain_code[0]
        for direction in range(1, len(self.chain_code)-1):
            if prev != self.chain_code[direction]:
                count += 1
            prev = self.chain_code[direction]
        return count

    def get_simple(self):
        return (self.n_e + self.n_o)

    def get_freeman(self):
        return (self.n_e + (math.sqrt(2) * self.n_o))
    
    def get_groen_verbeek(self):
        return ((1.059 * self.n_e) + (1.183 * self.n_o))

    def get_profitt_rosen(self):
        return ((0.984 * self.n_e) + (1.340 * self.n_o))

    def get_vossepoel_smeulders(self):
        return ((0.980 * self.n_e) + (1.406 * self.n_o) - (0.091 * self.n_c))
    
