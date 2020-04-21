from conditional import Conditional
import constants

# What is the probability of no two faces being the same on three tosses of a die?

DIE_ELEM_EVENTS = constants.DIE_ELEM_EVENTS
TOSSES = 3


def calc_prob(elem_events, total_items):

    coin_conditional = Conditional(elem_events)
    arrangements = coin_conditional.arrange_items(total_items)

    # Two faces being the same
    same_2_faces = [arr for arr in arrangements if len(set(arr)) == 3]

    print(f"{len(same_2_faces)}/{len(arrangements)}")
    return len(same_2_faces) / len(arrangements)


def main():
    probability = calc_prob(DIE_ELEM_EVENTS, TOSSES)
    print(probability)


if __name__ == "__main__":
    main()
