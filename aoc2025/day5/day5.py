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


def process_ingredient_database(database):
    """
    The first part of the database is the list of fresh ingredient id ranges.
    An entry of "3-5" means that ingredient ids 3, 4, and 5 are all fresh.

    The second part of the database is the list of available ingredient ids.
    The two parts are delimited by the '' character.

    :param database: List of ingredient ids from the input file
    :type database: [str]
    :return: A list of fresh ingredient ranges, and a list of available ingredients
    :rtype: tuple
    """

    fresh_ids = []
    avail_ids = []

    for i in database:
        if '-' in i:
            # Fresh ingredient id ranges
            start = int(i.split('-')[0])
            end = int(i.split('-')[1])
            fresh_ids.append(range(start, end+1))
        elif i == '':
            # Delimiter
            pass
        else:
            # Available ingredient ids
            avail_ids.append(int(i))

    return (fresh_ids, avail_ids)

def run_sample(file_path):
    database = read_lines(file_path)
    fresh_ids, avail_ids = process_ingredient_database(database)
    fresh_count = 0

    for avail in avail_ids:
        first_pass = True
        for fresh in fresh_ids:
            if avail in fresh and first_pass:
                fresh_count += 1
                first_pass = False
        
    return fresh_count


if __name__ == '__main__':
    print(run_sample('aoc2025/day5/first.txt'))
