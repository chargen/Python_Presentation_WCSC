#!/usr/bin/env python3

import logging

# import coloredlogs
# import loggingtree

# Get the local logger instance
log = logging.getLogger(__name__)



def spam():
    log.debug("Running an example")

    for i in range(5, -1, -1):
        if i == 3:
            log.info("Found the number 3")
        try:
            baz = 1 / i
        except ZeroDivisionError:
            log.exception("Whoops, that math didn't work")


if __name__ == '__main__':
    logging.basicConfig()

    log.setLevel("DEBUG")
    log.info("Wew, started main")

    spam()

    log.info("Finished")