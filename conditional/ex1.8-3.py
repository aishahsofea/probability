from conditional import Conditional

# What is the probability of exactly three heads knowing that there are at
# least two heads in the toss of 4 coins?

COIN_ELEM_EVENTS = ['H', 'T']
TOTAL_COINS = 4


def calc_prob(elem_events, total_items):

    coin_conditional = Conditional(elem_events)
    arrangements = coin_conditional.arrange_items(total_items)

    # Excludes the case of all tails (given that we know that there is at
    # least one head)
    no_all_tails = [arr for arr in arrangements if not all(
        [i == 'T' for i in arr])]

    # At least 2 heads
    atleast_2H = [arr for arr in no_all_tails if list(arr).count('H') >= 2]

    # Exactly 3 heads
    exactly_3H = [arr for arr in atleast_2H if list(arr).count('H') == 3]

    print(f"{len(exactly_3H)}/{len(atleast_2H)}")
    return len(exactly_3H) / len(atleast_2H)


def main():
    probability = calc_prob(COIN_ELEM_EVENTS, TOTAL_COINS)
    print(probability)


if __name__ == "__main__":
    main()
