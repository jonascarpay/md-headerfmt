#!/usr/bin/env python3

import fileinput
import re
from typing import Optional, Tuple

h1_pound = re.compile("# *([^#].*)$")
h1_under = re.compile("=+$")
h2_pound = re.compile("## *([^#].*)$")
h2_under = re.compile("-+$")
titleish = re.compile("( *)(\\w.*)$")

line_buffer: Optional[Tuple[str, str]] = None
h1_leading_spaces: Optional[int] = None
h2_leading_spaces: Optional[int] = None


def flush_buffer() -> None:
    global line_buffer
    if line_buffer:
        indent, text = line_buffer
        print(indent + text)
        line_buffer = None


def print_h1(spaces: int, text: str) -> None:
    global h1_leading_spaces
    if h1_leading_spaces is None:
        h1_leading_spaces = spaces
    print(" " * h1_leading_spaces + text)
    print((h1_leading_spaces * 2 + len(text)) * "=")


def print_h2(spaces: int, text: str) -> None:
    global h2_leading_spaces
    if h2_leading_spaces is None:
        h2_leading_spaces = spaces
    print(" " * h2_leading_spaces + text)
    print((h2_leading_spaces * 2 + len(text)) * "-")


for line in fileinput.input():

    m = titleish.match(line)
    if m:
        flush_buffer()
        line_buffer = m.group(1), m.group(2)
        continue

    m = h1_pound.match(line)
    if m:
        flush_buffer()
        print_h1(0, m.group(1))
        continue

    m = h2_pound.match(line)
    if m:
        flush_buffer()
        print_h2(0, m.group(1))
        continue

    if h1_under.match(line) and line_buffer:
        indent, text = line_buffer
        print_h1(len(indent), text)
        line_buffer = None
        continue

    if h2_under.match(line) and line_buffer:
        indent, text = line_buffer
        print_h2(len(indent), text)
        line_buffer = None
        continue

    flush_buffer()
    print(line, end="")

flush_buffer()
