from collections import deque

FAVORITE_NUM = 1358

DIRECTIONS = [1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j]


def is_open_space(pos: complex, favorite_num: int) -> bool:
    x, y = int(pos.real), int(pos.imag)
    value = x**2 + (3 * x) + (2 * x * y) + y + y**2 + favorite_num
    return value.bit_count() % 2 == 0


def neighbours(pos: complex, favorite_num: int) -> list[complex]:
    positions = [pos + d for d in DIRECTIONS]
    return [
        p
        for p in positions
        if is_open_space(p, favorite_num) and p.imag >= 0 and p.real >= 0
    ]


def solve(
    start: tuple[int, int] = (1, 1),
    destination: tuple[int, int] = (31, 39),
    favorite_num: int = FAVORITE_NUM,
    part1: bool = True,
) -> int:
    dest = complex(*destination)

    visited = set()
    q = deque([(complex(*start), 0)])

    while q:
        pos, dist = q.popleft()

        if part1 and pos == dest:
            return dist
        else:
            visited.add(pos)
            for n in neighbours(pos, favorite_num):
                if n not in visited:
                    if part1:
                        q.append((n, dist + 1))
                    else:
                        if dist < 50:
                            q.append((n, dist + 1))
    return len(visited)


if __name__ == "__main__":
    print("The minimal number of steps is", solve())
    print(solve(part1=False), "can be reached in 50 steps")
