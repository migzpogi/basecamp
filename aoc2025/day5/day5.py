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
    :return: A list of fresh ingredient ranges, and a list of available ingredients ranges
    :rtype: tuple (range(), range())
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

def is_range_overlap(rng_start, rng_stop):
    """
    Determines if the two given ranges overlap with each other.
    The order of ranges matter.

    range(10,15) and range(12,19) == True
    range(12,19) and range(10,15) == False

    :param rng_start: Range with the smaller start
    :type database: range
    :param rng_stop: Range with the higher stop
    :type database: range
    :return: True/False
    :rtype: boolean
    """
    if rng_stop[0] <= rng_start[-1]:
        return True
    else:
        return False

def extend_range(rng_start, rng_stop):
    """
    Extends/retains the range if they overlap
    The order of ranges matter.

    range(10,15) and range(12,19) -> range(10,19)
    range(10,18) and range(12,15) -> range(10,18)

    :param rng_start: Range with the smaller start
    :type database: range
    :param rng_stop: Range with the higher stop
    :type database: range
    :return: Extended or retained range
    :rtype: range()
    """
    if is_range_overlap(rng_start, rng_stop):
        if rng_stop[-1] <= rng_start[-1]:
            return(range(rng_start[0], rng_start[-1]+1))
        else:
            return(range(rng_start[0], rng_stop[-1]+1))
    else:
        raise ValueError("Given ranges do not overlap.")

def run(file_path):
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

def run_2(file_path):
    """
    Given a list of fresh ids   -> [range(3,5), range(10,14), range(16,20), range(12,18)]
    Sort it in descending order -> [range(16,20), range(12,18), range(10,14), range(3,5)]
    Pop the elements and evaluate merge/retain logic.

    [(16,20), (12,18), (10,14)]     [(3,5)]
    [(16,20), (12,18)]              [(3,5), (10,14)]
    [(16,20)]                       [(3,5), (10,18)]
    []                              [(3,5), (10,20)]

    Count elements in new list -> 14
    """
    database = read_lines(file_path)
    fresh_ids, avail_ids = process_ingredient_database(database)
    fresh_ids.sort(key=lambda x: x[0], reverse=True)

    combined_ranges = [range(0,0)]
    unique_ids = 0

    while fresh_ids:
        p = fresh_ids.pop()
        q = combined_ranges.pop()
    
        if q == range(0,0):
            combined_ranges.append(q)
            combined_ranges.append(p)
            continue

        if is_range_overlap(q, p):
            combined_ranges.append(extend_range(q,p))
        else:
            combined_ranges.append(q)
            combined_ranges.append(p)

    for i in combined_ranges:
        unique_ids += len(i)


    return unique_ids

if __name__ == '__main__':
    # print(run('aoc2025/day5/first.txt'))
    print(run_2('aoc2025/day5/first.txt'))
