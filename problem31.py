'''
Problem 31 - Coin Sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general
circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

# coins = [200, 100, 50, 20, 10, 5, 2, 1]

from helpers.runtime import print_answer_and_elapsed_time

def combinations_of_coins(amount, coins):
    result = []
    if amount == 0:
        return result

    for coin in coins:
        amount_remaining = amount - coin
        if amount_remaining < 0:
            continue

        combinations_for_remaining = combinations_of_coins(amount_remaining, [c for c in coins if c <= coin])
        if len(combinations_for_remaining) == 0:
            result.append([coin])
            continue

        for combination in combinations_for_remaining:
            result.append([coin] + combination)
    return result

def answer():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    amount = 200
    return len(combinations_of_coins(amount, coins))

if __name__ == '__main__':
    print_answer_and_elapsed_time(answer)
