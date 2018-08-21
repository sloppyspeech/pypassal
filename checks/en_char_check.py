import collections as cll
import re as rgx

class CharCheck(object):

    char_counter=cll.defaultdict(int)

    def __init__(self,p_passwd):
        self.passwd=str(p_passwd)
        self.pwdlen=len(self.passwd)
    
    def are_all_nums(self):
        return self.passwd.isdigit()
    
    def is_fc_num(self):
        return self.passwd[0].isdigit()
    
    def is_lc_num(self):
        return self.passwd[-1].isdigit()
    
    def are_all_lc(self):
        return self.passwd.islower()
    
    def are_all_uc(self):
        return self.passwd.isupper()
    
    def is_fc_al(self):
        return (self.passwd[0].isalnum() == True and  self.passwd[0].isdigit() == False )
    
    def is_lc_al(self):
        return (self.passwd[-1].isalnum() == True and  self.passwd[-1].isdigit() == False )

    def is_lc_spchr(self):
        return (self.passwd[-1].isalnum() == False and  self.passwd[-1].isdigit() == False )
        
    def is_fc_spchr(self):
        return (self.passwd[0].isalnum() == False and  self.passwd[0].isdigit() == False )
    
    def len_le_6 (self):
        return self.pwdlen <=6
    
    def len_le_8 (self):
        return self.pwdlen <=8

    def len_gt_8 (self):
        return self.pwdlen >8
    
    def get_lst_dgts(self,dlen):
        drgx=rgx.search(rgx.compile('(\d){'+str(dlen)+'}$'),self.passwd)
        return drgx.group() if drgx else None
