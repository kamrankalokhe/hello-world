#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 20:32:49 2018

@author: kkalokhe
"""

from unittest.mock import patch

from colors import print_colors


@patch("builtins.input", side_effect=['blue', 'Yellow', 'white',
                                      'red', 'Orange', 'quit'])
def test_print_colors(input_mock, capfd):
    not_valid = 'Not a valid color'
    expected = '\n'.join(['blue', 'yellow', not_valid, 'red',
                          not_valid, 'bye'])

    print_colors()

    output = capfd.readouterr()[0].strip()
    assert output == expected