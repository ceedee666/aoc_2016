import re

from commons import read_input_file


def decode(line: str) -> str:
    decoded_line = ""
    pos = 0
    while pos < len(line):
        marker_start = line.find("(", pos)
        marker_end = line.find(")", marker_start)

        if marker_start == -1 and marker_end == -1:
            decoded_line += line[pos : len(line) + 1]
            pos = len(line)

        if marker_start > pos:
            decoded_line += line[pos:marker_start]

        if marker_start != -1 and marker_end != -1:
            values = [int(x) for x in re.findall(r"\d+", line[marker_start:marker_end])]
            length, repetitions = values
            decoded_line += line[marker_end + 1 : marker_end + 1 + length] * repetitions

            pos = marker_end + length + 1

    return decoded_line


def solve(line: str, part2: bool = False) -> int:
    if not part2:
        return len(decode(line))
    else:
        decoded_line = line
        while "(" in decoded_line:
            decoded_line = decode(decoded_line)
        return len(decoded_line)


if __name__ == "__main__":
    print("The length of the decoded file is", solve(read_input_file("input.txt")[0]))
    print(
        "The length of the decoded file is",
        solve(read_input_file("input.txt")[0], True),
    )
