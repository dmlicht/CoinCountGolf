def recurse(amounts, money_left, mem={}):
    #memoize
    if mem.get((amounts, money_left), False):
        return mem[(amounts, money_left)]

    #base case
    if len(amounts) == 1:
        if money_left % amounts[0] == 0:
            return 1
        return 0

    #recurse loop
    coin = amounts[0]
    others = amounts[1:]
    return sum([recurse(others, money_left - coin*i) for i in xrange(money_left/coin)])

def count_combinations(amounts, money_left):
    """returns number of ways you use multiples of given amounts to sum to money_left
    this function runs recursively using the mem dict to store previously seen cases"""
    amounts = tuple(sorted(amounts))[::-1]
    return recurse(amounts, money_left)
