from collections import defaultdict
from pathlib import Path


def p1(f):
    cwd = Path("/")
    dirs = defaultdict(int)

    for line in f.read().splitlines():
        match line.split():
            case ["$", "cd", newdir]:
                cwd = cwd / newdir
                cwd = cwd.resolve()
            case [size, _] if size.isdigit():
                size = int(size)
                for path in [cwd, *cwd.parents]:
                    dirs[path] += size
    print(dirs)
    return sum(x for x in dirs.values() if x <= 100000)


def p2(f):
    cwd = Path("/")
    dirs = defaultdict(int)

    for line in f.read().splitlines():
        match line.split():
            case ["$", "cd", newdir]:
                cwd = cwd / newdir
                cwd = cwd.resolve()
            case [size, _] if size.isdigit():
                size = int(size)
                for path in [cwd, *cwd.parents]:
                    dirs[path] += size

    return min(x for x in dirs.values() if dirs[Path("/")] - x <= 70000000 - 30000000)

with open('input.txt', 'r') as f:
    print(p1(f))
