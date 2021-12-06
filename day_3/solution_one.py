from collections import Counter

from utils.get_input import get_for_day


def solve_puzzle() -> None:
    gamma = ''
    epsilon = ''

    entries = [val.strip() for val in get_for_day(3).split('\n') if val.strip()]
    length = len(entries[0])

    for i in range(length):
        ctr = Counter([val[i] for val in entries])
        # Since these are binary we can calculate both gamma and epsilon
        gamma += str(ctr.most_common()[0][0])
        epsilon += str(ctr.most_common()[1][0])
    print(f'Gamma:\n\tBinary: {gamma}\n\tDecimal: {int(gamma, 2)}\n')
    print(f'Epsilon:\n\tBinary: {epsilon}\n\tDecimal: {int(epsilon, 2)}\n')

    print(f'Power Consumption: {int(gamma, 2) * int(epsilon, 2)}')


if __name__ == '__main__':
    solve_puzzle()
