COIN_ELEM_EVENTS = ['H', 'T']
DIE_ELEM_EVENTS = [1, 2, 3, 4, 5, 6]

CARD_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
CARD_DECK = {
    'heart': CARD_VALUES,
    'club': CARD_VALUES,
    'diamond': CARD_VALUES,
    'spade': CARD_VALUES
}
CARD_ELEM_EVENTS = [f"{card}_{suit}" for suit in CARD_DECK for card in CARD_DECK[suit]]