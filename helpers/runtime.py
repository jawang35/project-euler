import timeit

def print_answer_and_elapsed_time(function):
    start = timeit.default_timer()
    answer = function()
    elapsed = timeit.default_timer() - start

    print("Answer: %(answer)s" % locals())
    print("Elapsed time: %(elapsed)s ms" % locals())
