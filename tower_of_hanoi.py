a = [1, 2, 3, 4]
b = []
c = []

def tower(n, a, b, c):
    if n == 1:
        print(f"Move disk from {a} to disk {c}")
        return
    tower(n - 1, a, c, b)
    print(f"Move {n}th disk from {a} to {c} ")
    tower(n-1, b,c,a)

tower(4, 'A', 'B', 'C')