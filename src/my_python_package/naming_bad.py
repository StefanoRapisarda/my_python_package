def do_something(a, b):
    c = 0
    for d in b:
        c += d
    return a * c


x = 5
y = [1, 2, 3]

z = do_something(x, y)

print(z)