from pathlib import Path
from typing import Iterator


def read_input_file(input_file_path: str) -> Iterator[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return (line.strip() for line in lines)
