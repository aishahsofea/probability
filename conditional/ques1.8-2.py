from conditional import Conditional
import constants

# 1.8–2: Given that the sum of the two faces of a pair of dice is greater
# than 10, what is the probability that the sum is 12?

DIE_ELEM_EVENTS = constants.DIE_ELEM_EVENTS
TOTAL_DICE = 2


def calc_prob(elem_events, total_items):

    die_conditional = Conditional(elem_events)
    arrangements = die_conditional.arrange_items(total_items)
    
    # Sum greater than 10
    more_than_10 = [arr for arr in arrangements if sum([int(i) for i in arr]) > 10]

    # Sum is 12
    sum_12 = [arr for arr in more_than_10 if sum([int(i) for i in arr]) == 12]

    print(f"{len(sum_12)}/{len(more_than_10)}")
    return len(sum_12) / len(more_than_10)


def main():
    probability = calc_prob(DIE_ELEM_EVENTS, TOTAL_DICE)
    print(probability)


if __name__ == "__main__":
    main()
