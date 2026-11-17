from typing import List, Tuple


def read_lines(file_path: str, encoding: str = 'utf-8') -> List[str]:
    """Read grid rows, removing only newline terminators."""
    with open(file_path, 'r', encoding=encoding) as file:
        return [line.rstrip('\r\n') for line in file]


def parse_manifold(lines: List[str]) -> Tuple[List[str], int, int]:
    """Validate a manifold grid and return its rows and the start coordinate."""
    if not lines:
        raise ValueError("Manifold must contain at least one row")

    width = len(lines[0])
    if width == 0:
        raise ValueError("Manifold rows must not be empty")

    start = None
    for row_index, row in enumerate(lines):
        if len(row) != width:
            raise ValueError("Manifold must be rectangular")

        for column_index, character in enumerate(row):
            if character not in ('.', '^', 'S'):
                raise ValueError("Manifold may contain only '.', '^', and 'S'")
            if character == 'S':
                if start is not None:
                    raise ValueError("Manifold must contain exactly one 'S'")
                start = (row_index, column_index)

    if start is None:
        raise ValueError("Manifold must contain exactly one 'S'")

    return lines, start[0], start[1]


def count_splits(lines: List[str]) -> int:
    """Return the number of splitter cells reached by merged beams."""
    rows, start_row, start_column = parse_manifold(lines)
    width = len(rows[0])
    active_columns = {start_column}
    split_count = 0

    for row in rows[start_row + 1:]:
        next_columns = set()
        for column in active_columns:
            if row[column] == '^':
                split_count += 1
                if column > 0:
                    next_columns.add(column - 1)
                if column + 1 < width:
                    next_columns.add(column + 1)
            else:
                next_columns.add(column)
        active_columns = next_columns

    return split_count


def run_1(file_path: str) -> int:
    """Read the input file and return its Part 1 split count."""
    return count_splits(read_lines(file_path))

print(run_1("input.txt"))