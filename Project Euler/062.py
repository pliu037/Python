# https://projecteuler.net/problem=62


def find_num_cube_permuations(n):
    """
    Returns the smallest integer such that n of its permutations (including itself) are cubes
    """
    perm_dict = {}
    i = 345
    while True:
        check = i**3
        check_tuple = tuple(sorted(str(check)))
        if check_tuple not in perm_dict:
            perm_dict[check_tuple] = []
        perm_dict[check_tuple].append(check)
        if len(perm_dict[check_tuple]) == n:
            return perm_dict[check_tuple][0]
        i += 1


print find_num_cube_permuations(5)
