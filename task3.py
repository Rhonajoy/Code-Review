def average_valid_measurements(values):
    total = 0
    count = len(values)
    print(count)
    for v in values:
        if v is not None:
            total += float(v)
            print(total)

    print( total / count)
average_valid_measurements([10, None, 20])