from conditional import Conditional

# 1.8–1: If a fair coin is tossed 10 times what is the probabilty that the
# first five are the same side?

COIN_ELEM_EVENTS = ['H', 'T']
TOTAL_TOSSES = 10


def calc_prob(elem_events, total_items):

    coin_conditional = Conditional(elem_events)
    arrangements = coin_conditional.arrange_items(total_items)

    # First 5 the same sides
    same_sides = [arr for arr in arrangements if len(set(arr[:5])) == 1]

    print(f"{len(same_sides)}/{len(arrangements)}")
    return len(same_sides) / len(arrangements)


def main():
    probability = calc_prob(COIN_ELEM_EVENTS, TOTAL_TOSSES)
    print(probability)


if __name__ == "__main__":
    main()
