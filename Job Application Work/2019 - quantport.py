"""
Calculates the optimal moves in an adversarial card game in which two players take turns
taking cards off the left or right end of an array of cards with the player with the
most points winning at the end (each card has some point value)
Method:
We first note that this is a zero sum, symmetric game: the total point value of all cards
is fixed (since a card can only be picked by a single player, maximizing points for one
player is equivalent to minimizing them for the other) and players take alternating
turns (the logic that each player operates by is the same).
Thus, at any given point in the game, the player whose turn it is looks to minimize the
points the next player can obtain. Given an array of cards [0...n], this means picking
either the 0 or nth card such that the value the next player can obtain from [1...n]
or [0...n-1], respectively, is minimized. We know what value a player whose turn it is
can obtain from a given subarray by memoizing subarrays of size 1 up the full initial
array. We must also keep track of the card that is picked for every subarray (i.e.:
whether we picked 0, leaving subarray [1...n], or n, leaving subarray [0...n-1]; in fact
we only really need to record whether we picked the left or right side). This allows us
to calculate the obtainable value of the current array.
Say picking 0 minimizes the next player's obtainable value by leaving [1...n] (we would
thus record that we picked 0 for the [0...n] array). Then, knowing that for subarray
[1...n] the optimal move is to pick card n, we can calculate the obtainable value of
array [0...n] by adding the value of 0 to the obtainable value of [1...n-1].
"""


def max_sum_adversarial_cards(cards):
    subarray_value = {}
    side_picked = {}
    for i in xrange(len(cards)):
        key = (i, i)
        subarray_value[key] = cards[i]
    for i in xrange(len(cards) - 1):
        key = (i, i + 1)
        left_subarray_key = (i, i)
        right_subarray_key = (i + 1, i + 1)
        if subarray_value[left_subarray_key] < subarray_value[right_subarray_key]:
            subarray_value[key] = subarray_value[right_subarray_key]
            side_picked[key] = "r"
        else:
            subarray_value[key] = subarray_value[left_subarray_key]
            side_picked[key] = "l"

    for i in xrange(2, len(cards)):
        for j in xrange(0, len(cards) - i):
            key = (j, j + i)
            left_subarray_key = (j, j + i - 1)
            right_subarray_key = (j + 1, j + i)
            if subarray_value[left_subarray_key] < subarray_value[right_subarray_key]:
                left = j
                right = j + i - 1
                side_picked[key] = "r"
                value = cards[j + i]
            else:
                left = j + 1
                right = j + i
                side_picked[key] = "l"
                value = cards[j]
            if side_picked[(left, right)] == "r":
                subarray_value[key] = value + subarray_value[(left, right - 1)]
            else:
                subarray_value[key] = value + subarray_value[(left + 1, right)]

    return subarray_value, side_picked


arr = [5, 7, 1, 17, 12, 4]
values, sides = max_sum_adversarial_cards(arr)
for k in sorted(sides.keys()):
    print k, sides[k], values[k]
print values[(0, len(arr) - 1)]
