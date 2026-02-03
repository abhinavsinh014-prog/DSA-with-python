def minAddedCoins(coins, target):
    coins.sort()
    maxReach = 0
    added = 0
    i = 0

    while maxReach < target:
        if i < len(coins) and coins[i] <= maxReach + 1:
            maxReach += coins[i]
            i += 1
        else:
            # add a new coin
            added += 1
            maxReach += maxReach + 1

    return added

coins = [1,4,10]
target = 19