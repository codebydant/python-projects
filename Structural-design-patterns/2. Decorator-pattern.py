import functools

# Fibonacci(8) = 17.5073835 seconds
known = {0: 0, 1: 1}


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


@memoize
def fibonacci(n):
    '''Returns the nth number of the Fibonacci sequence'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)

# Fibonacci(8) = 0.3047768 seconds
# def fibonacci(n):
#     assert(n >= 0), 'n must be >= 0'
#     a, b = 0, 1
#     for i in range(n + 1):
#         yield a
#         a, b = b, a + b


known_sum = {0: 0}


@memoize
def nsum(n):
    assert(n >= 0), 'n must be >= 0'
    if n in known_sum:
        return known_sum[n]
    res = n + nsum(n - 1)
    known_sum[n] = res
    return res


if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(200)', 'import': 'fibonacci', 'func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum', 'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time: {}'.format(m['func'].__name__, m['func'].__doc__,
                                                                  m['exec'], t.timeit()))
