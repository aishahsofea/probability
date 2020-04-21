from conditional import Conditional

# On the roll of two independent dice, if at least one face is known to be
# an even number, what is the probability of a total of 8?

DIE_ELEM_EVENTS = [1, 2, 3, 4, 5, 6]
TOTAL_DICE = 2


def is_odd(num):
    return int(num) % 2 == 1


def calc_prob(elem_events, total_items):
    die_conditional = Conditional(elem_events)
    die_init_arrangements = die_conditional.arrange_items(total_items)

    # Excludes the case where both dice are odd
    arrangements = [arr for arr in die_init_arrangements if not (is_odd(arr[0]) and is_odd(arr[1]))]

    # Cases where total of 2 dice is 8
    total_8 = [arr for arr in arrangements if int(arr[0]) + int(arr[1]) == 8]

    print(f"{len(total_8)}/{len(arrangements)}")
    return len(total_8) / len(arrangements)


def main():
    probability = calc_prob(DIE_ELEM_EVENTS, TOTAL_DICE)
    print(probability)


if __name__ == "__main__":
    main()
