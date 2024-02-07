import re
from hashlib import md5

SALT = "qzyelonm"
THREE_CHARS_REGEX = re.compile(r"(\w)\1\1")


def hash(salt: str, index: int, use_stretching: bool = False) -> str:
    hash = md5((salt + str(index)).encode()).hexdigest()
    if use_stretching:
        for _ in range(2016):
            hash = md5(hash.encode()).hexdigest()
    return hash


def is_key(index: int, hashes: list[str]) -> bool:
    matches = THREE_CHARS_REGEX.search(hashes[index])
    if matches:
        for i in range(1, 1001):
            if matches[0][0] * 5 in hashes[index + i]:
                return True
    return False


def solve(salt: str, part_2: bool = False) -> int:
    keys = []
    hashes = [hash(salt, i, part_2) for i in range(1000)]

    index = 0
    while len(keys) < 64:
        hashes.append(hash(salt, index + 1000, part_2))
        if is_key(index, hashes):
            keys.append((index, hashes[index]))
        index += 1
    return keys[-1][0]


if __name__ == "__main__":
    print("The index", solve(SALT), "produces the 64th key")
    print("The index", solve(SALT, True), "produces the 64th key")
