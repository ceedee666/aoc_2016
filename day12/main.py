from collections import defaultdict
from enum import Enum
from typing import Iterator

from commons import read_input_file

Operations = Enum("Operations", ["COPY", "INC", "DEC", "JUMP_NOT_ZERO"])

OPERATION_MAP = {
    "cpy": Operations.COPY,
    "inc": Operations.INC,
    "dec": Operations.DEC,
    "jnz": Operations.JUMP_NOT_ZERO,
}


def parse_line(line: str) -> tuple[Operations, list[str]]:
    op, *values = line.split(" ")
    return OPERATION_MAP[op], values


def parse_input(lines: Iterator[str]) -> list[tuple[Operations, list[str]]]:
    return [parse_line(line) for line in lines]


def execute_program(program: list[tuple[Operations, list[str]]], part2: bool) -> dict:
    registers = defaultdict(int)
    if part2:
        registers["c"] = 1

    instr_ptr = 0
    while instr_ptr < len(program):
        op, values = program[instr_ptr]
        match op:
            case Operations.COPY:
                if values[0].isdigit():
                    registers[values[1]] = int(values[0])
                else:
                    registers[values[1]] = registers[values[0]]
                instr_ptr += 1
            case Operations.INC:
                registers[values[0]] += 1
                instr_ptr += 1
            case Operations.DEC:
                registers[values[0]] -= 1
                instr_ptr += 1
            case Operations.JUMP_NOT_ZERO:
                if registers[values[0]] != 0 or (
                    values[0].isdigit() and int(values[0]) != 0
                ):
                    instr_ptr += int(values[1])
                else:
                    instr_ptr += 1
    return registers


def solve(lines: Iterator[str], part2: bool = False) -> dict:
    program = parse_input(lines)
    return execute_program(program, part2)


if __name__ == "__main__":
    print(
        "The value in register a after executing the program is",
        solve(read_input_file("input.txt"))["a"],
    )
    print(
        "The value in register a after executing the program is",
        solve(read_input_file("input.txt"), True)["a"],
    )
