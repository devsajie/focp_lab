def multiply(a, b=None):
    if b is None:
        return a * a
    return a * b

print(multiply(4, 5))
print(multiply(7))
