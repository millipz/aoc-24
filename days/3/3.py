def aoc_3(switch=False) -> int:
    global buffer, char_gen
    char_gen = (char for line in open("days/3/input.txt", "r") for char in line if char)
    START, DELIM, END, ON, OFF = "mul(", ",", ")", "do()", "don't()"
    state, results, a = "searching", [], ""
    buffer_size = max(map(len, [START, DELIM, END, ON, OFF]))
    buffer = [next(char_gen, None) for _ in range(buffer_size)]

    def match(pattern):
        return buffer[: len(pattern)] == list(pattern)

    def roll(n=1) -> str:
        for _ in range(n):
            buffer.append(next(char_gen, None))
            char = buffer.pop(0)
        return char

    def get_num():
        num = ""
        while buffer[0].isdigit():
            num += roll()
        return num, buffer[0]

    while any(buffer):
        match state:
            case "off":
                state, _ = (
                    ("searching", roll(len(ON))) if match(list(ON)) else ("off", roll())
                )
            case "searching":
                if match(list(OFF)) and switch:
                    state, _ = "off", roll(len(OFF))
                elif match(list(START)):
                    state, _ = "num", roll(len(START))
                else:
                    roll()
            case "num":
                num, char = get_num()
                if not a and char == DELIM:
                    a, _ = num, roll()
                elif a and char == END:
                    results.append(int(a) * int(num))
                    a, state, _ = "", "searching", roll()
                else:
                    a, state = "", "searching"

    return sum(results)


print(aoc_3())
print(aoc_3(True))
