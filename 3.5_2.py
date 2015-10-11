from collections import namedtuple
from pprint import pprint as pp
from math import floor

Stem = namedtuple('Stem', 'data, leafdigits')

data2 = Stem([700, 716, 728, 719, 685, 709, 691, 684, 705, 718,
              706, 715, 712, 722, 691, 708, 690, 692, 707, 701,
              708, 729, 694, 681, 695, 685, 706, 661, 735, 665,
              668, 710, 693, 697, 674, 658, 698, 666, 696, 698,
              706, 692, 691, 747, 699, 682, 698, 700, 710, 722,
              694, 690, 736, 689, 696, 651, 673, 749, 708, 727,
              688, 689, 683, 685, 702, 741, 698, 713, 676, 702,
              701, 671, 718, 707, 683, 717, 733, 712, 683, 692,
              693, 697, 654, 681, 721, 720, 677, 679, 695, 691,
              713, 699, 725, 726, 704, 729, 703, 696, 717, 688], 1.0)


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
    print(stemplot(data2))
