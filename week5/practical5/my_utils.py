def average(values):
    """ Calculates the average of the given list. """
    total = 0.0
    for n in values:
        total += float(n)
    return total / len(values)

if __name__ == "__main__":
    import sys

    if len(sys.argv) <= 1:
        print("no arguments were provided")
    else:
        values = [float(x) for x in sys.argv[1:]]
        print("Average of provided args is", average(values))
