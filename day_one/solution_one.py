from utils.get_input import get_for_day


def solve_puzzle():
    increased_count = 0
    # TODO - Move this to a reusable utility function - the parsing of the lines
    entries = get_for_day(1).split('\n')
    prev_depth = int(entries.pop(0))
    for entry in entries:
        if not entry:
            pass
        try:
            if int(entry) > prev_depth:
                increased_count += 1
        except ValueError:
            print(f"Entry not an integer: {entry}")
            continue

        prev_depth = int(entry)

    print(f'{increased_count=}')


if __name__ == '__main__':
    solve_puzzle()
