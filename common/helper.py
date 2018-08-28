import re

class RegexUtil(object):
    #
    def __init__(self, *args, **kwargs):
            pass
    #
    @staticmethod
    def compile_regex(regex):
        return re.compile(regex)
