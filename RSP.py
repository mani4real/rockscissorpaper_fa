import random
print("be skg khosh amadid")
i = 1
r = 0
w = 0
d = 0
l = 0
u = 0
a = 0
while a < i:
    choice = input("sang ya kaghaz ya gheichi: ")
    if choice == 'sang':
        u = 1
    if choice == 'kaghaz':
        u = 2
    if choice == 'gheichi':
        u = 3
    c = random.randint(1, 3)
    if c == 1:
        cp = 'sang'
    if c == 2:
        cp = 'kaghaz'
    if c == 3:
        cp = 'gheichi'
    print("user: ", choice)
    print("cpu: ", cp)
    if u == c:
        print("mosavi")
        d = d + 1
        r = r + 1
    if u == 1:
        if c == 2:
            print("bakhti")
            l = l + 1
            r = r +1
        if c == 3:
            print("bordi")
            w = w + 1
            r = r +1
    if u == 2:
        if c == 3:
            print("bakhti")
            l = l + 1
            r = r +1
        if c == 1:
            print("bordi")
            w = w + 1
            r = r +1
    if u == 3:
        if c == 1:
            print("bakhti")
            l = l + 1
            r = r +1
        if c == 2:
            print("bordi")
            w = w + 1
            r = r +1
    def result():
        print(r, ' round bazi krdi, ', w, ' round bordi, ', l, 'round bakhti va ', d,' round mosavi kardi :)')
    result()
    bazam = input("Bazam bazi(y/n)? ")
    if bazam == 'y':
        ac = 0
    if bazam == 'n':
        print("bye")
        exit()
