import re
from collections import defaultdict
from math import prod
from typing import Iterator

from commons import read_input_file


def active_bots(values: dict[str, list[int]], processed: set[str]) -> list[str]:
    return [v for v in values if len(values[v]) == 2 and v not in processed]


def parse_input(
    lines: Iterator[str],
) -> tuple[dict[str, list[str]], dict[str, list[int]]]:
    bots = defaultdict(list)
    values = defaultdict(list)

    for line in lines:
        if "value" in line:
            value, bot = re.findall(r"\d+", line)
            values[bot].append(int(value))
        else:
            parts = line.split(" ")
            name = parts[1]

            if parts[5] == "output":
                low = parts[5] + parts[6]
            else:
                low = parts[6]

            if parts[10] == "output":
                high = parts[10] + parts[11]
            else:
                high = parts[11]

            bots[name].append(low)
            bots[name].append(high)
    return bots, values


def solve(lines: Iterator[str]) -> dict:
    bots, values = parse_input(lines)
    processed = set()

    while active := active_bots(values, processed):
        for bot in active:
            if "output" not in bot:
                processed.add(bot)

                vals = values[bot]
                low, high = bots[bot]
                values[low].append(min(vals))
                values[high].append(max(vals))

    return values


if __name__ == "__main__":
    values = solve(read_input_file("input.txt"))
    print(
        "The number of the bot comparing chips 61 and 17 is",
        [v for v in values if sorted(values[v]) == [17, 61]][0],
    )
    print(
        "The product of the outputs 0, 1 and 2 is",
        prod((values[f"output{i}"][0] for i in range(3))),
    )
