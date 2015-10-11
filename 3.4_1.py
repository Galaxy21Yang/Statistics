from collections import namedtuple
from pprint import pprint as pp
from math import floor

Stem = namedtuple('Stem', 'data, leafdigits')

data1 = Stem((57, 29, 29, 36, 31,
              23, 47, 23, 28, 28,
              35, 51, 39, 18, 46,
              18, 26, 50, 29, 33,
              21, 46, 41, 52, 18,
              21, 43, 19, 42, 20), 1.0)


def stemplot(stem):
    d = []
    interval = int(10**int(stem.leafdigits))
    for data in sorted(stem.data):
        data = int(floor(data))
        stm, lf = divmod(data, interval)
        d.append((int(stm), int(lf)))
    stems, leafs = list(zip(*d))
    stemwidth = max(len(str(x)) for x in stems)
    leafwidth = max(len(str(x)) for x in leafs)
    laststem, out = min(stems) - 1, []
    for s, l in d:
        while laststem < s:
            laststem += 1
            out.append('\n%*i |' % (stemwidth, laststem))
        out.append(' %0*i' % (leafwidth, l))
    return ''.join(out)

if __name__ == '__main__':
    print(stemplot(data1))
