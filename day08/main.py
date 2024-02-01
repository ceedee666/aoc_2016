import re
from enum import Enum
from typing import Iterator

from commons import read_input_file

Operations = Enum("Operations", ["RECT", "ROTATE_ROW", "ROTATE_COL"])


def parse_operation(line: str) -> tuple:
    if "rect" in line:
        return (Operations.RECT, re.findall(r"(\d+)", line))
    else:
        if "row" in line:
            return (Operations.ROTATE_ROW, [int(v) for v in re.findall(r"(\d+)", line)])
        else:
            return (Operations.ROTATE_COL, [int(v) for v in re.findall(r"(\d+)", line)])


def parse_operations(lines: Iterator[str]) -> list[tuple]:
    return [parse_operation(line) for line in lines]


def transpose(matrix: list[list[str]]) -> list[list[str]]:
    return list(map(list, zip(*matrix)))


def execute_operrations(
    operations: list[tuple], row: int = 50, col: int = 6
) -> list[list[str]]:
    screen = [["." for _ in range(row)] for _ in range(col)]
    for op, args in operations:
        if op == Operations.RECT:
            width, height = args
            for c in range(int(width)):
                for r in range(int(height)):
                    screen[r][c] = "#"
        if op == Operations.ROTATE_ROW:
            row, by = args
            screen[row] = screen[row][-by:] + screen[row][:-by]
        if op == Operations.ROTATE_COL:
            col, by = args
            screen = transpose(screen)
            screen[col] = screen[col][-by:] + screen[col][:-by]
            screen = transpose(screen)

    return screen


def solve(
    lines: Iterator[str],
) -> list[list[str]]:
    operations = parse_operations(lines)
    return execute_operrations(operations)


if __name__ == "__main__":
    screen = solve(read_input_file("input.txt"))
    print(
        sum([sum([1 for c in row if c == "#"]) for row in screen]),
        "pixels are lit.",
    )

    print("The display shows the following code:")
    for row in screen:
        print("".join(row))
