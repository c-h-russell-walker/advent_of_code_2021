from typing import Tuple

from utils.get_input import get_for_day


def _forward(
    h_pos: int,
    v_pos: int,
    aim: int,
    units: int,
) -> Tuple[int, int]:
    return h_pos + units, v_pos + (aim * units)


def _down(aim: int, units: int) -> int:
    return aim + units


def _up(aim: int, units: int) -> int:
    return aim - units


def solve_puzzle() -> None:
    h_pos = 0
    v_pos = 0
    aim = 0

    entries = [val.strip() for val in get_for_day(2).split('\n') if val.strip()]

    for entry in entries:
        direction, value = entry.split(' ')
        units = int(value)

        if direction == 'forward':
            h_pos, v_pos = _forward(
                h_pos=h_pos,
                v_pos=v_pos,
                aim=aim,
                units=units,
            )
        elif direction == 'down':
            aim = _down(aim=aim, units=units)
        elif direction == 'up':
            aim = _up(aim=aim, units=units)
        else:
            raise Exception(f'Unknown values:\n\tDirection: ({direction})\n\tUnits: ({units})')

    print(f'Horiz. Pos.\n\t{h_pos}\n')
    print(f'Vert. Pos.\n\t{v_pos}\n')
    print(f'Multiplied: {h_pos * v_pos}')


if __name__ == '__main__':
    solve_puzzle()
