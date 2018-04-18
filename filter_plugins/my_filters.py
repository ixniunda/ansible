#!/usr/bin/env python


class FilterModule(object):
    def filters(self):
        return {
            'a_filter': self.a_filter,
##            'another_filter': self.b_filter
        }


    def a_filter(self, a_variable):
        a_new_variable = a_variable + ' CRAZY NEW FILTER'
        return a_new_variable
