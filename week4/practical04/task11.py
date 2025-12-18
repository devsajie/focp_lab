to_seconds = lambda hours, minutes: hours*3600 + minutes*60

print(to_seconds(0, 2))
print(to_seconds(2, 0))
print(to_seconds(1, 30))
