from collections import OrderedDict
from collections import defaultdict
from pathlib import Path

#if there exists a parent then search it othewise return value
def search(dir, key):
    for k in dir:
        if key + '/' in k and len(('/').split(key)) == len(('/').split(k)) + 1: # this finds grandparents instead of just parents
            dir[key] += search(dir, k)
            #print(key, dir[key] , k)
    #print('*', end="")
    return dir[key]

def p1(input):
    dir = OrderedDict('')
    key = []

    for line in input:
        match line.split():
            case ['$', 'cd', id]:
                if id == "..":
                    key.pop()
                else:
                    key.append(id)
                    dir["/".join(key)] = 0
            case [i, id] if i.isnumeric():
                dir["/".join(key)] = dir.get("/".join(key), 0) + int(i)
    print(dir)

    search(dir, '/')
    sum = 0
    for k in dir:
        val = dir[k]
        if val <= 100000:
            sum += dir[k]

    print(dir)
    return sum

def p3(f):
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

def p2(input):
    return
with open('input.txt', 'r') as f:
    print(p3(f))
with open('input.txt', 'r') as f:
    items = [line.replace("\n", "") for line in f]
    print(p1(items))
    print("1582412")

