import argparse
from collections import namedtuple
from pathlib import Path
from typing import Any, List

from utils.get_input import get_for_day

BoardTile = namedtuple('BoardTile', ['number', 'marked'])

BoardType = List[List[BoardTile]]


def _mark_bingo_board(board: BoardType, number: int) -> None:
    for row in board:
        for tile in row:
            if tile.number == number:
                tile = tile._replace(marked=True)


def _check_board_for_bingo(board: BoardType) -> bool:
    # Check horizontals
    # Check verticals
    # Check two diagonals
    pass


def _sum_unmarked_numbers(board: BoardType) -> int:
    total = 0
    for row in board:
        for tile in row:
            total += tile.marked
    return total


def _calculate_final_score(unmarked_sum: int, final_number: int) -> int:
    return unmarked_sum * final_number


# TODO - Move this to a utility function
# Also better annotate the return type
def _get_data(use_test_data: bool = False) -> Any:
    if not use_test_data:
        return get_for_day(4)
    else:
        parent_dir = Path(__file__).parent
        input_file = Path(parent_dir, './test_input.txt')
        with open(input_file) as file:
            data = file.read()
        return data


def solve_puzzle(use_test_data: bool = False) -> None:
    boards = []

    data = _get_data(use_test_data=use_test_data)
    split_data = data.split('\n')
    random_numbers = split_data[0].split(',')
    boards_data = split_data[1:]

    temp_board: BoardType = []
    for raw_board_data in boards_data:
        if not raw_board_data:
            if temp_board:
                # Boards are delimited by empty strings
                boards.append(temp_board)
                temp_board = []
        else:
            board_data = [BoardTile(num, False) for num in raw_board_data.split(' ') if num.strip()]
            temp_board.append(board_data)

    for random_num in random_numbers:
        for board in boards:
            _mark_bingo_board(board=board, number=random_num)
        # Maybe we could have multiple winners at once? - Leave as a TODO
        for board in boards:
            if _check_board_for_bingo(board=board):
                unmarked_sum = _sum_unmarked_numbers(board)
                print(f'Final Score: {_calculate_final_score(unmarked_sum=unmarked_sum, final_number=random_num)}')
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-data', action='store_true')
    args = parser.parse_args()
    solve_puzzle(use_test_data=args.test_data)
