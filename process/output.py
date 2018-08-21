import pandas

class Summaries(object):
    def __init__(self,pwd_df):
            self.pwd_df=pwd_df
            self.pwd_df=pwd_df[pwd_df['year'] != 0].groupby('year')['passwd'].count()
            self.tot_passwd=pwd_df['passwd'].count()
            self.all_lc=pwd_df['all_lc'].sum()
            self.all_uc=pwd_df['all_uc'].sum()
            self.all_nums=pwd_df['all_nums'].sum()
            self.fc_al=pwd_df['fc_al'].sum()
            self.fc_num=pwd_df['fc_num'].sum()
            self.lc_al=pwd_df['lc_al'].sum()
            self.lc_num=pwd_df['lc_num'].sum()
            self.fc_spchr=pwd_df['fc_spchr'].sum()
            self.lc_spchr=pwd_df['lc_spchr'].sum()
            self.len_le_6=pwd_df['len_le_6'].sum()
            self.len_le_8=pwd_df['len_le_8'].sum()
            self.len_gt_8=pwd_df['len_gt_8'].sum()
            self.cnt_last_digit=pwd_df['last_digit'].count()
            self.cnt_last_2_digits=pwd_df['last_2_digits'].count()
            self.cnt_last_3_digits=pwd_df['last_3_digits'].count()
            self.cnt_last_4_digits=pwd_df['last_4_digits'].count()
            self.year=pwd_df['year'].count()
            self.day_long=pwd_df['day_long'].str.count(r'..*').sum()
            self.day_short=pwd_df['day_short'].str.count(r'..*').sum()
            self.mnth_long=pwd_df['mnth_long'].str.count(r'..*').sum()
            self.mnth_short=pwd_df['mnth_short'].str.count(r'..*').sum()

    def get_all_chars_lc(self):
        return [ self.all_lc,self.all_lc/self.tot_passwd ]

    def get_all_chars_uc(self):
        return [ self.all_uc,self.all_uc/self.tot_passwd ]

    def get_all_nums(self):
        return [ self.all_nums,self.all_nums/self.tot_passwd ]

    def get_fc_num(self):
        return [ self.fc_num,self.fc_num/self.tot_passwd ]
    
    def get_fc_al(self):
        return [ self.fc_al,self.fc_al/self.tot_passwd ]

    def get_lc_num(self):
        return [ self.lc_num,self.lc_num/self.tot_passwd ]
    
    def get_lc_al(self):
        return [ self.lc_al,self.lc_al/self.tot_passwd ]
 
    def get_fc_spchr(self):
        return [ self.fc_spchr,self.fc_spchr/self.tot_passwd ]

    def get_lc_spchr(self):
        return [ self.lc_spchr,self.lc_spchr/self.tot_passwd ]

    def get_len_le_6(self):
        return [ self.len_le_6,self.len_le_6/self.tot_passwd ]

    def get_len_le_8(self):
        return [ self.len_le_8,self.len_le_8/self.tot_passwd ]

    def get_len_gt_8(self):
        return [ self.len_gt_8,self.len_gt_8/self.tot_passwd ]

    def get_last_digit(self):
        return [ self.cnt_last_digit,self.cnt_last_digit/self.tot_passwd ]

    def get_last_2_digits(self):
        return [ self.cnt_last_2_digits,self.cnt_last_2_digits/self.tot_passwd ]

    def get_last_3_digits(self):
        return [ self.cnt_last_3_digits,self.cnt_last_3_digits/self.tot_passwd ]

    def get_last_4_digits(self):
        return [ self.cnt_last_4_digits,self.cnt_last_4_digits/self.tot_passwd ]
