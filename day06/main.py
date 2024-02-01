from collections import Counter
from typing import Iterator

from commons import read_input_file


def solve(lines: Iterator[str], part2: bool = False) -> str:
    message = ""
    transposed = zip(*lines)
    for line in transposed:
        if not part2:
            message += Counter(line).most_common()[0][0]
        else:
            message += Counter(line).most_common()[-1][0]
    return message


if __name__ == "__main__":
    print(
        "The error corrected version of the message is",
        solve(read_input_file("input.txt")),
    )
    print(
        "The error corrected version of the message is",
        solve(read_input_file("input.txt"), True),
    )
