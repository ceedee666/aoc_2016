import string
from collections import Counter

from commons import read_input_file


def parse_line(line: str) -> tuple[str, str, int]:
    parts = line.split("-")
    letters = parts[:-1]
    rest = parts[-1]
    id, checksum = rest.split("[")
    checksum = checksum[:-1]
    return "".join(letters), checksum, int(id)


def parse_input(lines: list[str]) -> list[tuple[str, str, int]]:
    return [parse_line(line) for line in lines]


def is_real_room(room: tuple[str, str, int]) -> bool:
    letters, checksum, _ = room
    counter = Counter(letters)
    most_common = counter.most_common()
    most_common = sorted(most_common, key=lambda c: (-c[1], c[0]))
    most_common_letters = [c[0] for c in most_common[:5]]
    return checksum == "".join(most_common_letters)


def decode(room: tuple[str, str, int]) -> tuple[str, str, int]:
    letters, checksum, id = room
    shift = id % len(string.ascii_lowercase)
    decoded = "".join(
        [
            string.ascii_lowercase[(string.ascii_lowercase.index(c) + shift) % 26]
            for c in letters
        ]
    )
    return decoded, checksum, id


def solve(lines: list[str], part2: bool = False) -> int:
    rooms = parse_input(lines)
    real_rooms = [r for r in rooms if is_real_room(r)]
    if not part2:
        sector_ids = [r[2] for r in real_rooms]
        return sum(sector_ids)
    else:
        real_rooms = [decode(r) for r in real_rooms]
        room = [r[2] for r in real_rooms if "north" in r[0]]
        return room[0]


if __name__ == "__main__":
    print(
        "The sum of the sector IDs of the real rooms is",
        solve(read_input_file("input.txt")),
    )
    print(
        "The sector ID of the room in which the 'north pole objects' are stored is",
        solve(read_input_file("input.txt"), True),
    )
