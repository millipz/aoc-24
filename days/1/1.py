def aoc_1() -> tuple[int]:
    with open("days/1/input.txt", "r") as f:
        pairs = [nums.split() for nums in f.readlines()]

    list_a = [int(pair[0]) for pair in pairs]
    list_b = [int(pair[1]) for pair in pairs]

    zipped = zip(sorted(list_a), sorted(list_b))

    diff_total = sum([abs(pair[0] - pair[1]) for pair in zipped])
    total_sim_score = sum([num * list_b.count(num) for num in list_a])

    return diff_total, total_sim_score

print(aoc_1())
