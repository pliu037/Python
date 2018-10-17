# https://projecteuler.net/problem=61


class Chain:
    def __init__(self, chain):
        self.chain = chain

    def first_two_digits(self):
        return self.chain[0] / 100

    def last_two_digits(self):
        return self.chain[-1] % 100


def _add_to_components_dict(components_dict, values):
    keys = [2**i for i in xrange(len(values))]
    for index, value in enumerate(values):
        if 1000 <= value < 10000 and value % 100 >= 10:
            if keys[index] not in components_dict:
                components_dict[keys[index]] = {'starting': {}, 'ending': {}}
            starting_dict = components_dict[keys[index]]['starting']
            ending_dict = components_dict[keys[index]]['ending']
            chain = Chain([value])
            if chain.first_two_digits() not in starting_dict:
                starting_dict[chain.first_two_digits()] = []
            starting_dict[chain.first_two_digits()].append(chain)
            if chain.last_two_digits() not in ending_dict:
                ending_dict[chain.last_two_digits()] = []
            ending_dict[chain.last_two_digits()].append(chain)


def merge_components_dicts(head_components_dict, tail_components_dict):
    """
    Given two dictionaries of the form defined in get_initial_components_dict, merges them to form a new
    dictionary of the same form but whose chains are the concatenation of chains from the two initial
    dictionaries (1 chain from each)
    """
    merged_components_dict = {}
    for head_components in head_components_dict:
        for tail_components in tail_components_dict:
            if not head_components & tail_components:
                head_last_two_buckets = head_components_dict[head_components]['ending']
                for head_last_two_digits in head_last_two_buckets:
                    if head_last_two_digits not in tail_components_dict[tail_components]['starting']:
                        continue
                    head_chains = head_last_two_buckets[head_last_two_digits]
                    tail_chains = tail_components_dict[tail_components]['starting'][head_last_two_digits]
                    for head_chain in head_chains:
                        for tail_chain in tail_chains:
                            merged_component = head_components | tail_components
                            if merged_component not in merged_components_dict:
                                merged_components_dict[merged_component] = {'starting': {}, 'ending': {}}
                            starting_dict = merged_components_dict[merged_component]['starting']
                            ending_dict = merged_components_dict[merged_component]['ending']
                            chain = Chain(head_chain.chain + tail_chain.chain)
                            if chain.first_two_digits() not in starting_dict:
                                starting_dict[chain.first_two_digits()] = []
                            starting_dict[chain.first_two_digits()].append(chain)
                            if chain.last_two_digits() not in ending_dict:
                                ending_dict[chain.last_two_digits()] = []
                            ending_dict[chain.last_two_digits()].append(chain)
    return merged_components_dict


def get_initial_components_dict():
    """
    Generates the initial dictionary of 1-length chains with the form (see _add_to_components_dict):
    <components>:
        "starting":
            <first two digits>: [list of chains]
        "ending":
            <last two digits>: [list of chains]
    where the <components> key is a bit array indicating the series present in a chain, the <first two digits>
    and <last two digit> keys are the first and last two digits of a chain, respectively, and a chain is a
    chain of integers such that there is at most one integer from each series and the last two digits of one
    integer are the first two digits of the next
    """
    # 19 is the point below which the largest function, octagonal, yields 3-digit numbers
    i = 19
    components_dict = {}

    # 141 is the point above which the smallest function, triangular, yields 5-digit numbers
    while i < 142:
        values = [i * (i + 1) / 2,
                  i * i,
                  i * (3 * i - 1) / 2,
                  i * (2 * i - 1),
                  i * (5 * i - 3) / 2,
                  i * (3 * i - 2)]
        _add_to_components_dict(components_dict, values)
        i += 1
    return components_dict


def cyclical_figurate():
    """
    Returns the sum of the chain of six 4-digit integers such that there is an integer from each of the six
    series defined in get_initial_length_dict and the last two digits of one integer are the first two digits
    of the next (with the last integer wrapping around to the first)
    """
    length_dict = {1: get_initial_components_dict()}
    length_dict[2] = merge_components_dicts(length_dict[1], length_dict[1])
    length_dict[3] = merge_components_dicts(length_dict[2], length_dict[1])
    length_dict[6] = merge_components_dicts(length_dict[3], length_dict[3])
    final_dict = length_dict[6][63]
    for first_two_digits in final_dict['starting']:
        chains = final_dict['starting'][first_two_digits]
        for chain in chains:
            if chain.last_two_digits() == first_two_digits:
                return sum(chain.chain)


print cyclical_figurate()
