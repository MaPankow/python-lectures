SUITS = [ 'CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS' ]
RANKS = [ 'ACE', 'KING', 'QUEEN', 'JACK', 'TEN', 'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO' ]

def deck():
    cards = []
    for suit in SUITS:
        for rank in RANKS:
            card = (suit, rank)
            cards.append(card)
    return cards
 
print(deck())
cards = deck()
print(len(cards))


    

def split(deck, pos: int) -> tuple[list, list]:
    ''''Split a deck of cards at a given position.
    Return a tuple containing first and second part of the deck.
    '''
    
    deck1 = deck[ : pos]
    deck2 = deck[pos : ]
    return deck1, deck2

a, b = split(cards, 45)
print(a)
print('--------')
print(b)

def peek(deck: list[tuple]) -> tuple:
    '''Show top card from the deck.
    '''
    pass

def draw(deck: list[tuple], random=False) -> tuple:
    '''Draw a card from the deck.
    Choose a random card when random=True,
    otherwise choose top card.
    '''
    pass

# filter by suit
# filter by rank
# contains specific rank