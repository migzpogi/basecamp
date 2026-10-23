import re

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


if __name__ == '__main__':
    # lines = read_lines("sample.txt")
    lines = read_lines("input.txt")
    print(len(lines))