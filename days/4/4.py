def aoc_4() -> int:
    WORD = "XMAS"
    grid = {
        (row, col): char
        for row, line in enumerate(open("days/4/input.txt"))
        for col, char in enumerate(line.strip())
    }

    print(grid)
    print(WORD[0])

    live_candidates = [loc for loc, char in grid.items() if char == WORD[0]]
    print(live_candidates)
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for c in live_candidates:
        for x, y in directions:
            for i, char in enumerate(WORD[1:], 1):
                pass



        # try:
        #     live_candidates.extend(
        #         (c[0] + dy * i, c[1] + dx * i)
        #         for dy, dx in directions
        #         if grid[c[0] + dy * i, c[1] + dx * i] == char
        #     )
        # except KeyError:
        #     continue
    # candidates = live_candidates
    # print(candidates)
    # print(len(candidates))


print(aoc_4())
