# from parent directory: python -m unittest tests

import unittest
from riverCrossing import GameState
from riverCrossing import Move
from tests import dummyStates
from tests.dummyStates import DummyStates

class testMoveValidity(unittest.TestCase):

    #def __init_ (self):

    #def test_basic(self):
    #    self.assertGreater(sampleSet.len(), 0)
    
    "test for impropper input"
    def test_input(self):
        x = DummyStates()
        sampleSet = x.generate()
        badSubject = Move("Purple people eater.", "boat")
        badLocation = Move("man", "potato")
        for state in sampleSet:
            with self.assertRaises(InvalidMove):
                state.apply_move(badLocation)
            with self.assertRaises(InvalidMove):
                state.apply_move(badSubject)
            "Perhaps add a verification that a valid character/location name does NOT raise an exception?"
            

    "test for enforcement of rules"

    "test for movement accomplished"
