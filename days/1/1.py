def aoc_1_1():
    with open("days/1/input.txt", "r") as f:
        pairs = [nums.split() for nums in f.readlines()]

    list_a = [int(pair[0]) for pair in pairs]
    list_b = [int(pair[1]) for pair in pairs]

    [list.sort() for list in [list_a, list_b]]

    zipped = zip(list_a, list_b)

    return sum([abs(pair[0]-pair[1]) for pair in zipped])

def aoc_1_2():
    with open("days/1/input.txt", "r") as f:
        pairs = [nums.split() for nums in f.readlines()]

    list_a = [int(pair[0]) for pair in pairs]
    list_b = [int(pair[1]) for pair in pairs]

    sim_scores = [num * list_b.count(num) for num in list_a]

    return sum(sim_scores)

print(aoc_1_1())
print(aoc_1_2())
