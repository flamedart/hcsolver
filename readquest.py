#!/usr/bin/env python3.4

def parseHeader(fileName, nameList):
    with open(fileName, "r") as f:
        s = f.readline().split()
        vals = [int(x) for x in s]
    # print(s, len(vals), len(nameList))
    assert len(vals) == len(nameList)
    return dict(zip(nameList, vals))

def parseFile(fileName, skipNumOfHeaderLines):
    data = []
    with open(fileName, "r") as f:
        f.readlines(skipNumOfHeaderLines)
        for line in f:
            s = line.split()
            # SAME as: data.append(list(map(float, s)))
            data.append([int(x) for x in s])
    return data

if __name__ == "__main__":
    h = parseHeader("a_example.in", ["v1", "v2", "v3", "v4", "v5", "v6"])
    print(h, h['v2'])
    for d in parseFile("a_example.in", 1):
        print(d)
