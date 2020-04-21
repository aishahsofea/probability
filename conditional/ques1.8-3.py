from conditional import Conditional
import constants

# In drawing two cards from a deck (without returning the first card) what
# is the probability of two aces when you get at least one ace?

CARD_ELEM_EVENTS = constants.CARD_ELEM_EVENTS
DRAWS = 2


def calc_prob(elem_events, total_items):

    card_conditional = Conditional(elem_events, False)
    arrangements = card_conditional.arrange_items(total_items)

    # At least one ace
    atleast_1A = {
        tuple(arr) for arr in arrangements if [
            card[0] for card in arr].count('A') >= 1}

    # Exactly two aces
    exatly_2A = {tuple(arr) for arr in arrangements if [card[0] for card in arr].count('A') == 2}

    print(f"{len(exatly_2A)}/{len(atleast_1A)}")
    return len(exatly_2A) / len(atleast_1A)


def main():
    probability = calc_prob(CARD_ELEM_EVENTS, DRAWS)
    print(probability)


if __name__ == "__main__":
    main()
