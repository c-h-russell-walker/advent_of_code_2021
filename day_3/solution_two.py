from collections import Counter

from utils.get_input import get_for_day


def solve_puzzle() -> None:  # noqa[C901]
    entries = [val.strip() for val in get_for_day(3).split('\n') if val.strip()]
    length = len(entries[0])

    oxygen_entries = entries[:]
    co2_entries = entries[:]

    for i in range(length):
        ctr = Counter([val[i] for val in oxygen_entries])
        try:
            (most_common_bit, most_common_count), (least_common_bit, least_common_count) = ctr.most_common()
            if most_common_count == least_common_count:
                bit_to_check = '1'
            else:
                bit_to_check = most_common_bit
        except ValueError:
            ((most_common_bit, most_common_count),) = ctr.most_common()
            bit_to_check = most_common_bit

        oxygen_entries = [entry for entry in oxygen_entries if entry[i] == bit_to_check]
        if len(oxygen_entries) == 1:
            break

    print(f'{oxygen_entries=}')

    for i in range(length):
        ctr = Counter([val[i] for val in co2_entries])
        try:
            (most_common_bit, most_common_count), (least_common_bit, least_common_count) = ctr.most_common()
            if most_common_count == least_common_count:
                bit_to_check = '0'
            else:
                bit_to_check = least_common_bit
        except ValueError:
            ((most_common_bit, most_common_count),) = ctr.most_common()
            bit_to_check = least_common_bit

        co2_entries = [entry for entry in co2_entries if entry[i] == bit_to_check]
        if len(co2_entries) == 1:
            break

    print(f'{co2_entries=}')

    print(f'Life support rating: {int(oxygen_entries[0], 2) * int(co2_entries[0], 2)}')


if __name__ == '__main__':
    solve_puzzle()
