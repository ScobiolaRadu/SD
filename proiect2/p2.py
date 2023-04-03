from random import randrange
from bisect import bisect_right
from bisect import bisect_left

class Nod:
    def __init__(self, data, prioritate=100, st=None, dr=None):
        self.data = data
        self.prioritate = randrange(prioritate)
        self.st = st
        self.dr = dr

def rotatieSt(radacina):
    R = radacina.dr
    X = radacina.dr.st
    R.st = radacina
    radacina.dr = X
    return R

def rotatieDr(radacina):
    L = radacina.st
    Y = radacina.st.dr
    L.dr = radacina
    radacina.st = Y
    return L

def inserareNod(radacina, data):
    if radacina is None:
        return Nod(data)
    if data < radacina.data:
        radacina.st = inserareNod(radacina.st, data)
        if radacina.st and radacina.st.prioritate > radacina.prioritate:
            radacina = rotatieDr(radacina)
    else:
        radacina.dr = inserareNod(radacina.dr, data)
        if radacina.dr and radacina.dr.prioritate > radacina.prioritate:
            radacina = rotatieSt(radacina)
    return radacina

def cautaNod(radacina, cheie):
    if radacina is None:
        return False
    if radacina.data == cheie:
        return True
    if cheie < radacina.data:
        return cautaNod(radacina.st, cheie)
    return cautaNod(radacina.dr, cheie)

def stergeNod(radacina, cheie):
    if radacina is None:
        return None
    if cheie < radacina.data:
        radacina.st = stergeNod(radacina.st, cheie)
    elif cheie > radacina.data:
        radacina.dr = stergeNod(radacina.dr, cheie)
    else:
        if radacina.st is None and radacina.dr is None:
            radacina = None
        elif radacina.st and radacina.dr:
            if radacina.st.prioritate < radacina.dr.prioritate:
                radacina = rotatieSt(radacina)
                radacina.st = stergeNod(radacina.st, cheie)
            else:
                radacina = rotatieDr(radacina)
                radacina.dr = stergeNod(radacina.dr, cheie)
        else:
            frunza = radacina.st if (radacina.st) else radacina.dr
            radacina = frunza
    return radacina


f = open("abce.in")
g = open("abce.out", "w")
Q = int(f.readline())
keys = []
rad = None
for i in range(Q):
    x = f.readline().split()
    comanda = int(x[0])
    if comanda == 1:
        rad = inserareNod(rad, int(x[1]))
        keys.append(int(x[1]))
    elif comanda == 2:
        rad = stergeNod(rad, int(x[1]))
        keys.remove(int(x[1]))
    elif comanda == 3:
        k = cautaNod(rad, int(x[1]))
        if k is False:
            g.write("0\n")
        else:
            g.write("1\n")
    elif comanda == 4:
             a = int(x[1])
             keys.sort()
             maxi = keys[bisect_left(keys, a)-1]
             g.write(str(maxi) + "\n")
    elif comanda == 5:
        a = int(x[1])
        keys.sort()
        mini = keys[bisect_right(keys, a)]
        g.write(str(mini) + "\n")
    elif comanda == 6:
        a = int(x[1])
        b = int(x[2])
        keys.sort()
        for i in range(a, b+1):
            if i in keys:
                g.write(str(i) + " ")
        g.write("\n")
