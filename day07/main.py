import re
from typing import Iterator

from commons import read_input_file


def supports_tls(ip: str) -> bool:
    abba_regex = re.compile(r"(\w)(?!\1)(\w)\2\1")
    parts = re.split(r"\[|\]", ip)

    parts_outside_brackets = [p for i, p in enumerate(parts) if i % 2 == 0]
    parts_inside_brackets = [p for i, p in enumerate(parts) if i % 2 != 0]

    matching_parts_outside = [
        abba_regex.search(part) for part in parts_outside_brackets
    ]
    matching_parts_inside = [abba_regex.search(part) for part in parts_inside_brackets]
    if any(matching_parts_outside) and not any(matching_parts_inside):
        return True
    else:
        return False


def supports_ssl(ip: str) -> bool:
    # use the look ahead assertion ?= as the aba expressions might be overlapping.
    # For an example see the last part of test string 3
    aba_regex = re.compile(r"(?=(\w)(?!\1)(\w)\1)")
    parts = re.split(r"\[|\]", ip)

    parts_outside_brackets = [p for i, p in enumerate(parts) if i % 2 == 0]
    parts_inside_brackets = [p for i, p in enumerate(parts) if i % 2 != 0]

    matches_outside = [aba_regex.findall(part) for part in parts_outside_brackets]
    for matches in matches_outside:
        if any(
            [
                any(
                    [m[1] + m[0] + m[1] in p for p in parts_inside_brackets]
                )  # Matches a tuples due to capturing groups in the regex
                for m in matches
            ]
        ):
            return True
    return False


def solve(
    lines: Iterator[str],
) -> tuple[int, int]:
    ips_supporting_tls = [ip for ip in lines if supports_tls(ip)]
    ips_supporting_ssl = [ip for ip in lines if supports_ssl(ip)]
    return len(ips_supporting_tls), len(ips_supporting_ssl)


if __name__ == "__main__":
    print(solve(read_input_file("input.txt"))[0], "IPs support TLS.")
    print(solve(read_input_file("input.txt"))[1], "IPs support SSL.")
