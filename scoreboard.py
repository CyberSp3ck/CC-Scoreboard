#!/usr/bin/env python3

import requests
import os
import time
import signal
from dotenv import load_dotenv
from rich.align import Align
from rich import box
from rich.table import Table
from rich.live import Live

load_dotenv()
TOKEN = os.getenv("TOKEN")
assert TOKEN, "TOKEN not found in .env file"
URL = os.getenv("URL", "https://ctf.cyberchallenge.it/api/scoreboard")


def get_scoreboard():
    r = requests.get(URL, headers={"Authorization": TOKEN})
    return r.json()


def generate_table(scoreboard, prev_scoreboard=None):
    table = Table(
        show_header=True,
        header_style="bold magenta",
        box=box.ROUNDED,
    )
    table.add_column("Pos", style="dim", width=4, justify="center")
    table.add_column("Name")
    table.add_column("Score", justify="right")
    table.row_styles = ["", "on color(236)"]

    for i, user in enumerate(scoreboard):
        if i == 0:
            style = "bold color(11)"
            pos = ":1st_place_medal:"
        elif i == 1:
            style = "bold color(248)"
            pos = ":2nd_place_medal:"
        elif i == 2:
            style = "bold color(202)"
            pos = ":3rd_place_medal:"
        else:
            style = ""
            pos = str(i + 1).rjust(2)

        if prev_scoreboard:
            for p_i, prev_user in enumerate(prev_scoreboard):
                if prev_user["displayedName"] == user["displayedName"]:
                    if i > p_i:
                        style = "bold green blink"
                    break

        table.add_row(
            pos,
            user["displayedName"],
            str(user["score"]),
            style=style,
        )
    return Align.center(table)


def signal_handler(sig, frame):
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    prev_scoreboard = None
    initial_table = generate_table(get_scoreboard())
    with Live(initial_table, screen=True) as live:
        while True:
            scoreboard = get_scoreboard()
            live.update(generate_table(scoreboard, prev_scoreboard))
            prev_scoreboard = scoreboard
            time.sleep(20)
