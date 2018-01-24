import os
import json
import strutils
import tables

let dir = getAppDir()

var results = {"updated": 0, "inserted": 0}.toTable

for kind, path in walkDir(dir):
    if endsWith(path, "json"):
        let node = parseFile(path)

        if existsKey(node, "items"):
            for i in node["items"]:
                let res = i["index"]["result"]
                if results.hasKey(getStr(res)):
                    results[getStr(res)] += 1
                else:
                    results[getStr(res)] = 1
echo results
