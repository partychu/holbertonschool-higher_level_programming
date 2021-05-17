#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        func = fct(*args)
        return func
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
