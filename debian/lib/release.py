#!/usr/bin/python

import requests
import json

r = requests.get('https://api.github.com/repos/OpenSCAP/scap-security-guide/releases/tags/v0.1.31')
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    print "# scap-security-guide" + " " + repoItem['tag_name']
    print ""
    print repoItem['body']
