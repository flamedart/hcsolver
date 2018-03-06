#!/usr/bin/env python3.4

def parseHeader(fileName, nameList):
    with open(fileName, "r") as f:
        s = f.readlines(1)[0].split()
        vals = [float(x) for x in s]
    # print(s, len(vals), len(nameList))
    assert len(vals) == len(nameList)
    d = dict()
    for i in range(0, len(nameList)):
        d[nameList[i]] = vals[i]
    return d

def parseFile(fileName, skipNumOfHeaderLines):
    data = []
    with open(fileName, "r") as f:
        f.readlines(skipNumOfHeaderLines)
        for line in f:
            s = line.split()
            # SAME as: data.append(list(map(float, s)))
            data.append([float(x) for x in s])
    return data

if __name__ == "__main__":
    h = parseHeader("a_example.in", ["v1", "v2", "v3", "v4", "v5", "v6"])
    print(h, h['v2'])
    for d in parseFile("a_example.in", 1):
        print(d)
