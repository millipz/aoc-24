def aoc_5():
    with open("days/5/input.txt") as f:
        pairs_string, updates_string = f.read().split("\n\n")
    pairs = [pair.split("|") for pair in pairs_string.split("\n")]
    updates = [update.split(",") for update in updates_string.split("\n")]

    def sort_and_validate(update: list) -> dict:
        validator = {page: [a for a, b in pairs if b == page] for page in update}
        updated_pages = []
        while validator:
            for page, befores in validator.items():
                if all([value not in befores for value in validator.keys()]):
                    updated_pages.append(page)
                    validator.pop(page)
                    break
        return {"valid": updated_pages == update, "pages": updated_pages}

    updates = [sort_and_validate(u) for u in updates]

    return sum(
        int(u["pages"][len(u["pages"]) // 2]) for u in updates if not u["valid"]
    ), sum(int(u["pages"][len(u["pages"]) // 2]) for u in updates if u["valid"])


print(aoc_5())
