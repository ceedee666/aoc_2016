from commons import read_input_file

KEYPAD = {
    complex(0, 0): 7,
    complex(1, 0): 8,
    complex(2, 0): 9,
    complex(0, 1): 4,
    complex(1, 1): 5,
    complex(2, 1): 6,
    complex(0, 2): 1,
    complex(1, 2): 2,
    complex(2, 2): 3,
}

KEYPAD2 = {
    complex(2, 2): "1",
    complex(1, 1): "2",
    complex(2, 1): "3",
    complex(3, 1): "4",
    complex(0, 0): "5",
    complex(1, 0): "6",
    complex(2, 0): "7",
    complex(3, 0): "8",
    complex(4, 0): "9",
    complex(1, -1): "A",
    complex(2, -1): "B",
    complex(3, -1): "C",
    complex(2, -2): "D",
}
DIRS = {"U": 1j, "D": -1j, "L": -1, "R": 1}


def solve(
    lines: list[str],
    start: complex = complex(1, 1),
    part2: bool = False,
) -> str:
    code = []
    pos = start
    current_keypad = KEYPAD2 if part2 else KEYPAD
    for line in lines:
        for c in line:
            next = pos + DIRS[c]
            if next in current_keypad:
                pos = next
        code.append(current_keypad[pos])
    return "".join((str(c) for c in code))


if __name__ == "__main__":
    print("The code is: ", solve(read_input_file("input.txt")))
    print("The code is: ", solve(read_input_file("input.txt"), complex(0, 0), True))
