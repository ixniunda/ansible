#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)
from ansible import errors
__metaclass__ = type


def my_filter1(arg, os_family, os_release, mongodb_version):


    if os_family == "Fedora":
        temp_os = "Fedora"
        os_family = "rhel"

    for i in range(len(arg)):
        if ((os_family + os_release) in arg[i]) and (
                mongodb_version in arg[i]):
            return "Required OS version: " + temp_os + ", Release number: " + \
                os_release + ", mongodb version: " + mongodb_version + \
                ".  MongoDB release :  " + arg[i]


class FilterModule(object):
    def filters(self):
        return {
            'get_mongo_src': my_filter1
        }

