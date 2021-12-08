import argparse
from collections import namedtuple
from pathlib import Path
from typing import Any, List

from utils.get_input import get_for_day

Coord = namedtuple('Coord', ['x', 'y'])

Line = namedtuple('Line', ['coord_one', 'coord_two'])


# TODO - Move this to a utility function
# Also better annotate the return type
def _get_data(use_test_data: bool = False) -> Any:
    if not use_test_data:
        return get_for_day(5)
    else:
        parent_dir = Path(__file__).parent
        input_file = Path(parent_dir, './test_input.txt')
        with open(input_file) as file:
            data = file.read()
        return data


def _munge_data_as_lines(use_test_data: bool) -> List[Line]:
    data = _get_data(use_test_data=use_test_data)
    return [
        Line(
            Coord(
                int(entry.split('->')[0].strip().split(',')[0]),
                int(entry.split('->')[0].strip().split(',')[-1]),
            ),
            Coord(
                int(entry.split('->')[-1].strip().split(',')[0]),
                int(entry.split('->')[-1].strip().split(',')[-1]),
            ),
        )
        for entry in data.split('\n')
        if entry
    ]


def solve_puzzle(use_test_data: bool = False) -> None:
    lines = _munge_data_as_lines(use_test_data=use_test_data)
    print(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-data', action='store_true')
    args = parser.parse_args()
    solve_puzzle(use_test_data=args.test_data)
