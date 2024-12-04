def aoc_4() -> int:
    WORD = "XMAS"
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    grid = {
        (row, col): char
        for row, line in enumerate(open("days/4/input.txt"))
        for col, char in enumerate(line.strip())
    }
    xmases = [
        1
        for x, y in grid.keys()
        for dx, dy in directions
        if all(
            grid.get((x + dx * i, y + dy * i), "") == char
            for i, char in enumerate(WORD)
        )
    ]

    return len(xmases)


print(aoc_4())
