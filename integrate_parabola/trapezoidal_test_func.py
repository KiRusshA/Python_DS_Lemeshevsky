from rectangular import rectangular

g = lambda x: 2*(x**3)
a = 1; b = 3
n = 250
r = rectangular(g, a, b, n)
print(r)