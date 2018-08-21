import pandas


class PrintReport(object):
    def __init__(self):
        pass

    @staticmethod
    def pct_format(inp):
        """ Return a two decimal percent """
        return ('{0:.2f}'.format(inp))

    @staticmethod
    def l_format_3(value, value_count, value_pct):
        return (('{0:3d}   = {1:8d} ({2:.2f}%)').format(value, value_count, value_pct*100))

    @staticmethod
    def l_format_6(value, value_count, value_pct):
        return (('{0:6d}   = {1:8d} ({2:.2f}%)').format(value, value_count, value_pct*100))

    @staticmethod
    def misc_format_pct(value, value_count, value_pct):
        return (('{0:25}   = {1:8d} ({2:05.2f}%)').format(value, value_count, value_pct*100))

    @staticmethod
    def misc_format_pct_short(value, value_count, value_pct):
        return ((' {0:'+str(50)+'} = {1:8d} ({2:05.2f}%)').format(value, value_count, value_pct*100))

    @staticmethod
    def line_fmt1_pct(value, value_count, value_pct, val_fmt="5", val_cnt="8d", pct_fmt="05.2f"):
        return ((' {0:'+str(val_fmt)+'} = {1:'+str(val_cnt)+'} ({2:'+str(pct_fmt)+'}%)').format(value, value_count, value_pct*100))

    @staticmethod
    def misc_format(value, value_count):
        return (('{0:25}   = {1:8d}').format(value, value_count))

    @staticmethod
    def report_header(report_name):
        return ('\n'+'='*60+'\n'+'*'*15+'{0:^30}'.format(report_name)+'*'*15+'\n'+'='*60)

    @staticmethod
    def report_footer(report_name):
        return ("-"*20+'{0:^20}'.format(report_name+" End")+'-'*20+'\n')

    @staticmethod
    def show_indv_report_df(report_name, inp_df, grp_bycol, count_col, tot_count, prn_col1_width):
        print(PrintReport.report_header(report_name))
        for idx, row in inp_df.iterrows():
            print(PrintReport.line_fmt1_pct(
                row[grp_bycol], row[count_col], row[count_col]/tot_count, prn_col1_width))
        print(PrintReport.report_footer(report_name))

    @staticmethod
    def show_indv_report_dict(report_name, inp_dict, tot_count, prn_col1_width):
        print(PrintReport.report_header(report_name))
        for k, v in inp_dict.items():
            print(PrintReport.line_fmt1_pct(k, v, v/tot_count, prn_col1_width))
        print(PrintReport.report_footer(report_name))


if __name__ == '__main__':
    print(PrintReport.report_header('My Report'))
    for i in range(10):
        print(PrintReport.misc_format_pct(str(i*2), i*9284, i*297/678))
