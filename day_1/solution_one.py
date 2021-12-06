from utils.get_input import get_for_day


def solve_puzzle() -> None:
    increased_count = 0
    # TODO - Move this to a reusable utility function - the parsing of the lines
    entries = [int(val.strip()) for val in get_for_day(1).split('\n') if val.strip()]
    prev_depth = entries.pop(0)

    for entry in entries:
        if entry > prev_depth:
            increased_count += 1
        prev_depth = entry

    print(f'{increased_count=}')


if __name__ == '__main__':
    solve_puzzle()
