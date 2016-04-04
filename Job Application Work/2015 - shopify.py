import json
import urllib2

'''
Gets the JSON from the shopicruit URL and returns the value corresponding to the 'products' key
Could remove hard-coded url and have url passed in as a parameter; this would require sanitizing
the input, however, to ensure both that the url is valid and that the data retrieved from is
parsable to JSON
'''
def getProducts():
    return json.loads(urllib2.urlopen("http://shopicruit.myshopify.com/products.json").read())['products']


# Given a list of products, returns a list of dictionaries containing product title, variant id,
# variant weight, and variant price
def flattenVariants(products):
    flattenedVariants = []
    for product in products:
        for variant in product['variants']:
            flattenedVariant = {}
            flattenedVariant['title'] = product['title']
            flattenedVariant['id'] = variant['id']
            flattenedVariant['weight'] = variant['grams']
            flattenedVariant['price'] = variant['price']
            flattenedVariants.append(flattenedVariant)
    return flattenedVariants


'''
Given a list of objects, a knapsack capacity, and functions that return the size and value of a
given object, uses a greedy heuristic (value/size) to determine which objects should be packed to
maximize the total value while remaining within the capacity
Returns both the list of the objects that are to be packed into the knapsack and the list of objects
that are left out (objects whose size is larger than the capacity are not included in either list)
'''
def greedyKnapsack(objects, capacity, size_func, value_func):

    # Objects that are larger than the capacity are removed
    objects = [item for item in objects if size_func(item) <= capacity]

    # Saves the largest object
    maxSizeObject = max(objects, key=size_func)

    # Sorts the objects in descending order of the greedy heuristic
    objects = sorted(objects, key=lambda x: float(value_func(x))/size_func(x), reverse=True)

    included = []
    notIncluded = []
    used = 0
    totalValue = 0

    # Adds objects to the knapsack, so long as they fit, in descending order of the greedy heuristic
    # Can be thought of as maximizing the value density of any occupied space within the knapsack
    for item in objects:
        if size_func(item) + used <= capacity:
            included.append(item)
            used += size_func(item)
            totalValue += value_func(item)
        else:
            notIncluded.append(item)

    '''
    If the value of the largest object is greater than the total value of added objects, return the
    largest object and its compliment
    This step tightens the bounds around the optimality of the solution
    '''
    if value_func(maxSizeObject) > totalValue:
        return [maxSizeObject], objects.remove(maxSizeObject)

    return included, notIncluded


'''
Given lists of included and not included objects, as determined using the greedy knapsack algorithm,
a knapsack capacity, and functions that return the size and value of a given object, approximates
the minimum total value of <included> while maintaining its cardinality
The approach used is similar to that of the greedy knapsack problem with the remaining capacity as
the knapsack capacity, pairs of swappable objects as the objects to be packed, the difference in
value between the pair of objects to be swapped as the value function, the difference in size
between the pair of objects to be swapped as the size function, and a heuristic representing the
density (dValue/dSize = [value-in - value-out]/[size-in - size-out])
Returns an approximation of the lowest value set
Still need to perform the analysis to bound the optimality of the solution and the running time
'''
def minimizeValue(included, notIncluded, capacity, size_func, value_func):
    remainingCapacity = capacity - sum([size_func(x) for x in included])
    maxIncludedSize = size_func(max(included, key=size_func))

    # Generates a list of objects that could be swapped with at least one object in the current
    # <included> list while remaining within capacity (reduces the running time of the next step)
    inConsideration = [item for item in notIncluded if size_func(item) - maxIncludedSize <= remainingCapacity]

    # Generates pairs of objects, one from <included> and one from <inConsideration>, that could be
    # swapped to reduce the total value while remaining within capacity
    options = [(x, y) for x in included for y in inConsideration if size_func(y) - size_func(x) <= remainingCapacity and
               value_func(y) < value_func(x)]

    baseIncluded = []
    valueDiff = 0

    while options:

        # Of the valid swaps, finds the minimum using the dValue/dSize heuristic, breaking ties
        # using dValue
        minSwap = min(options, key=lambda x: (float("-inf"), value_func(x[1]) - value_func(x[0])) if size_func(x[1]) - size_func(x[0]) == 0 else
                  ((value_func(x[1]) - value_func(x[0]))/(size_func(x[1]) - size_func(x[0])), value_func(x[1]) - value_func(x[0])))

        # The decrease in value from all swaps that alter the remaining capacity are tallied
        if size_func(minSwap[1]) - size_func(minSwap[0]) != 0:
            valueDiff += value_func(minSwap[1]) - value_func(minSwap[0])

            # Snapshots the state of <included> and the swap with the largest value decrease after
            # all swaps that do not alter the remaining capacity have been made
            if not baseIncluded:
                largestDecreaseSwap = min(options, key=lambda x: value_func(x[1]) - value_func(x[0]))
                baseIncluded = [item for item in included]

        # Swaps the given pair of objects as determined using the dValue/dSize heuristic
        included.append(minSwap[1])
        inConsideration.append(minSwap[0])
        included.remove(minSwap[0])
        inConsideration.remove(minSwap[1])

        # Recomputes new valid swaps given the modified <included> and <inConsideration> lists
        remainingCapacity = capacity - sum([size_func(x) for x in included])
        maxIncludedSize = size_func(max(included, key=size_func))
        inConsideration = [object for object in inConsideration if size_func(object) - maxIncludedSize <= remainingCapacity]
        options = [(x, y) for x in included for y in inConsideration if size_func(y) - size_func(x) <= remainingCapacity and
                   value_func(y) < value_func(x)]

    # If the swap with the largest decrease decreases the value more than the total value decreased
    # by the individual swaps, return the snapshotted <included> with that swap applied instead
    if baseIncluded and valueDiff > value_func(largestDecreaseSwap[1]) - value_func(largestDecreaseSwap[0]):
        included = baseIncluded
        included.append(largestDecreaseSwap[1])

    return included


