from conditional import Conditional

# What is the probability of at least two heads in the toss of 10 coins,
# given that we know that there is at least one head.

COIN_ELEM_EVENTS = ['H', 'T']
TOTAL_COINS = 10


def calc_prob(elem_events, total_items):

    coin_conditional = Conditional(elem_events)

    # Possible permutations of H/T in the toss of 10 coins
    arrangements = coin_conditional.arrange_items(total_items)

    # Excludes the case of all tails (given that we know that there is at least one head)
    no_all_tails = [arr for arr in arrangements if not all([i == 'T' for i in arr])]

    # Excludes the case where there is a single head
    no_one_heads = [arr for arr in no_all_tails if list(arr).count('H') != 1]

    print(f"{len(no_one_heads)}/{len(no_all_tails)}")
    return len(no_one_heads) / len(no_all_tails)


def main():
    probability = calc_prob(COIN_ELEM_EVENTS, TOTAL_COINS)
    print(probability)


if __name__ == "__main__":
    main()
