def my_range_gen(start=0, stop=0, step=1):
    if stop == 0:
        start, stop = 0, start
    if step > 0:
        if start > stop:
            return
        while start < stop:
            yield start
            start += step
    elif step < 0:
        if start < stop:
            return
        while stop < start:
            yield start
            start += step
    elif step == 0:
        return