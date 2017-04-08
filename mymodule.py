#!/usr/bin/env python2

"""Test module for showing off modules

This should never be used in production
"""

"""Sedan class holds information about cars"""
class Sedan():
    def __init__(self, numwheels):
        self.numwheels = numwheels

    def go_forward(self):
        """Prints 'going forward'"""
        print "going forward"


def test():
    """Print out the word test

    No arguments or returns
    """
    print "hello"

