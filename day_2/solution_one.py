from utils.get_input import get_for_day


def _forward(h_pos: int, units: int) -> int:
    return h_pos + units


def _down(v_pos: int, units: int) -> int:
    return v_pos + units


def _up(v_pos: int, units: int) -> int:
    return v_pos - units


def solve_puzzle() -> None:
    h_pos = 0
    v_pos = 0

    entries = [val.strip() for val in get_for_day(2).split('\n') if val.strip()]

    for entry in entries:
        direction, value = entry.split(' ')
        units = int(value)

        if direction == 'forward':
            h_pos = _forward(h_pos=h_pos, units=units)
        elif direction == 'down':
            v_pos = _down(v_pos=v_pos, units=units)
        elif direction == 'up':
            v_pos = _up(v_pos=v_pos, units=units)
        else:
            raise Exception(f'Unknown values:\n\tDirection: ({direction})\n\tUnits: ({units})')

    print(f'Horiz. Pos.\n\t{h_pos}\n')
    print(f'Vert. Pos.\n\t{v_pos}\n')
    print(f'Multiplied: {h_pos * v_pos}')


if __name__ == '__main__':
    solve_puzzle()
