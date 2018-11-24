#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TDD echo command line tool creation

Using test driven development, the program implements the echo function
with some added features

Aaron Jackson
TimeApollo
"""

__author__ = "TimeApollo"

import argparse
import sys


def upper_case(text):
    return text.upper()


def lower_case(text):
    return text.lower()


def title_case(text):
    return text.title()


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("-u", "--upper", action="store_true",
                        help="convert text to uppercase")
    parser.add_argument("-l", "--lower", action="store_true",
                        help="convert text to lowercase")
    parser.add_argument("-t", "--title", action="store_true",
                        help="convert text to titlecase")
    parser.add_argument("text", help="text to be manipulated")

    return parser


def main(args):
    """Implementation of echo"""
    parser_args = create_parser().parse_args(args)
    text = parser_args.text

    if parser_args.upper:
        text = upper_case(text)
    if parser_args.lower:
        text = lower_case(text)
    if parser_args.title:
        text = title_case(text)

    print(text)


if __name__ == "__main__":
    main(sys.argv[1:])
