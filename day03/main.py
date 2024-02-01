from typing import Iterator

from commons import read_input_file


def is_possible(triangle: list[int]) -> bool:
    a, b, c = triangle
    return a + b > c and a + c > b and c + b > a


def solve_part_1(
    lines: Iterator[str],
) -> int:
    triangles = [list(map(int, line.split())) for line in lines]
    possible = [t for t in triangles if is_possible(t)]
    return len(possible)


def solve_part_2(
    lines: Iterator[str],
) -> int:
    input = [list(map(int, line.split())) for line in lines]
    values = [v[0] for v in input] + [v[1] for v in input] + [v[2] for v in input]
    triangles = [values[i : i + 3] for i in range(0, len(values), 3)]
    possible = [t for t in triangles if is_possible(t)]
    return len(possible)


if __name__ == "__main__":
    print(solve_part_1(read_input_file("input.txt")), "of the triangles are possible.")
    print(solve_part_2(read_input_file("input.txt")), "of the triangles are possible.")
