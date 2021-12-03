import os

import requests


def get_from_url(url: str):
    session_cookie = os.environ.get('SESSION_COOKIE')
    resp = requests.get(url, cookies={'session': session_cookie})

    return resp.text


def get_for_day(day: int):
    return get_from_url(f'https://adventofcode.com/2021/day/{day}/input')
