def find_number_of_repeats(substr, s):
    if s == '':
        return 0
    for i in xrange(len(substr) - 1):
        if s.startswith(substr[i:]):
            count = 1
            remaining_s = s[i + 1:]
            while len(remaining_s) >= len(substr):
                print remaining_s
                if remaining_s.startswith(substr):
                    count += 1
                    remaining_s = remaining_s[len(substr):]
                else:
                    break
            if substr.startswith(remaining_s):
                count += 1
                return count
    return -1
