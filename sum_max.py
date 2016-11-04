def find_max_min(n):
    min_max = []
    identity = []
    sorted_list = sorted(n)
    min_max.append(sorted_list[0])
    min_max.append(sorted_list[int(len(n)-1)])
    a = min_max[0]
    b = min_max[1]
    if a == b:
        identity.append(len(n))
        return identity
    elif a != b:
        return min_max

    