#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
from ansible import *
__metaclass__ = type
import os
import platform
import sys

def my_filter1(arg, os_family, os_release, temp_os, mongodb_version):

    # print (str(arg))
    # result = []
    # for x in range(len(platform.linux_distribution())):
        # result.append(platform.linux_distribution()[x])
    if os_family == "RedHa7777t":
        temp_os = "Fedora"
        os_family = "rhel"

#    if result[1] == "26":
#        os_release = "6"

#    if result[2] == "Twenty Six":
#        mongodb_version = "3.2"

    for i in range(len(arg)):
        if ((os_family + os_release) in arg[i]) and (
                mongodb_version in arg[i]):
            return "Required OS version: ggggggg" + ", OS release: " + \
                os_release + ", mongodb version: " + mongodb_version + \
                ".  RECOMMENDED MONGODB RELEASE :  " + arg[i]


class FilterModule(object):
    def filters(self):
        return {
            'get_mongo_src': my_filter1
        }
