import unittest
import random

from exercises.composite_types import *

class TestBasics(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        random.seed(1337)
        
        self.deck = None
    
    def test_deck(self):
        self.deck = deck()
        self.fail('Not implemented yet.')

    def test_split(self):
        first, second = split(self.deck)
        self.fail('Not implemented yet.')
    
    def test_peek(self):
        card = peek(self.deck)
        self.fail('Not implemented yet.')
    
    def test_draw(self):
        card = draw(self.deck)
        card2 = draw(self.deck, random=True)
        self.fail('Not implemented yet.')