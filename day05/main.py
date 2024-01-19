import hashlib


def find_hash(i: int, door_id: str = "wtnhxymk") -> tuple[str, int]:
    while True:
        hash = hashlib.md5(f"{door_id}{i}".encode()).hexdigest()
        if hash.startswith("00000"):
            return hash, i
        i += 1


def solve(door_id: str = "wtnhxymk", part2: bool = False) -> str:
    if not part2:
        passwd = ""
        i = 0
        while len(passwd) < 8:
            hash, i = find_hash(i, door_id)
            i += 1
            passwd += hash[5]

        return passwd
    else:
        passwd = "--------"
        i = 0
        while "-" in passwd:
            hash, i = find_hash(i, door_id)
            i += 1

            if hash[5].isdigit():
                pos = int(hash[5])
                if pos < len(passwd) and passwd[pos] == "-":
                    passwd = passwd[:pos] + hash[6] + passwd[pos + 1 :]
        return passwd


if __name__ == "__main__":
    print("The password is", solve())
    print("The second password is", solve(part2=True))
