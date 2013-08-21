def count_combinations(amts, money_left, mem={}):
    amts = tuple(sorted(amts))[::-1] #sort to allow us to use amts as key for memoization
    if len(amts) == 1: #base case
        return 1 if money_left % amts[0] == 0 else 0 #if we can divy up change using last coin return 1
    mem[(amts, money_left)] = mem.get((amts, money_left), False) or sum([count_combinations(amts[1:], money_left - amts[0]*i) for i in xrange(money_left/amts[0])]) #MEAT
    return mem[(amts, money_left)] #return newly stored memoization value
