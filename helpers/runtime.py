import timeit

def print_answer_and_elapsed_time(function):
    start = timeit.default_timer()
    answer = function()
    elapsed = 1000 * (timeit.default_timer() - start)

    print("Answer: %(answer)s" % locals())
    print("Elapsed time: %(elapsed)s ms" % locals())
