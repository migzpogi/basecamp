import re

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



if __name__ == '__main__':
    print(run_1("input.txt"))