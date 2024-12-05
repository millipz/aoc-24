def aoc_4_grid() -> dict:
    return {
        (row, col): char
        for row, line in enumerate(open("days/4/input.txt"))
        for col, char in enumerate(line.strip())
    }


def aoc_4_search(word, grid):
    directions = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy]
    return sum(
        True
        for x, y in grid.keys()
        for dx, dy in directions
        if all(
            grid.get((x + dx * i, y + dy * i), "") == char
            for i, char in enumerate(word)
        )
    )


def aoc_4_cross(word, grid):
    l, words = len(word), word, word[::-1]
    height = max(row for row, _ in grid) - l + 2
    width = max(col for _, col in grid) - l + 2
    candidates = [
        (
            "".join([grid[x + i, y + i] for i in range(l)]),
            "".join([grid[x + l - i - 1, y + i] for i in range(l)]),
        )
        for x in range(width)
        for y in range(height)
    ]
    return sum(1 for c in candidates if (c[0] in words) and (c[1] in words))


grid = aoc_4_grid()
print(aoc_4_search("XMAS", grid))
print(aoc_4_cross("MAS", grid))
