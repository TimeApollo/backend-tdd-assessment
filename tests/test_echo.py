#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import unittest
import echo


# Your test case class goes here
class TestKatas(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEqual(stdout, usage)

    def test_upper_argparse_upper(self):
        """ verifying --upper stores upper in args namespace """

        arg = echo.create_parser().parse_args(['--upper', 'hello'])
        self.assertTrue(arg.upper)

    def test_upper_argparse_u(self):
        """ verifying -u stores upper in args namespace """

        arg = echo.create_parser().parse_args(['-u', 'hello'])
        self.assertTrue(arg.upper)

    def test_upper_u(self):
        """ Running echo with -u option """

        process = subprocess.Popen(
                      ["python", "./echo.py", "-u", "hello"],
                      stdout=subprocess.PIPE,
                    )
        stdout, _ = process.communicate()
        self.assertEqual(stdout.strip(), "HELLO")

    def test_lower_argparse_lower(self):
        """ verifying --lower stores lower in args namespace """

        arg = echo.create_parser().parse_args(['--lower', 'HELLO'])
        self.assertTrue(arg.lower)

    def test_lower_argparse_l(self):
        """ verifying -l stores lower in args namespace """

        arg = echo.create_parser().parse_args(['-l', 'HELLO'])
        self.assertTrue(arg.lower)

    def test_lower_l(self):
        """ Running echo with -l option """

        process = subprocess.Popen(
                      ["python", "./echo.py", "-l", "HELLO"],
                      stdout=subprocess.PIPE
                    )
        stdout, _ = process.communicate()
        self.assertEqual(stdout.strip(), "hello")

    def test_title_argparse_t(self):
        """ Verifying -t stores title in args namespace """

        arg = echo.create_parser().parse_args(['-t', "hello"])
        self.assertTrue(arg.title)

    def test_title_argparse_title(self):
        """ Verifying --title stores title in args namespace """

        arg = echo.create_parser().parse_args(['--title', 'hello'])
        self.assertTrue(arg.title)

    def test_title_t(self):
        """ Running echo with -t option """

        process = subprocess.Popen(
                    ['python', './echo.py', '-t', 'hello'],
                    stdout=subprocess.PIPE
                  )

        stdout, _ = process.communicate()
        self.assertEqual(stdout.strip(), 'Hello')

    def test_multi_argparse_tu(self):
        """ Verifying -tu stores title and upper in args namespace """

        arg = echo.create_parser().parse_args(['-tu', 'hello'])
        self.assertTrue(arg.title and arg.upper)

    def test_title_multi_word_text(self):
        """ Running echo with -t option with multi-word text """

        process = subprocess.Popen(
                    ['python', './echo.py', '-t', 'hello world'],
                    stdout=subprocess.PIPE
                  )

        stdout, _ = process.communicate()
        self.assertEqual(stdout.strip(), 'Hello World')

    def test_all_options_tul(self):
        """ Running echo with -tul options """

        process = subprocess.Popen(
            ['python', './echo.py', '-tul', 'hello world!'],
            stdout=subprocess.PIPE
        )

        stdout, _ = process.communicate()
        self.assertEqual(stdout.strip(), 'Hello World!')

    def test_some_options_ul(self):
        """ Running echo with -u -l options """

        process = subprocess.Popen(
            ['python', './echo.py', '-u', '-l', 'heLLo!'],
            stdout=subprocess.PIPE
        )

        stdout, _ = process.communicate()
        self.assertEqual(stdout.strip(), 'hello!')

    def test_no_arguments_only_text(self):
        """ Running echo with no options and only text """

        process = subprocess.Popen(
            ['python', './echo.py', 'Hello World!'],
            stdout=subprocess.PIPE
        )

        stdout, _ = process.communicate()
        self.assertEqual(stdout.strip(), 'Hello World!')


if __name__ == '__main__':
    unittest.main()
