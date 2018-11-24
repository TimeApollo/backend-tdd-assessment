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


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument("-u", "--upper", action="store_true",
                        help="convert text to uppercase")
    parser.add_argument("-l", "--lower", action="store_true",
                        help="convert text to lowercase")
    parser.add_argument("-t", "--title", action="store_true",
                        help="convert text to titlecase")
    parser.add_argument("text", help="text to be manipulated")

    return parser.parse_args()


def main():
    """Implementation of echo"""
    args = create_parser()


if __name__ == "__main__":
    main()
