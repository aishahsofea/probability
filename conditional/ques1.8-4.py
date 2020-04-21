from conditional import Conditional
import constants

# What is the probability of different faces turning up on two tosses of a die?

DIE_ELEM_EVENTS = constants.DIE_ELEM_EVENTS
TOSSES = 2


def calc_prob(elem_events, total_items):

    coin_conditional = Conditional(elem_events)
    arrangements = coin_conditional.arrange_items(total_items)

    # Different faces turning up
    diff_faces = [arr for arr in arrangements if len(set(arr)) != 1]

    print(f"{len(diff_faces)}/{len(arrangements)}")
    return len(diff_faces) / len(arrangements)


def main():
    probability = calc_prob(DIE_ELEM_EVENTS, TOSSES)
    print(probability)


if __name__ == "__main__":
    main()
