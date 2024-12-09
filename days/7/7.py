def aoc_7():
    equations = {}
    with open("days/7/input.txt") as f:
        for line in f.readlines():
             res, input = line.split(":")
             equations[int(res)] = [int(x) for x in input.split()]
    def bin_perms(n):
        for i in range(2**n):
            s = bin(i)[2:]
            s = "0" * (n-len(s)) + s
            yield s

    print list(perms(5)) 

print(aoc_7())
