def aoc_3(switch=False) -> int:
    char_gen = (char for line in open("days/3/input.txt", "r") for char in line if char)
    START, DELIM, END, ON, OFF = "mul(", ",", ")", "do()", "don't()"
    a = ""
    buffer_size = max([len(var) for var in [START, a, DELIM, END, ON, OFF]])
    print('buffer_size: ', buffer_size)
    state = "searching"
    results = []

    buffer = [next(char_gen, None) for _ in range(buffer_size)]

    def match_pattern(buffer, pattern):
        return buffer[: len(pattern)] == list(pattern)
    
    def roll(buffer, gen, repeats=1):
        for _ in range(repeats):
            buffer.append(next(gen, None))
            char = buffer.pop(0)
        return char
    
    def get_num(buffer, gen):
        num = ""
        while buffer[0].isdigit():
            num += roll(buffer, gen, 1)
        return num, buffer[0]

    while any(buffer):
        print(state)
        print(buffer)
        match state:
            case "off":
                if match_pattern(buffer, list(ON)):
                    state = "searching"
                    roll(buffer, char_gen, len(ON))
                else:
                    roll(buffer, char_gen, 1)
            case "searching":
                if match_pattern(buffer, list(OFF)) and switch:
                    state = "off"
                    roll(buffer, char_gen, len(OFF))
                elif match_pattern(buffer, list(START)):
                    state = "num"
                    roll(buffer, char_gen, len(START))
                else:
                    roll(buffer, char_gen, 1)
            case "num":
                num, char = get_num(buffer,char_gen)
                if not a and char == DELIM:
                    a = num
                    roll(buffer, char_gen, 1)
                elif a and char == END:
                    results.append((int(a), int(num)))
                    a, state = "", "searching"
                    roll(buffer, char_gen, 1)
                else:
                    state = "searching"
                    a = ""

    return sum([a * b for a, b in results])


print(aoc_3())
print(aoc_3(True))
