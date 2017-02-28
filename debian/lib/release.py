#!/usr/bin/python

import requests
import codecs
import json

r = requests.get('https://api.github.com/repos/OpenSCAP/scap-security-guide/releases/tags/v0.1.31')
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    with codecs.open("changelog", "w", "utf-8") as file:
        file.write("# scap-security-guide" + " " + repoItem['tag_name'] + "\r\n")
        file.write("\r\n")
        file.write(repoItem['body'])
