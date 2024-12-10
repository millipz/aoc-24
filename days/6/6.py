def aoc_6_grid() -> dict:
    return {
        (row, col): char
        for row, line in enumerate(open("days/6/input.txt"))
        for col, char in enumerate(line.strip())
    }


def aoc_6():
    grid = aoc_6_grid()
    obstacles = set()
    for loc, char in grid.items():
        match char:
            case "^":
                start = loc
            case "#":
                obstacles.add(loc)

    dir_change = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }

    def is_loop(obstacle_loc):
        # print(f"testing - {obstacle_loc}")
        positions = set()
        guard = {"loc": start, "dir": (-1, 0)}
        while guard:
            positions.add((guard["loc"], guard["dir"]))
            next = tuple(map(sum, zip(guard["loc"], guard["dir"])))
            if next not in grid.keys():
                # print("off the map!")
                # print({"loop": False, "visited": set([loc for loc, _ in positions])})
                return {
                    "loop": False,
                    "visited": len(set([loc for loc, _ in positions])),
                }
            elif (next, guard["dir"]) in positions:
                return {
                    "loop": True,
                    "visited": len(set([loc for loc, _ in positions])),
                }
            elif next in obstacles or next == obstacle_loc:
                guard["dir"] = dir_change[guard["dir"]]
            else:
                guard["loc"] = next

    return (
        sum([1 for loc in grid.keys() if is_loop(loc)["loop"]]),
        is_loop(None)["visited"],
    )


print(aoc_6())
