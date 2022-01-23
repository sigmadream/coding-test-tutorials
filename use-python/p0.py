from time import perf_counter


def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = perf_counter()
        result = original_fn(*args, **kwargs)
        end_time = perf_counter()
        print(f"WorkingTime[{original_fn.__name__}]: {end_time - start_time} ms")
        return result

    return wrapper_fn
