#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # write layout's config
    os.system("rc-update add bluetooth default")
