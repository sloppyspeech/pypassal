[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/sloppyspeech/pypassal/blob/master/LICENSE)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

# pypassal
Password Analyser in Python,is a python implementation for https://github.com/digininja/pipal . 

## Author 
SloppySpeech (https://github.com/sloppyspeech)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to https://github.com/digininja/pipal
* Inspiration https://github.com/digininja/pipal 
* Really Really Inspired from https://github.com/digininja/pipal 

### Lets Do IT
*** Tested only on python3.6

Make sure python points to alteast python3.6 on Linux/MacOS/Unix

Create Virtual Env and install the required packages/modules


```
git clone https://github.com/sloppyspeech/pypassal.git
cd pypassal
python -m venv ev_pypassal
source ./ev_pypassal/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
Create a data directory,download and extract the test file
```
mkdir data
cd data
wget http://downloads.skullsecurity.org/passwords/phpbb.txt.bz2
bzip2 -dk phpbb.txt.bz2
cd ..
```
### Sample Run

```

================================================================================
                              Password Analyser
================================================================================
 Press CTRL+C to cancel anytime 
================================================================================

184389it [00:18, 10206.61it/s]                                                                                                                                

============================================================
***************      Top 20 Base words       ***************
============================================================
 phpbb                               =      293 (00.16%)
 a                                   =      282 (00.15%)
 php                                 =      124 (00.07%)
 b                                   =      122 (00.07%)
 c                                   =       96 (00.05%)
 d                                   =       88 (00.05%)
 m                                   =       85 (00.05%)
 e                                   =       85 (00.05%)
 s                                   =       83 (00.05%)
 p                                   =       71 (00.04%)
 password                            =       71 (00.04%)
 f                                   =       68 (00.04%)
 blue                                =       63 (00.03%)
 pass                                =       62 (00.03%)
 mike                                =       61 (00.03%)
 dragon                              =       59 (00.03%)
 test                                =       55 (00.03%)
 qwerty                              =       53 (00.03%)
 alex                                =       53 (00.03%)
 x                                   =       52 (00.03%)
--------------------Top 20 Base words End--------------------


============================================================
***************        Top Passwords         ***************
============================================================
 666                                 =        2 (00.00%)
 b                                   =        2 (00.00%)
 ola                                 =        2 (00.00%)
 monalisa                            =        2 (00.00%)
 mega                                =        1 (00.00%)
 meesterbok                          =        1 (00.00%)
 meer2807                            =        1 (00.00%)
 meera                               =        1 (00.00%)
 meera1                              =        1 (00.00%)
 meerakillas                         =        1 (00.00%)
 meereg                              =        1 (00.00%)
 meeri93                             =        1 (00.00%)
 meerim                              =        1 (00.00%)
 meesha33                            =        1 (00.00%)
 meeting                             =        1 (00.00%)
 meg@ssI                             =        1 (00.00%)
 meeturdate                          =        1 (00.00%)
 meer00                              =        1 (00.00%)
 mega1man5                           =        1 (00.00%)
 mefirst                             =        1 (00.00%)
-------------------- Top Passwords End  --------------------


============================================================
***************        Year Breakdown        ***************
============================================================
 1970   =       45 (00.02%)
 1971   =       58 (00.03%)
 1972   =       60 (00.03%)
 1973   =       84 (00.05%)
 1974   =       84 (00.05%)
 1975   =       80 (00.04%)
 1976   =       78 (00.04%)
 1977   =       96 (00.05%)
 1978   =      117 (00.06%)
 1979   =      139 (00.08%)
 1980   =      130 (00.07%)
 1981   =      139 (00.08%)
 1982   =      140 (00.08%)
 1983   =      165 (00.09%)
 1984   =      170 (00.09%)
 1985   =      167 (00.09%)
 1986   =      148 (00.08%)
 1987   =      182 (00.10%)
 1988   =      162 (00.09%)
 1989   =      135 (00.07%)
 1990   =      125 (00.07%)
 1991   =      114 (00.06%)
 1992   =       82 (00.04%)
 1993   =       46 (00.02%)
 1994   =       40 (00.02%)
 1995   =       25 (00.01%)
 1996   =       36 (00.02%)
 1997   =       53 (00.03%)
 1998   =       49 (00.03%)
 1999   =       78 (00.04%)
 2000   =      428 (00.23%)
 2001   =      230 (00.12%)
 2002   =      263 (00.14%)
 2003   =      226 (00.12%)
 2004   =      176 (00.10%)
 2005   =      199 (00.11%)
 2006   =      142 (00.08%)
 2007   =       88 (00.05%)
 2008   =       27 (00.01%)
 2009   =       23 (00.01%)
 2010   =       55 (00.03%)
 2011   =       47 (00.03%)
 2012   =       41 (00.02%)
 2013   =       27 (00.01%)
 2014   =        9 (00.00%)
 2015   =       15 (00.01%)
 2016   =       12 (00.01%)
 2017   =       17 (00.01%)
 2018   =       16 (00.01%)
 2019   =       15 (00.01%)
 2020   =       46 (00.02%)
 2021   =       39 (00.02%)
 2022   =       27 (00.01%)
 2023   =       14 (00.01%)
 2024   =       15 (00.01%)
-------------------- Year Breakdown End --------------------


============================================================
*************** Breakdown By Password Length ***************
============================================================
     8 =    55334 (30.01%)
     6 =    42064 (22.81%)
     7 =    32732 (17.75%)
     9 =    19183 (10.40%)
    10 =    11896 (06.45%)
     5 =     8208 (04.45%)
    11 =     4933 (02.68%)
     4 =     4599 (02.49%)
    12 =     2504 (01.36%)
    13 =     1018 (00.55%)
     3 =      779 (00.42%)
    14 =      516 (00.28%)
    15 =      231 (00.13%)
     2 =      136 (00.07%)
    16 =      125 (00.07%)
    17 =       36 (00.02%)
     1 =       33 (00.02%)
    18 =       27 (00.01%)
    19 =        9 (00.00%)
    20 =        8 (00.00%)
    21 =        5 (00.00%)
    23 =        3 (00.00%)
    32 =        3 (00.00%)
    22 =        2 (00.00%)
    27 =        2 (00.00%)
    25 =        1 (00.00%)
    28 =        1 (00.00%)
--------------------Breakdown By Password Length End--------------------


============================================================
***************     Break By Last Digit      ***************
============================================================
 1     =    13572 (07.36%)
 3     =     9313 (05.05%)
 2     =     8735 (04.74%)
 0     =     7753 (04.20%)
 9     =     6728 (03.65%)
 7     =     6473 (03.51%)
 5     =     6409 (03.48%)
 4     =     6279 (03.41%)
 6     =     5992 (03.25%)
 8     =     5726 (03.11%)
--------------------Break By Last Digit End--------------------


============================================================
***************       Day Abbreviated        ***************
============================================================
 mon   =      954 (00.52%)
 sun   =      298 (00.16%)
 sat   =      187 (00.10%)
 fri   =      169 (00.09%)
 wed   =       69 (00.04%)
 tue   =       16 (00.01%)
 thurs =        6 (00.00%)
--------------------Day Abbreviated End --------------------


============================================================
***************        Day Full Name         ***************
============================================================
 monday          =       12 (00.01%)
 friday          =       11 (00.01%)
 sunday          =        5 (00.00%)
 thursday        =        3 (00.00%)
 tuesday         =        2 (00.00%)
 saturday        =        1 (00.00%)
 wednesday       =        1 (00.00%)
-------------------- Day Full Name End  --------------------


============================================================
***************      Month Abbreviated       ***************
============================================================
 mar   =     1401 (00.76%)
 jan   =      341 (00.18%)
 jun   =      186 (00.10%)
 may   =      171 (00.09%)
 nov   =      159 (00.09%)
 jul   =      158 (00.09%)
 dec   =      119 (00.06%)
 sep   =      118 (00.06%)
 apr   =      108 (00.06%)
 aug   =       83 (00.05%)
 oct   =       69 (00.04%)
 feb   =       42 (00.02%)
--------------------Month Abbreviated End--------------------


============================================================
***************       Month Long Name        ***************
============================================================
 may             =      171 (00.09%)
 june            =       56 (00.03%)
 april           =       48 (00.03%)
 july            =       27 (00.01%)
 march           =       23 (00.01%)
 august          =       22 (00.01%)
 october         =       15 (00.01%)
 january         =        8 (00.00%)
 november        =        7 (00.00%)
 december        =        6 (00.00%)
 february        =        3 (00.00%)
 september       =        3 (00.00%)
--------------------Month Long Name End --------------------


============================================================
***************           Over All           ***************
============================================================
Total Passwords             =   184388
All Chars Lower Case        =   144786 (78.52%)
All Chars Upper Case        =     3984 (02.16%)
All Numbers                 =    20730 (11.24%)
First Char Number           =    31629 (17.15%)
First Char AlphaNum         =   152217 (82.55%)
Last Char Number            =    76980 (41.75%)
Last Char AlphaNum          =   106093 (57.54%)
First Char Special Char     =      542 (00.29%)
Last Char Special Char      =     1315 (00.71%)
Length Less than eq 6       =    55819 (30.27%)
Length Less than eq 8       =   143885 (78.03%)
Length greater than 8       =    40503 (21.97%)
Single Digit at the end     =    76980 (41.75%)
Two Digits at the end       =    62525 (33.91%)
Three Digits at the end     =    44393 (24.08%)
Four Digits at the end      =    34663 (18.80%)
--------------------    Over All End    --------------------


============================================================
***************Top 100 Characters in Password***************
============================================================
 a          =    97231 (07.00%)
 e          =    88474 (06.37%)
 o          =    65471 (04.71%)
 i          =    62326 (04.48%)
 r          =    61981 (04.46%)
 1          =    60861 (04.38%)
 n          =    58970 (04.24%)
 s          =    57282 (04.12%)
 t          =    49680 (03.57%)
 l          =    49344 (03.55%)
 0          =    45302 (03.26%)
 2          =    45240 (03.25%)
 m          =    39796 (02.86%)
 d          =    36329 (02.61%)
 3          =    34625 (02.49%)
 c          =    34610 (02.49%)
 h          =    32254 (02.32%)
 p          =    31323 (02.25%)
 b          =    30884 (02.22%)
 u          =    30169 (02.17%)
 9          =    29840 (02.15%)
 4          =    28482 (02.05%)
 k          =    28381 (02.04%)
 8          =    27474 (01.98%)
 5          =    27082 (01.95%)
 7          =    26361 (01.90%)
 6          =    25673 (01.85%)
 g          =    25381 (01.83%)
 y          =    20570 (01.48%)
 f          =    18032 (01.30%)
 w          =    15052 (01.08%)
 j          =    13195 (00.95%)
 v          =    12361 (00.89%)
 z          =     9829 (00.71%)
 x          =     8703 (00.63%)
 q          =     4289 (00.31%)
 A          =     3546 (00.26%)
 S          =     2948 (00.21%)
 E          =     2786 (00.20%)
 R          =     2561 (00.18%)
 T          =     2448 (00.18%)
 B          =     2384 (00.17%)
 M          =     2353 (00.17%)
 N          =     2333 (00.17%)
 L          =     2318 (00.17%)
 D          =     2211 (00.16%)
 I          =     2187 (00.16%)
 C          =     2150 (00.15%)
 P          =     2131 (00.15%)
 O          =     2103 (00.15%)
 H          =     1901 (00.14%)
 G          =     1775 (00.13%)
 K          =     1744 (00.13%)
 F          =     1676 (00.12%)
 J          =     1493 (00.11%)
 U          =     1489 (00.11%)
 W          =     1363 (00.10%)
 Y          =     1281 (00.09%)
 V          =     1205 (00.09%)
 X          =     1110 (00.08%)
 Z          =     1099 (00.08%)
 Q          =      927 (00.07%)
 !          =      830 (00.06%)
 .          =      790 (00.06%)
 @          =      611 (00.04%)
 -          =      604 (00.04%)
 _          =      504 (00.04%)
 *          =      451 (00.03%)
 $          =      312 (00.02%)
 #          =      265 (00.02%)
            =      181 (00.01%)
 /          =      120 (00.01%)
 ,          =      106 (00.01%)
 &          =       81 (00.01%)
 +          =       76 (00.01%)
 ?          =       73 (00.01%)
 %          =       69 (00.00%)
 ;          =       58 (00.00%)
 )          =       53 (00.00%)
 ^          =       50 (00.00%)
 =          =       46 (00.00%)
 \          =       42 (00.00%)
 ~          =       41 (00.00%)
 (          =       40 (00.00%)
 [          =       33 (00.00%)
 ]          =       29 (00.00%)
 `          =       26 (00.00%)
 :          =       21 (00.00%)
 '          =       17 (00.00%)
 <          =       13 (00.00%)
 "          =        8 (00.00%)
 |          =        7 (00.00%)
 >          =        7 (00.00%)
 {          =        4 (00.00%)
 }          =        2 (00.00%)
--------------------Top 100 Characters in Password End--------------------

```
