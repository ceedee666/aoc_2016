from commons import read_input_file


def manhatten_distance(pos: complex, start: complex = complex(0, 0)) -> int:
    return int(abs(start.real - pos.real)) + int(abs(start.imag - pos.imag))


def solve(
    lines: list[str],
    start: complex = complex(0, 0),
    dir: complex = complex(0, 1),
    part2: bool = False,
) -> int:
    visited = set()
    pos = start
    visited.add(pos)

    moves = [(instr[0], int(instr[1:])) for instr in lines[0].split(", ")]
    for turn, dist in moves:
        match turn:
            case "R":
                dir *= -1j
            case "L":
                dir *= 1j

        if part2:
            for _ in range(dist):
                pos += dir
                if pos in visited:
                    return manhatten_distance(pos)
                else:
                    visited.add(pos)
        else:
            pos += dist * dir
    return manhatten_distance(pos)


if __name__ == "__main__":
    print(
        "The distance to the Easter Bunny HQ is: ", solve(read_input_file("input.txt"))
    )
    print(
        "The distance to the Easter Bunny HQ is: ",
        solve(read_input_file("input.txt"), part2=True),
    )
