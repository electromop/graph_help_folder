n = 5
d = []
rez = []

for i in range(1, n//2 + 1):
    d.append(i)

kon = (2**(n//2)) - 1

for a in range(1, kon + 1):
    for b in range(1, kon + 1):
        print(a, b, min((a + b), n - (a + b)))
        c = min((a + b), n - (a + b))
        if c in d:
            rez.append(f'c({c}) in {d}')

for i in rez:
    print(i)
