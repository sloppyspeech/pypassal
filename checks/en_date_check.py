import re as rgx

class DateCheck(object):
    days_long=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
    #
    days_short=('mon','tue','wed','thurs','fri','sat','sun')
    #
    mnth_long=('january', 'february', 'march', 'april', 'may', 'june',\
               'july', 'august', 'september', 'october', 'november', 'december')
    #
    mnth_short=('jan', 'feb', 'mar', 'apr', 'may', 'jun',\
               'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
    #
    years=set([str(year) for year in range(1970,2025)])
    #
    def __init__(self,p_passwd):
            self.passwd=str(p_passwd).lower()
    
    @property
    def get_day_long(self):
        for day in self.days_long:
            if rgx.search(day,self.passwd):
                return day
        else:
            return ''

    @property
    def get_day_short(self):
        for day in self.days_short:
            if rgx.search(day,self.passwd):
                return day
        else:
            return ''

    @property
    def get_mnth_long(self):
        for mnth in self.mnth_long:
            if rgx.search(mnth,self.passwd):
                return mnth
        else:
            return ''
    
    @property
    def get_mnth_short(self):
        for mnth in self.mnth_short:
            if rgx.search(mnth,self.passwd):
                return mnth
        else:
            return ''
    
    @property
    def get_year(self):
        for year in self.years:
            if rgx.search(year,self.passwd):
                return year
        else:
            return 0
    


if __name__=='__main__':
    mydat=DateCheck("324023948@")
    print(mydat.get_day_long)
    print(mydat.get_day_short)
    print(mydat.get_mnth_long)
    print(mydat.get_mnth_short)
    print(mydat.get_year)
   