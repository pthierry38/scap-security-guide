#!/usr/bin/python

"""
release.py: Get back the upstream releaseNotes to generate the correponsing
ChangeLog file
"""

import codecs
import json
import re
import subprocess
import requests

__author__ = "P. Thierry"
__license__ = "GPL2+"
__version__ = "1.0"
__maintainer__ = "P. Thierry"
__email__ = "phil@reseau-libre.net"

CMD = 'dpkg-parsechangelog -l debian/changelog -S Version'
BASEURL = 'https://api.github.com/repos/OpenSCAP/scap-security-guide/releases/tags/v'

# runing subprocess and waiting for its end
P = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
(STDOUT, STDERR) = P.communicate()
P_STATUS = P.wait()

# cleaning Debian subversion
VERSION = re.sub(r"-.+$", "", STDOUT)

# loading the current version ReleaseNote.md from Github
print 'Loading ReleaseNotes from ' + BASEURL + VERSION
R = requests.get(BASEURL + VERSION)
if R.ok:
    REPOITEM = json.loads(R.text or R.content)
    with codecs.open("changelog", "w", "utf-8") as ch:
        ch.write("# scap-security-guide" + " " + REPOITEM['tag_name'] + "\r\n")
        ch.write("\r\n")
        ch.write(REPOITEM['body'])
else:
    print "error loading request: got " + str(R.status_code)
