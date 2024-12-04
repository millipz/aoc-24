def aoc_4() -> int:
    WORD = "XMAS"
    grid = {
        (row, col): char
        for row, line in enumerate(open("days/4/input.txt"))
        for col, char in enumerate(line.strip())
    }
    locs = set(grid.keys())
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    live_candidates = [
        (loc, dir)
        for loc, char in grid.items()
        for dir in directions
        if char == WORD[0]
    ]
    print(live_candidates)
    remaining = [(i, char) for i, char in enumerate(WORD[1:], 1)]
    print(f"remaining -> {remaining}")
    # for c in live_candidates:
    #     print("-----------------")
    #     print(f"candidate -> {c}")
    #     for i, char in remaining:
    #         print(f"(i, char) -> {i, char}")
    #         loc, dir = c
    #         x, y = loc
    #         print(f"x = {x} y = {y}")
    #         dx, dy = dir
    #         print(f"dx = {dx} dy = {dy}")
    #         check_loc =  x + dx * i, y + dy * i
    #         print(f"check_loc -> {check_loc}")
    #         if check_loc not in locs or grid[check_loc] != char:
    #             print(f"removing{c}")
    #             live_candidates.remove(c)
    #             break

    xmases = [
        c for c in live_candidates
        if all(
            grid.get((c[0][0] + c[1][0] * i, c[0][1] + c[1][1] * i), '') == char
            for i, char in enumerate(WORD)
        )
    ]

    print(len(live_candidates))
    print(live_candidates)
    return len(live_candidates)

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
