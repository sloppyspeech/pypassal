import sys
import pandas as pd
import memory_profiler
import argparse
import os
import collections as colls
from tqdm import tqdm

from checks import en_char_check as ec
from checks import en_date_check as dc
from common import helper as hp
from process import output as op
from common import print_report as prn


def show_overall_report():
    pass


def show_report(my_df, passwd_count, char_count):

    year_df = my_df[my_df['year'] != 0].groupby(
        'year')['passwd'].size().reset_index(name='counts').sort_values(by='year')
    #
    top_passwds = pd.DataFrame(my_df.groupby('passwd', as_index=False).size(
    ).reset_index(name='counts').sort_values(by='counts', ascending=False))
    #
    pwdlen_df = my_df[my_df['pwdlen'] != 0].groupby('pwdlen')['passwd'].count(
    ).to_frame().reset_index().sort_values(by='passwd', ascending=False)
    #
    last_digit_df = my_df[my_df['last_digit'] != None].groupby('last_digit')['passwd'].count(
    ).to_frame().reset_index().sort_values(by='passwd', ascending=False)
    #
    day_long_df = my_df[my_df['day_long'] != ''].groupby('day_long')['passwd'].count(
    ).to_frame().reset_index().sort_values(by='passwd', ascending=False)
    #
    day_short_df = my_df[my_df['day_short'] != ''].groupby('day_short')['passwd'].count(
    ).to_frame().reset_index().sort_values(by='passwd', ascending=False)
    #
    mnth_short_df = my_df[my_df['mnth_short'] != ''].groupby('mnth_short')['passwd'].count(
    ).to_frame().reset_index().sort_values(by='passwd', ascending=False)
    #
    mnth_long_df = my_df[my_df['mnth_long'] != ''].groupby('mnth_long')['passwd'].count(
    ).to_frame().reset_index().sort_values(by='passwd', ascending=False)
    #
    # Form basewords
    data_df=my_df['passwd'].to_frame().reset_index()
    data_df['passwd1']= my_df['passwd'].str.replace(r'[^a-zA-Z]*$','').to_frame()
    data_df['passwd2']= data_df['passwd1'].str.replace(r'^[^a-zA-Z]*','').to_frame()
    baseword_df=data_df[data_df['passwd2']!=''].groupby('passwd2')['index'].count().reset_index().sort_values(by='index',ascending=False)
    baseword_df.columns=['passwd','counts']
    #
    prn.PrintReport.show_indv_report_df(
        "Top 20 Base words", baseword_df[0:20], "passwd", "counts", passwd_count, 35)
    #
    prn.PrintReport.show_indv_report_df(
        "Top Passwords", top_passwds[0:20], "passwd", "counts", passwd_count, 35)
    #
    prn.PrintReport.show_indv_report_df(
        "Year Breakdown", year_df, "year", "counts", passwd_count, 6)
    #
    prn.PrintReport.show_indv_report_df(
        "Breakdown By Password Length", pwdlen_df, "pwdlen", "passwd", passwd_count, 5)
    #
    prn.PrintReport.show_indv_report_df(
        "Break By Last Digit", last_digit_df, "last_digit", "passwd", passwd_count, 5)
    #
    prn.PrintReport.show_indv_report_df(
        "Day Abbreviated", day_short_df, "day_short", "passwd", passwd_count, 5)
    #
    prn.PrintReport.show_indv_report_df(
        "Day Full Name", day_long_df, "day_long", "passwd", passwd_count, 15)
    #
    prn.PrintReport.show_indv_report_df(
        "Month Abbreviated", mnth_short_df, "mnth_short", "passwd", passwd_count, 5)
    #
    prn.PrintReport.show_indv_report_df(
        "Month Long Name", mnth_long_df, "mnth_long", "passwd", passwd_count, 15)
    #
    smry = op.Summaries(my_df)
    print(prn.PrintReport.report_header("Over All"))
    print(prn.PrintReport.misc_format('Total Passwords', passwd_count))
    print(prn.PrintReport.misc_format_pct('All Chars Lower Case',
                                          smry.get_all_chars_lc()[0], smry.get_all_chars_lc()[1]))
    print(prn.PrintReport.misc_format_pct('All Chars Upper Case',
                                          smry.get_all_chars_uc()[0], smry.get_all_chars_uc()[1]))
    print(prn.PrintReport.misc_format_pct('All Numbers',
                                          smry.get_all_nums()[0], smry.get_all_nums()[1]))
    print(prn.PrintReport.misc_format_pct('First Char Number',
                                          smry.get_fc_num()[0], smry.get_fc_num()[1]))
    print(prn.PrintReport.misc_format_pct(
        'First Char AlphaNum', smry.get_fc_al()[0], smry.get_fc_al()[1]))
    print(prn.PrintReport.misc_format_pct('Last Char Number',
                                          smry.get_lc_num()[0], smry.get_lc_num()[1]))
    print(prn.PrintReport.misc_format_pct(
        'Last Char AlphaNum', smry.get_lc_al()[0], smry.get_lc_al()[1]))
    print(prn.PrintReport.misc_format_pct('First Char Special Char',
                                          smry.get_fc_spchr()[0], smry.get_fc_spchr()[1]))
    print(prn.PrintReport.misc_format_pct('Last Char Special Char',
                                          smry.get_lc_spchr()[0], smry.get_lc_spchr()[1]))
    print(prn.PrintReport.misc_format_pct('Length Less than eq 6',
                                          smry.get_len_le_6()[0], smry.get_len_le_6()[1]))
    print(prn.PrintReport.misc_format_pct('Length Less than eq 8',
                                          smry.get_len_le_8()[0], smry.get_len_le_8()[1]))
    print(prn.PrintReport.misc_format_pct('Length greater than 8',
                                          smry.get_len_gt_8()[0], smry.get_len_gt_8()[1]))
    print(prn.PrintReport.misc_format_pct('Single Digit at the end',
                                          smry.get_last_digit()[0], smry.get_last_digit()[1]))
    print(prn.PrintReport.misc_format_pct('Two Digits at the end',
                                          smry.get_last_2_digits()[0], smry.get_last_2_digits()[1]))
    print(prn.PrintReport.misc_format_pct('Three Digits at the end',
                                          smry.get_last_3_digits()[0], smry.get_last_3_digits()[1]))
    print(prn.PrintReport.misc_format_pct('Four Digits at the end',
                                          smry.get_last_4_digits()[0], smry.get_last_4_digits()[1]))
    print(prn.PrintReport.report_footer("Over All"))
    #
    my_new_df=pd.Series(ec.CharCheck.char_counter).to_frame()
    my_new_df['char']=my_new_df.index
    my_new_df.columns=['count','characters']
    my_new_df=my_new_df.sort_values(by='count',ascending=False)
    prn.PrintReport.show_indv_report_df(
        "Top 100 Characters in Password", my_new_df[0:100], "characters", "count", char_count, 10)
    #