# Given a list of flattened variants, prints them and calculates and prints the number of variants,
# the total price, and the total weight
def printFlattenedVariants(list):
    print 'Included:'
    for flattenedVariant in list:
        print flattenedVariant
    print '# of Variants: ' + str(len(list))
    print 'Total Price: ' + str(sum([float(item['price']) for item in list]))
    print 'Total Weight: ' + str(sum([item['weight'] for item in list]))


'''
Retrieves the list of shopicruit products and returns an approximation of the lowest price to buy
the maximum number of unique variants of the given product types such the total weight of purchased
variants is less than or equal to the capacity
'''
def findMinCostOfMaxTypes(capacity, productTypes):
    products = getProducts()
    productTypes = set(productTypes)  # Solely to speed up lookup in the next step

    # Products whose type is not one of the desired product types are removed
    validProducts = [product for product in products if product['product_type'] in productTypes]

    flattenedVariants = flattenVariants(validProducts)

    '''
    DISCLAIMER:
    The following two sections, greedyKnapsack and minimizeValue, are not necessary in this
    particular instance as the total weight of all variants of the given product types fits within
    the capacity given; however, I wanted to also find a general solution that would work in the
    case where the total weight exceeded the capacity and we wished to minimize the price while
    still maximizing the number of unique variants that could fit within the capacity
    I believe the general problem is NP-Hard
    getProducts, filtering for valid products and flattenVariants run in O(n) time and
    greedyKnapsack runs in O(n log n) where n is the number of variants
    '''

    '''
    Uses the greedy knapsack algorithm to pack objects into a knapsack with <capacity> capacity; an
    object's size is given by its weight and every object has a value of 1; this step maximizes the
    number of items that can fit within the capacity
    '''
    included, notIncluded = greedyKnapsack(flattenedVariants, capacity, lambda x: x['weight'], lambda x: 1)

    print 'Greedy knapsack'
    printFlattenedVariants(included)

    '''
    Approximates the set of objects with the lowest total price from amongst the potentially
    multiple sets (it is possible that there are multiple sets with the same cardinality, as
    determined in the previous step, and that fit within the given capacity)
    '''
    included = minimizeValue(included, notIncluded, capacity, lambda x: x['weight'], lambda x: float(x['price']))

    print 'Minimized'
    printFlattenedVariants(included)


# Capacity is 100 kg, but variant weight is given in grams
findMinCostOfMaxTypes(100000, ['Keyboard', 'Computer'])

test = [(2, 0), (2, 1), (2, 1)]
test2 = [(1, 0), (0, 1), (1, 0)]
print minimizeValue(test, test2, 2, lambda x: x[1], lambda x: x[0])
