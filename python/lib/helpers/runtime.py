from timeit import default_timer


def print_answer_and_elapsed_time(function):
    start = default_timer()
    answer = function()
    elapsed = 1000 * (default_timer() - start)

    print('Answer: %(answer)s' % locals())
    print('Elapsed time: %(elapsed)s ms' % locals())
