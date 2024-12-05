def aoc_4(word, cross=False) -> int:
    grid = {
        (row, col): char
        for row, line in enumerate(open("days/4/input.txt"))
        for col, char in enumerate(line.strip())
    }
    if not cross:
        directions = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 1),
            (1, 1),
            (1, -1),
            (-1, -1),
        ]
        print(directions)
        return sum(
            True
            for x, y in grid.keys()
            for dx, dy in directions
            if all(
                grid.get((x + dx * i, y + dy * i), "") == char
                for i, char in enumerate(word)
            )
        )
    else:
        l = len(word)
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
        return len(
            c
            for c in candidates
            if (c[0] == word or c[0][::-1] == word)
            and (c[1] == word or c[1][::-1] == word)
        )

print(aoc_4("XMAS"))
print(aoc_4("MAS", True))
