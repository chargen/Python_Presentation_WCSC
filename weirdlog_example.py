#!/usr/bin/env python2

import logging
import inspect

# import logging_tree




class MylocalFilter(logging.Filter):
    def filter(self, record):
        '''try:
            mylocal = record.mylocal
        except keyError:
            record.mylocal = "_none_"'''
        mylocal = calling_scope_variable("mylocal")
        record.mylocal = mylocal or "_none_"
        # print "running filter"
        return True


if __name__ == '__main__':
    # Use coloredlogs if we have them
    log_format = '%(asctime)s | %(levelname)8s %(module)s:%(funcName)s:%(lineno)d [%(process)d] %(mylocal)s | %(message)s'
    log_dateformat = '%Y-%m-%dT%H:%M:%S'
    try:
        import coloredlogs
    except ImportError:
        logging.basicConfig(
            level=logging.DEBUG,
            format=log_format,
            datefmt=log_dateformat)
    else:
        coloredlogs.install(
            level=logging.DEBUG,
            datefmt=log_dateformat,
            field_styles = {
                'asctime': {'color': 'green'},
                'levelname': {'color': 'black', 'bold': True},
                'module': {'color': 'yellow'},
                'process':{'color':'magenta'}},
            fmt = log_format)

    rootlog = logging.getLogger()
    rootlog.setLevel(logging.DEBUG)

    # Filters don't propagate on the log instances
    # Instead, add the filter to all handlers
    # http://stackoverflow.com/a/17276457/2293508
    mlf = MylocalFilter()
    for handler in rootlog.handlers:
        handler.addFilter(mlf)
    # rootlog.addFilter(mlf)



log = logging.getLogger(__name__)



def calling_scope_variable(name):
    """Return a varible by name from the caller's scope

    This is hella' sketch, so probably don't rely on it.
    http://stackoverflow.com/a/14694234/2293508

    We may need to use `del` on frame references to help
    garbage collection
    """
    try:
        frame = inspect.stack()[1][0]
        while name not in frame.f_locals:
            frame = frame.f_back
            if frame is None:
                return None
        return frame.f_locals[name]
    except:
        log.exception("Unknown failure getting scope")
        return None



def dec(f):
    def wrapped(*args, **kwargs):
        mylocal = calling_scope_variable("mylocal")
        log.debug("dec: calling %s"%f.__name__)
        log.debug("dec: local: %s"%mylocal)
        return f(*args, **kwargs)
    log.debug("dec: wrapping %s"%f.__name__)
    return wrapped


@dec
def test():
    log.info("test")

def baz():
    log.info("calling test")
    mylocal = "woohoo"
    log.info("calling test")
    test()
    del mylocal
    log.info("Deleted mylocal")

if __name__ == '__main__':
    baz()
    # logging_tree.printout()