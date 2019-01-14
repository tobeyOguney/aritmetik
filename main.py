def mystify(number, *mods):
    ans = list()
    for num in mods:
        ans.append(number%num)
    return ans

def demystify(lis, *mods):
    res = solveCongruences(lis, mods)
    return res['value']

def gcdExtra(a, b):
    aO, bO = a, b
    x=lasty=0
    y=lastx=1
    while (b!=0):
        q= int(a/b)
        a, b = b, a%b
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y
    return {
        "x": lastx,
        "y": lasty,
        "gcd": aO * lastx + bO * lasty
    }

def solveCongruences(rests, modulos):
    assert len(rests) == len(modulos)
    x = 0
    M = 1
    for num in modulos:
        M *= num

    for mi, resti in zip(modulos, rests):
        Mi = int(M / mi)
        s = gcdExtra(Mi, mi)["x"]
        e = s * Mi
        x += resti * e
    return {"value": ((x % M) + M) % M, "modulo": M}

def do(x, y, operator='+'):
    mods = [99, 98, 97, 95]
    assert x < 99*98*97*95
    assert y < 99*98*97*95
    a = mystify(x, *mods)
    b = mystify(y, *mods)
    res = list()
    for i in range(len(mods)):
        res.append(eval('%d %s %d'%(a[i], operator, b[i]))%mods[i])
    return demystify(res, 99, 98, 97, 95)