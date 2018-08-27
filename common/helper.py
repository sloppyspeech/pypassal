import re
# def gt_bln(p_inp):
#     return ( True if p_inp != None else False)

class RegexUtil(object):
    #
    def __init__(self, *args, **kwargs):
            pass
    #
    @staticmethod
    def compile_regex(regex):
        return re.compile(regex)