def main_pds_process(inp_file, file_num_lines):
    u_passwd = []
    char_counter = 0
    passwd_counter = 0
    with open(inp_file, encoding='utf8', errors='ignore') as pwd_fil:
        for line in tqdm(pwd_fil, total=file_num_lines):
            if len(line.strip()) > 0:
                inp_passwd = line.strip()
                passwd_counter += 1
                for c in inp_passwd:
                    ec.CharCheck.char_counter[c] = ec.CharCheck.char_counter[c]+1
                    char_counter += 1
                i_cc = ec.CharCheck(inp_passwd)
                i_dc = dc.DateCheck(inp_passwd)
                #
                inp_chrchk_props = [i_cc.passwd, i_cc.pwdlen, i_cc.are_all_lc(),
                                    i_cc.are_all_uc(), i_cc.are_all_nums(),
                                    i_cc.is_fc_al(), i_cc.is_fc_num(),
                                    i_cc.is_lc_al(), i_cc.is_lc_num(),
                                    i_cc.is_fc_spchr(), i_cc.is_lc_spchr(),
                                    i_cc.len_le_6(), i_cc.len_le_8(), i_cc.len_gt_8(),
                                    i_cc.get_lst_dgts(1), i_cc.get_lst_dgts(2),
                                    i_cc.get_lst_dgts(3), i_cc.get_lst_dgts(4)
                                    ]
                inp_datechk_props = [i_dc.get_year(),
                                     i_dc.get_day_long(), i_dc.get_day_short(),
                                     i_dc.get_mnth_long(), i_dc.get_mnth_short()
                                     ]
                #
                u_passwd.append(inp_chrchk_props+inp_datechk_props)
                inp_chrchk_props = []
                inp_datechk_props = []
    #print(u_passwd)
    col_list = ['passwd', 'pwdlen', 'all_lc', 'all_uc', 'all_nums', 'fc_al', 'fc_num',
                'lc_al', 'lc_num', 'fc_spchr', 'lc_spchr',
                'len_le_6', 'len_le_8', 'len_gt_8',
                'last_digit', 'last_2_digits', 'last_3_digits', 'last_4_digits',
                'year', 'day_long', 'day_short', 'mnth_long', 'mnth_short'
                ]

    show_report(pd.DataFrame(u_passwd, columns=col_list),
                passwd_counter, char_counter)


if __name__ == '__main__':
    argPrs = argparse.ArgumentParser()
    argPrs.add_argument('inp_file', help=' Input File Name ',)
    args = argPrs.parse_args()
    try:
        file_num_lines = round(os.stat(args.inp_file).st_size/10.5)
    except:
        print("Input File doesn't Exists or is empty ")
        exit(1)
    #
    print("*"*60)
    main_pds_process(args.inp_file, file_num_lines)
