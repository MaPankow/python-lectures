from random import randint, shuffle

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
print('--------')
def peek(deck: list[tuple]) -> tuple:
    '''Show top card from the deck.
    '''
    #random.shuffle(deck)
    return deck[-1]
    
print(peek(cards))

print('---------')

def draw(deck: list[tuple], random=False) -> tuple:
    '''Draw a card from the deck.
    Choose a random card when random=True,
    otherwise choose top card.
    
    Hint: Use the randint() function:
    from random import randint
    '''
    # random = random.shuffle(deck)
    if random == False:
        return deck[-1]
    else:
        return deck.pop(randint(0, len(deck)-1))
    

    
def abfrage():
    eingabe = input('Möchtest du die Karten mischen? ').strip()
    if eingabe == 'J':
        return True
    elif eingabe == 'N':
        return False
    else:
        print('Du darfst nur mit "J" oder "N" anworten')
        return abfrage()

mischen = abfrage()

    
    
print(draw(cards, mischen))

def follows(card, suit=None, rank=None):
    '''Check whether a card follows a given suit and rank.
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

def has_card(deck: list[tuple], suit=None, rank=None) -> bool:
    '''Check whether a deck has cards of a given suit and rank.
    '''
    pass