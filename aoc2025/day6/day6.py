import re
from typing import List, Tuple

class HomeWork:
    def __init__(self):
        self.matrix = []
        self.operators = []
        self.x_size = 0
        self.y_size = 0

    def __update_x_size(self):
        self.x_size += 1

    def __update_y_size(self, y):
        self.y_size = y

    def add_elements(self, elements):
        self.matrix.append(elements)
        self.__update_x_size()
        self.__update_y_size(len(elements))

    def add_operators(self, operators):
        self.operators = operators

    def get_element(self, x, y):
        return self.matrix[x][y]

    def compute_column(self, n):
        answer = 0
        for idx, i in enumerate(self.matrix):
            if idx == 0:
                answer = i[n]
            else:
                if self.operators[n] == '*':
                    answer *= i[n]
                if self.operators[n] == '+':
                    answer += i[n]
        return answer

    def compute_homework(self):
        total = 0
        for i in range(self.y_size):
            total += self.compute_column(i)

        return total

    
def foo():
    return 1

def read_lines(file_path, encoding='utf-8'):
    """
    Read a file line by line without trailing spaces

    :param file_path: Location of the file to be opened
    :type file_path: str
    :param encoding: Character encoding to be used ['utf-8', 'ascii', etc]
    :type encoding: str
    :return: Each line of the file as elements of a list
    :rtype: [str]
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return [line.strip() for line in file]

def read_raw_lines(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        return [line.rstrip('\r\n') for line in file]

def prepare_problem_input(line):
    """
    Removes the white spaces in between elements of the problem input.
    The number of white spaces in between are inconsistent, so a better approach is needed
      compared to str.split() 

    Converts to integer type whenever possible; retains str for operations
    """
    new_line = re.split(r"[,\s]+", line)

    if new_line[0] not in ['+', '*']:
        return list(map(lambda n: int(n), new_line))
    else:
        return new_line

def run_1(input_file):
    lines = read_lines(input_file)
    h = HomeWork()

    for l in lines:
        row = prepare_problem_input(l)
        if row[0] not in ['+', '*']:
            h.add_elements(prepare_problem_input(l))
        else:
            h.add_operators(prepare_problem_input(l))

    return h.compute_homework()

def parse_part_2_problems(lines: List[str]) -> List[Tuple[str, List[int]]]:
    if len(lines) < 2:
        raise ValueError("Worksheet must contain at least one number row and an operator row")

    width = max(len(line) for line in lines)
    rows = [line.ljust(width) for line in lines]
    digit_rows = rows[:-1]
    operator_row = rows[-1]
    problems = []
    span_start = None

    for column in range(width + 1):
        has_content = column < width and any(
            not row[column].isspace() for row in rows
        )

        if has_content and span_start is None:
            span_start = column
        elif not has_content and span_start is not None:
            span_end = column
            operators = [
                operator_row[index]
                for index in range(span_start, span_end)
                if not operator_row[index].isspace()
            ]
            if len(operators) != 1 or operators[0] not in ('+', '*'):
                raise ValueError("Each problem span must contain exactly one '+' or '*' operator")

            numbers = []
            for index in range(span_end - 1, span_start - 1, -1):
                digits = []
                for row in digit_rows:
                    character = row[index]
                    if character.isdigit():
                        digits.append(character)
                    elif not character.isspace():
                        raise ValueError("Number rows may contain only digits and whitespace")
                if digits:
                    numbers.append(int(''.join(digits)))

            if not numbers:
                raise ValueError("Each problem span must contain at least one number")
            problems.append((operators[0], numbers))
            span_start = None

    if not problems:
        raise ValueError("Worksheet does not contain any problem spans")
    return problems

def run_2(input_file):
    problems = parse_part_2_problems(read_raw_lines(input_file))
    total = 0

    for operator, numbers in problems:
        answer = numbers[0]
        for number in numbers[1:]:
            if operator == '*':
                answer *= number
            else:
                answer += number
        total += answer

    return total



if __name__ == '__main__':
    print(run_1("input.txt"))
    print(run_2("input.txt"))