SUITS = { 'CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS' }
RANKS = [ 'ACE', 'KING', 'QUEEN', 'JACK', 'TEN',
         'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO' ]

def deck() -> list[tuple]:
    '''Create a deck of cards.
    Each card is a tuple of suit and rank.
    '''
    pass

def split(deck, pos: int) -> tuple[list, list]:
    ''''Split a deck of cards at a given position.
    Return a tuple containing first and second part of the deck.
    '''
    pass

def peek(deck: list[tuple]) -> tuple:
    '''Show top card from the deck.
    '''
    pass

def draw(deck: list[tuple], random=False) -> tuple:
    '''Draw a card from the deck.
    Choose a random card when random=True,
    otherwise choose top card.
    
    Hint: Use the randint() function:
    from random import randint
    '''
    pass

def filter_by(deck: list[tuple], suit=None, rank=None) -> list[tuple]:
    '''Filter the deck by the given suit and rank.
    When only suit is given, include cards of all ranks with the given suit.
    When only rank is given, include cards of all suits with the given rank.
    When both are given, only include cards with the given suit and rank.
    When none are given, include all cards (no effect).
    '''
    pass