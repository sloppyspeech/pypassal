# pypassal
Password Analyser in Python,is a python implementation for https://github.com/digininja/pipal . 

### Getting Started 
git clone https://github.com/sloppyspeech/pypassal.git

### Prerequisites
*** Works only on Python >= 3.6
```
python -m venv <virtual_env>
source ./<virtual_env>/bin/activate
pip install requirements.txt
mkdir data
```
copy the data file with passwords to be analysed to "data"
```
python pypassal.py ./data/<password_file_name>
```
### Sample Run

```
(ev_pypassal) ╭─ashutosh [ ~/pypassal ] ‹master› 
╰─▶ time python3.6 pypassal.py ./data/passwds.txt
/usr/lib64/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
************************************************************
150000it [00:13, 11010.02it/s]                                                                                                                                
============================================================
***************      Top 20 Base words       ***************
============================================================
 qwerty                              =      150 (00.10%)
 password                            =      116 (00.08%)
 dragon                              =      115 (00.08%)
 silver                              =       87 (00.06%)
 daniel                              =       87 (00.06%)
 summer                              =       86 (00.06%)
 monkey                              =       84 (00.06%)
 master                              =       84 (00.06%)
 shadow                              =       83 (00.06%)
 orange                              =       79 (00.05%)
 thomas                              =       78 (00.05%)
 killer                              =       77 (00.05%)
 hunter                              =       75 (00.05%)
 robert                              =       72 (00.05%)
 andrew                              =       68 (00.05%)
 purple                              =       68 (00.05%)
 football                            =       66 (00.04%)
 alex                                =       65 (00.04%)
 michael                             =       64 (00.04%)
 yellow                              =       63 (00.04%)
--------------------Top 20 Base words End--------------------


============================================================
***************        Top Passwords         ***************
============================================================
 !@#$%^&*                            =        1 (00.00%)
 philoctetes                         =        1 (00.00%)
 phillip1                            =        1 (00.00%)
 phillip2                            =        1 (00.00%)
 phillip3                            =        1 (00.00%)
 phillipa                            =        1 (00.00%)
 phillipe                            =        1 (00.00%)
 phillipi                            =        1 (00.00%)
 phillipines                         =        1 (00.00%)
 phillipo                            =        1 (00.00%)
 phillipp                            =        1 (00.00%)
 phillippa                           =        1 (00.00%)
 phillippe                           =        1 (00.00%)
 phillips                            =        1 (00.00%)
 phillips1                           =        1 (00.00%)
 philmont                            =        1 (00.00%)
 philmore                            =        1 (00.00%)
 phillies1                           =        1 (00.00%)
 phillies                            =        1 (00.00%)
 phillida                            =        1 (00.00%)
-------------------- Top Passwords End  --------------------


============================================================
***************        Year Breakdown        ***************
============================================================
 1970   =       35 (00.02%)
 1971   =       50 (00.03%)
 1972   =       46 (00.03%)
 1973   =       75 (00.05%)
 1974   =      110 (00.07%)
 1975   =      120 (00.08%)
 1976   =      137 (00.09%)
 1977   =      200 (00.13%)
 1978   =      200 (00.13%)
 1979   =      210 (00.14%)
 1980   =      301 (00.20%)
 1981   =      302 (00.20%)
 1982   =      339 (00.23%)
 1983   =      330 (00.22%)
 1984   =      370 (00.25%)
 1985   =      349 (00.23%)
 1986   =      350 (00.23%)
 1987   =      373 (00.25%)
 1988   =      370 (00.25%)
 1989   =      365 (00.24%)
 1990   =      372 (00.25%)
 1991   =      350 (00.23%)
 1992   =      354 (00.24%)
 1993   =      326 (00.22%)
 1994   =      292 (00.19%)
 1995   =      237 (00.16%)
 1996   =      157 (00.10%)
 1997   =      122 (00.08%)
 1998   =       96 (00.06%)
 1999   =       55 (00.04%)
 2000   =      247 (00.16%)
 2001   =       48 (00.03%)
 2002   =       45 (00.03%)
 2003   =       47 (00.03%)
 2004   =       36 (00.02%)
 2005   =       63 (00.04%)
 2006   =       44 (00.03%)
 2007   =       57 (00.04%)
 2008   =       53 (00.04%)
 2009   =       43 (00.03%)
 2010   =       36 (00.02%)
 2011   =       14 (00.01%)
 2012   =       22 (00.01%)
 2013   =        3 (00.00%)
 2014   =        3 (00.00%)
 2015   =        3 (00.00%)
 2016   =        1 (00.00%)
 2017   =        1 (00.00%)
 2018   =        2 (00.00%)
 2019   =        3 (00.00%)
 2020   =        5 (00.00%)
 2021   =       19 (00.01%)
 2022   =        3 (00.00%)
 2023   =        3 (00.00%)
 2024   =        2 (00.00%)
-------------------- Year Breakdown End --------------------


============================================================
*************** Breakdown By Password Length ***************
============================================================
     8 =    77589 (51.73%)
     9 =    30118 (20.08%)
    10 =    19336 (12.89%)
    11 =    10168 (06.78%)
    12 =     6264 (04.18%)
    13 =     3499 (02.33%)
    14 =     1927 (01.28%)
    15 =      747 (00.50%)
    16 =      239 (00.16%)
    17 =       63 (00.04%)
    18 =       26 (00.02%)
    20 =       12 (00.01%)
    19 =       10 (00.01%)
    26 =        2 (00.00%)
--------------------Breakdown By Password Length End--------------------


============================================================
***************     Break By Last Digit      ***************
============================================================
 1     =     7132 (04.75%)
 3     =     4353 (02.90%)
 2     =     3212 (02.14%)
 0     =     2280 (01.52%)
 4     =     2268 (01.51%)
 7     =     2149 (01.43%)
 9     =     2148 (01.43%)
 5     =     2010 (01.34%)
 6     =     1880 (01.25%)
 8     =     1782 (01.19%)
--------------------Break By Last Digit End--------------------


============================================================
***************       Day Abbreviated        ***************
============================================================
 mon   =     1418 (00.95%)
 sun   =      282 (00.19%)
 sat   =      265 (00.18%)
 fri   =      260 (00.17%)
 wed   =       90 (00.06%)
 tue   =       21 (00.01%)
 thurs =        8 (00.01%)
--------------------Day Abbreviated End --------------------


============================================================
***************        Day Full Name         ***************
============================================================
 monday          =       11 (00.01%)
 friday          =        9 (00.01%)
 sunday          =        6 (00.00%)
 saturday        =        4 (00.00%)
 thursday        =        4 (00.00%)
 wednesday       =        4 (00.00%)
 tuesday         =        3 (00.00%)
-------------------- Day Full Name End  --------------------


============================================================
***************      Month Abbreviated       ***************
============================================================
 mar   =     1561 (01.04%)
 dec   =      379 (00.25%)
 sep   =      229 (00.15%)
 nov   =      205 (00.14%)
 aug   =      185 (00.12%)
 oct   =      176 (00.12%)
 jan   =      154 (00.10%)
 jun   =      144 (00.10%)
 apr   =      102 (00.07%)
 jul   =       70 (00.05%)
 may   =       69 (00.05%)
 feb   =       20 (00.01%)
--------------------Month Abbreviated End--------------------


============================================================
***************       Month Long Name        ***************
============================================================
 may             =       69 (00.05%)
 august          =       65 (00.04%)
 december        =       41 (00.03%)
 october         =       41 (00.03%)
 june            =       36 (00.02%)
 january         =       35 (00.02%)
 november        =       35 (00.02%)
 september       =       31 (00.02%)
 march           =       30 (00.02%)
 april           =       16 (00.01%)
 july            =       12 (00.01%)
 february        =        4 (00.00%)
--------------------Month Long Name End --------------------


============================================================
***************           Over All           ***************
============================================================
Total Passwords             =   150000
All Chars Lower Case        =   138122 (92.08%)
All Chars Upper Case        =      209 (00.14%)
All Numbers                 =    10001 (06.67%)
First Char Number           =    10827 (07.22%)
First Char AlphaNum         =   139160 (92.77%)
Last Char Number            =    29214 (19.48%)
Last Char AlphaNum          =   120746 (80.50%)
First Char Special Char     =       13 (00.01%)
Last Char Special Char      =       40 (00.03%)
Length Less than eq 6       =        0 (00.00%)
Length Less than eq 8       =    77589 (51.73%)
Length greater than 8       =    72411 (48.27%)
Single Digit at the end     =    29214 (19.48%)
Two Digits at the end       =    22504 (15.00%)
Three Digits at the end     =    14801 (09.87%)
Four Digits at the end      =    11834 (07.89%)
--------------------    Over All End    --------------------


============================================================
***************    Character Composition     ***************
============================================================
 e     =   132077 (88.05%)
 a     =   115507 (77.00%)
 i     =   100658 (67.11%)
 r     =    91499 (61.00%)
 n     =    88090 (58.73%)
 o     =    86257 (57.50%)
 s     =    80623 (53.75%)
 t     =    80559 (53.71%)
 l     =    71070 (47.38%)
 c     =    49838 (33.23%)
 d     =    40217 (26.81%)
 u     =    40089 (26.73%)
 m     =    39253 (26.17%)
 h     =    34372 (22.91%)
 p     =    32106 (21.40%)
 1     =    31869 (21.25%)
 g     =    29039 (19.36%)
 b     =    25809 (17.21%)
 y     =    21971 (14.65%)
 k     =    16434 (10.96%)
 2     =    16415 (10.94%)
 0     =    16069 (10.71%)
 f     =    15660 (10.44%)
 9     =    15329 (10.22%)
 v     =    13669 (09.11%)
 w     =    12753 (08.50%)
 3     =    10212 (06.81%)
 8     =     8837 (05.89%)
 7     =     6896 (04.60%)
 4     =     6735 (04.49%)
 5     =     6469 (04.31%)
 6     =     6018 (04.01%)
 z     =     4932 (03.29%)
 j     =     4262 (02.84%)
 x     =     3768 (02.51%)
 q     =     2737 (01.82%)
 A     =      351 (00.23%)
 S     =      265 (00.18%)
 C     =      251 (00.17%)
 E     =      196 (00.13%)
 M     =      195 (00.13%)
 R     =      188 (00.13%)
 P     =      169 (00.11%)
 I     =      169 (00.11%)
 N     =      160 (00.11%)
 L     =      151 (00.10%)
 B     =      146 (00.10%)
 T     =      141 (00.09%)
 D     =      135 (00.09%)
 H     =      125 (00.08%)
 O     =      110 (00.07%)
 G     =      108 (00.07%)
 F     =      100 (00.07%)
 W     =       72 (00.05%)
 K     =       65 (00.04%)
 J     =       54 (00.04%)
 V     =       50 (00.03%)
 -     =       50 (00.03%)
 Q     =       39 (00.03%)
 U     =       36 (00.02%)
 .     =       36 (00.02%)
 *     =       33 (00.02%)
 Z     =       27 (00.02%)
 Y     =       24 (00.02%)
 !     =       19 (00.01%)
 @     =       18 (00.01%)
 '     =       16 (00.01%)
 $     =       15 (00.01%)
 ?     =       11 (00.01%)
 X     =        9 (00.01%)
 _     =        9 (00.01%)
 ;     =        5 (00.00%)
 #     =        3 (00.00%)
 &     =        3 (00.00%)
 ,     =        2 (00.00%)
 %     =        2 (00.00%)
 ^     =        2 (00.00%)
 /     =        1 (00.00%)
 =     =        1 (00.00%)
 [     =        1 (00.00%)
 ]     =        1 (00.00%)
 (     =        1 (00.00%)
 )     =        1 (00.00%)
 +     =        1 (00.00%)
--------------------Character Composition End--------------------


```
