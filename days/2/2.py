def aoc_2_1(dampers = 0):

    def is_safe(report: list, lives: int = dampers) -> bool:
        direction = 1 if report[0] < report[1] else -1
        for i in range(1, len(report)):
            diff = report[i]-report[i-1]
            if abs(diff) not in range(1,4) or diff*direction < 0:
                lives -= 1
        return lives >= 0

    with open("days/2/input.txt", "r") as f:
        reports = [[int(num) for num in nums.split()] for nums in f.readlines()]

    return sum([is_safe(report) for report in reports])

print(aoc_2_1())
print(aoc_2_1(1))