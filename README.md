# pypassal
Password Analyser in Python,is a python implementation for https://github.com/digininja/pipal . 
## Authors

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

Make sure python points to alteast python3.6

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
wget http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2
bzip2 -dk rockyou.txt.bz2
head -3000000 rockyou.txt > rockyou_3M.txt
cd ..
```
### Sample Run

```
(ev_pypassal) ╭─ashutosh [ ~/pypassal ] ‹master*› 
╰─▶ python pypassal.py ./data/rockyou_3M.txt
/usr/lib64/python3.6/importlib/_bootstrap.py:219: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88
  return f(*args, **kwds)
************************************************************
3000000it [05:16, 9481.68it/s]                                                                                                                                

============================================================
***************      Top 20 Base words       ***************
============================================================
 a                                   =     3602 (00.12%)
 v                                   =     2675 (00.09%)
 love                                =     2489 (00.08%)
 z                                   =     2190 (00.07%)
 w                                   =     2180 (00.07%)
 j                                   =     2121 (00.07%)
 may                                 =     2095 (00.07%)
 y                                   =     2012 (00.07%)
 m                                   =     1865 (00.06%)
 june                                =     1517 (00.05%)
 k                                   =     1485 (00.05%)
 s                                   =     1404 (00.05%)
 july                                =     1390 (00.05%)
 angel                               =     1272 (00.04%)
 c                                   =     1189 (00.04%)
 b                                   =     1162 (00.04%)
 x                                   =     1143 (00.04%)
 baby                                =     1139 (00.04%)
 jan                                 =     1107 (00.04%)
 d                                   =     1106 (00.04%)
--------------------Top 20 Base words End--------------------


============================================================
***************        Top Passwords         ***************
============================================================
 rock                                =        2 (00.00%)
 amor                                =        2 (00.00%)
 angel                               =        2 (00.00%)
 bianca                              =        2 (00.00%)
 vanessia                            =        2 (00.00%)
 20042006                            =        2 (00.00%)
 daniel                              =        2 (00.00%)
 yoporsiempre                        =        2 (00.00%)
 viviana                             =        2 (00.00%)
 angela                              =        2 (00.00%)
 yesica                              =        2 (00.00%)
 5 15                                =        2 (00.00%)
 5 1 5                               =        2 (00.00%)
 mueca                               =        2 (00.00%)
 king                                =        2 (00.00%)
 sasha                               =        2 (00.00%)
 123                                 =        2 (00.00%)
 yara                                =        2 (00.00%)
 andy                                =        2 (00.00%)
 victoria                            =        2 (00.00%)
-------------------- Top Passwords End  --------------------


============================================================
***************        Year Breakdown        ***************
============================================================
 1970   =     1170 (00.04%)
 1971   =     1148 (00.04%)
 1972   =     1268 (00.04%)
 1973   =     1350 (00.05%)
 1974   =     1425 (00.05%)
 1975   =     1552 (00.05%)
 1976   =     1688 (00.06%)
 1977   =     1875 (00.06%)
 1978   =     2007 (00.07%)
 1979   =     2180 (00.07%)
 1980   =     2636 (00.09%)
 1981   =     2540 (00.08%)
 1982   =     2906 (00.10%)
 1983   =     2863 (00.10%)
 1984   =     3472 (00.12%)
 1985   =     3662 (00.12%)
 1986   =     3877 (00.13%)
 1987   =     4653 (00.16%)
 1988   =     4205 (00.14%)
 1989   =     4817 (00.16%)
 1990   =     5025 (00.17%)
 1991   =     5169 (00.17%)
 1992   =     5351 (00.18%)
 1993   =     5320 (00.18%)
 1994   =     5274 (00.18%)
 1995   =     4662 (00.16%)
 1996   =     3764 (00.13%)
 1997   =     2699 (00.09%)
 1998   =     2024 (00.07%)
 1999   =     1668 (00.06%)
 2000   =     3919 (00.13%)
 2001   =     2710 (00.09%)
 2002   =     3052 (00.10%)
 2003   =     3309 (00.11%)
 2004   =     3832 (00.13%)
 2005   =     5411 (00.18%)
 2006   =     7350 (00.25%)
 2007   =     7315 (00.24%)
 2008   =     5856 (00.20%)
 2009   =     2693 (00.09%)
 2010   =     2009 (00.07%)
 2011   =     1007 (00.03%)
 2012   =     1066 (00.04%)
 2013   =      663 (00.02%)
 2014   =      372 (00.01%)
 2015   =      346 (00.01%)
 2016   =      273 (00.01%)
 2017   =      278 (00.01%)
 2018   =      318 (00.01%)
 2019   =      939 (00.03%)
 2020   =      779 (00.03%)
 2021   =      553 (00.02%)
 2022   =      488 (00.02%)
 2023   =      368 (00.01%)
 2024   =      328 (00.01%)
-------------------- Year Breakdown End --------------------


============================================================
*************** Breakdown By Password Length ***************
============================================================
     6 =   659254 (21.98%)
     8 =   652935 (21.76%)
     7 =   580811 (19.36%)
     9 =   399687 (13.32%)
    10 =   299199 (09.97%)
    11 =   122726 (04.09%)
     5 =    99429 (03.31%)
    12 =    71122 (02.37%)
    13 =    41810 (01.39%)
    14 =    27017 (00.90%)
    15 =    16314 (00.54%)
    16 =    10748 (00.36%)
     4 =     7841 (00.26%)
    17 =     3169 (00.11%)
    18 =     2015 (00.07%)
    19 =     1325 (00.04%)
    20 =     1016 (00.03%)
     3 =      864 (00.03%)
    21 =      569 (00.02%)
    22 =      426 (00.01%)
    23 =      338 (00.01%)
    24 =      250 (00.01%)
    25 =      200 (00.01%)
    26 =      166 (00.01%)
     2 =      146 (00.00%)
    27 =      111 (00.00%)
    28 =       90 (00.00%)
    30 =       65 (00.00%)
    29 =       54 (00.00%)
    31 =       40 (00.00%)
    32 =       35 (00.00%)
     1 =       32 (00.00%)
    33 =       19 (00.00%)
    34 =       18 (00.00%)
    35 =       18 (00.00%)
    36 =       12 (00.00%)
    37 =       11 (00.00%)
    39 =        9 (00.00%)
    41 =        9 (00.00%)
    38 =        8 (00.00%)
    42 =        7 (00.00%)
    43 =        6 (00.00%)
    40 =        6 (00.00%)
    47 =        5 (00.00%)
   255 =        4 (00.00%)
    45 =        4 (00.00%)
    48 =        3 (00.00%)
    67 =        3 (00.00%)
    57 =        2 (00.00%)
    79 =        2 (00.00%)
    60 =        2 (00.00%)
    59 =        2 (00.00%)
    44 =        2 (00.00%)
    53 =        2 (00.00%)
    52 =        2 (00.00%)
    50 =        2 (00.00%)
    49 =        2 (00.00%)
    56 =        1 (00.00%)
    89 =        1 (00.00%)
   222 =        1 (00.00%)
   197 =        1 (00.00%)
   165 =        1 (00.00%)
   150 =        1 (00.00%)
   149 =        1 (00.00%)
   139 =        1 (00.00%)
   137 =        1 (00.00%)
   101 =        1 (00.00%)
    80 =        1 (00.00%)
    88 =        1 (00.00%)
    87 =        1 (00.00%)
    58 =        1 (00.00%)
    77 =        1 (00.00%)
    75 =        1 (00.00%)
    71 =        1 (00.00%)
    63 =        1 (00.00%)
    61 =        1 (00.00%)
    55 =        1 (00.00%)
    69 =        1 (00.00%)
--------------------Breakdown By Password Length End--------------------


============================================================
***************     Break By Last Digit      ***************
============================================================
 1     =   285141 (09.50%)
 3     =   197833 (06.59%)
 2     =   175914 (05.86%)
 7     =   150227 (05.01%)
 5     =   147700 (04.92%)
 4     =   143653 (04.79%)
 6     =   141001 (04.70%)
 0     =   140375 (04.68%)
 9     =   134035 (04.47%)
 8     =   131372 (04.38%)
 ๕     =        7 (00.00%)
 ๑     =        6 (00.00%)
 ๓     =        4 (00.00%)
 ๗     =        3 (00.00%)
 ๒     =        2 (00.00%)
 ๘     =        2 (00.00%)
 ๔     =        1 (00.00%)
 ۶     =        1 (00.00%)
 ๖     =        1 (00.00%)
 ３     =        1 (00.00%)
 ５     =        1 (00.00%)
 ７     =        1 (00.00%)
 ８     =        1 (00.00%)
--------------------Break By Last Digit End--------------------


============================================================
***************       Day Abbreviated        ***************
============================================================
 mon   =    18179 (00.61%)
 sun   =     3971 (00.13%)
 fri   =     2993 (00.10%)
 sat   =     1705 (00.06%)
 wed   =     1609 (00.05%)
 tue   =      251 (00.01%)
 thurs =       55 (00.00%)
--------------------Day Abbreviated End --------------------


============================================================
***************        Day Full Name         ***************
============================================================
 friday          =      122 (00.00%)
 monday          =       99 (00.00%)
 sunday          =       88 (00.00%)
 wednesday       =       79 (00.00%)
 tuesday         =       48 (00.00%)
 saturday        =       28 (00.00%)
 thursday        =       28 (00.00%)
-------------------- Day Full Name End  --------------------


============================================================
***************      Month Abbreviated       ***************
============================================================
 mar   =    38480 (01.28%)
 jan   =     9023 (00.30%)
 may   =     7195 (00.24%)
 jun   =     5534 (00.18%)
 jul   =     5238 (00.17%)
 nov   =     3150 (00.11%)
 dec   =     2806 (00.09%)
 sep   =     2721 (00.09%)
 apr   =     2634 (00.09%)
 aug   =     2439 (00.08%)
 oct   =     2056 (00.07%)
 feb   =     1860 (00.06%)
--------------------Month Abbreviated End--------------------


============================================================
***************       Month Long Name        ***************
============================================================
 may             =     7245 (00.24%)
 june            =     2273 (00.08%)
 july            =     1802 (00.06%)
 april           =     1493 (00.05%)
 march           =     1208 (00.04%)
 august          =      635 (00.02%)
 october         =      419 (00.01%)
 december        =      324 (00.01%)
 november        =      314 (00.01%)
 january         =      303 (00.01%)
 september       =      250 (00.01%)
 february        =      128 (00.00%)
--------------------Month Long Name End --------------------


============================================================
***************           Over All           ***************
============================================================
Total Passwords             =  2999985
All Chars Lower Case        =  2420212 (80.67%)
All Chars Upper Case        =    89701 (02.99%)
All Numbers                 =   406891 (13.56%)
First Char Number           =   501423 (16.71%)
First Char AlphaNum         =  2487003 (82.90%)
Last Char Number            =  1647283 (54.91%)
Last Char AlphaNum          =  1302316 (43.41%)
First Char Special Char     =    11559 (00.39%)
Last Char Special Char      =    50386 (01.68%)
Length Less than eq 6       =   767566 (25.59%)
Length Less than eq 8       =  2001312 (66.71%)
Length greater than 8       =   998673 (33.29%)
Single Digit at the end     =  1647282 (54.91%)
Two Digits at the end       =  1356314 (45.21%)
Three Digits at the end     =   853895 (28.46%)
Four Digits at the end      =   687527 (22.92%)
--------------------    Over All End    --------------------


============================================================
***************    Character Composition     ***************
============================================================
 a          =  1884738 (62.82%)
 e          =  1609452 (53.65%)
 i          =  1228445 (40.95%)
 1          =  1214289 (40.48%)
 o          =  1128675 (37.62%)
 n          =  1058967 (35.30%)
 r          =   973256 (32.44%)
 l          =   959421 (31.98%)
 2          =   896514 (29.88%)
 0          =   888259 (29.61%)
 s          =   864644 (28.82%)
 t          =   726658 (24.22%)
 m          =   620010 (20.67%)
 y          =   611996 (20.40%)
 9          =   595713 (19.86%)
 3          =   584315 (19.48%)
 u          =   527848 (17.60%)
 c          =   524632 (17.49%)
 8          =   504473 (16.82%)
 d          =   503171 (16.77%)
 h          =   493936 (16.46%)
 4          =   488749 (16.29%)
 5          =   487435 (16.25%)
 6          =   446703 (14.89%)
 7          =   446361 (14.88%)
 b          =   417192 (13.91%)
 k          =   397285 (13.24%)
 g          =   358007 (11.93%)
 v          =   324987 (10.83%)
 p          =   321418 (10.71%)
 w          =   317368 (10.58%)
 z          =   225332 (07.51%)
 j          =   211851 (07.06%)
 f          =   187618 (06.25%)
 x          =   159030 (05.30%)
 A          =    73963 (02.47%)
 E          =    60434 (02.01%)
 I          =    45096 (01.50%)
 O          =    42158 (01.41%)
 L          =    41207 (01.37%)
 N          =    40589 (01.35%)
 R          =    40205 (01.34%)
 S          =    39712 (01.32%)
 q          =    34195 (01.14%)
 .          =    31044 (01.03%)
 T          =    31015 (01.03%)
 M          =    29894 (01.00%)
 C          =    25275 (00.84%)
 D          =    23315 (00.78%)
 B          =    23018 (00.77%)
 !          =    22640 (00.75%)
 _          =    20505 (00.68%)
 Y          =    20168 (00.67%)
 H          =    19810 (00.66%)
 -          =    17085 (00.57%)
 U          =    16670 (00.56%)
 P          =    15858 (00.53%)
 K          =    15648 (00.52%)
 G          =    15058 (00.50%)
 J          =    13375 (00.45%)
 *          =    12938 (00.43%)
            =    12404 (00.41%)
 @          =     9436 (00.31%)
 F          =     8922 (00.30%)
 V          =     8763 (00.29%)
 W          =     6848 (00.23%)
 #          =     6798 (00.23%)
 /          =     5891 (00.20%)
 ~          =     5368 (00.18%)
 Z          =     5075 (00.17%)
 X          =     4079 (00.14%)
 ,          =     3774 (00.13%)
 $          =     3456 (00.12%)
 ?          =     2861 (00.10%)
 &          =     2565 (00.09%)
 \          =     2463 (00.08%)
 ฟ          =     2236 (00.07%)
 +          =     2208 (00.07%)
 จ          =     2084 (00.07%)
 Q          =     2022 (00.07%)
 =          =     1960 (00.07%)
 น          =     1955 (00.07%)
 '          =     1766 (00.06%)
 ;          =     1656 (00.06%)
 ๅ          =     1635 (00.05%)
 ื          =     1506 (00.05%)
 ]          =     1436 (00.05%)
 )          =     1422 (00.05%)
 ร          =     1355 (00.05%)
 <          =     1277 (00.04%)
 (          =     1239 (00.04%)
 ค          =     1202 (00.04%)
 ำ          =     1180 (00.04%)
 ภ          =     1138 (00.04%)
 ถ          =     1109 (00.04%)
 ะ          =     1066 (00.04%)
 ท          =     1051 (00.04%)
 ต          =     1046 (00.03%)
 %          =     1026 (00.03%)
 ุ          =      995 (00.03%)
 ึ          =      932 (00.03%)
 า          =      926 (00.03%)
 [          =      901 (00.03%)
 พ          =      807 (00.03%)
 ส          =      787 (00.03%)
 ย          =      742 (00.02%)
 ี          =      717 (00.02%)
 ั          =      707 (00.02%)
 ñ          =      675 (00.02%)
 ก          =      645 (00.02%)
 ห          =      639 (00.02%)
 :          =      637 (00.02%)
 เ          =      635 (00.02%)
 ^          =      632 (00.02%)
 ้          =      619 (00.02%)
 {          =      594 (00.02%)
 แ          =      524 (00.02%)
 }          =      522 (00.02%)
 ิ          =      491 (00.02%)
 `          =      466 (00.02%)
 อ          =      441 (00.01%)
 ่          =      394 (00.01%)
 "          =      354 (00.01%)
 ไ          =      296 (00.01%)
 ด          =      282 (00.01%)
 |          =      272 (00.01%)
 ´          =      269 (00.01%)
 £          =      224 (00.01%)
 >          =      207 (00.01%)
 ผ          =      200 (00.01%)
 ا          =      183 (00.01%)
 ç          =      174 (00.01%)
 é          =      174 (00.01%)
 ๘          =      153 (00.01%)
 ง          =      152 (00.01%)
 ๑          =      152 (00.01%)
 ش          =      147 (00.00%)
 ม          =      140 (00.00%)
 à          =      134 (00.00%)
 م          =      127 (00.00%)
 ว          =      124 (00.00%)
 ل          =      121 (00.00%)
 ♥          =      118 (00.00%)
 ป          =      117 (00.00%)
 ي          =      114 (00.00%)
 ö          =      101 (00.00%)
 ์          =       97 (00.00%)
 ●          =       92 (00.00%)
 ı          =       88 (00.00%)
 ล          =       87 (00.00%)
 خ          =       85 (00.00%)
 ü          =       84 (00.00%)
 ة          =       84 (00.00%)
 α          =       83 (00.00%)
 º          =       81 (00.00%)
 س          =       76 (00.00%)
 á          =       74 (00.00%)
 ใ          =       72 (00.00%)
 ب          =       70 (00.00%)
 ث          =       65 (00.00%)
 บ          =       65 (00.00%)
 ä          =       61 (00.00%)
 ธ          =       60 (00.00%)
 ن          =       59 (00.00%)
 è          =       59 (00.00%)
 ه          =       59 (00.00%)
 ح          =       56 (00.00%)
 ฤ          =       55 (00.00%)
 י          =       55 (00.00%)
 ช          =       54 (00.00%)
 Ñ          =       53 (00.00%)
 ى          =       50 (00.00%)
 ر          =       49 (00.00%)
 ณ          =       48 (00.00%)
 د          =       47 (00.00%)
 و          =       45 (00.00%)
 ف          =       44 (00.00%)
 ๊          =       43 (00.00%)
 ו          =       42 (00.00%)
 ฎ          =       42 (00.00%)
 ق          =       41 (00.00%)
 ข          =       41 (00.00%)
 σ          =       41 (00.00%)
 ι          =       40 (00.00%)
 ş          =       39 (00.00%)
 โ          =       39 (00.00%)
 ¨          =       39 (00.00%)
 ع          =       38 (00.00%)
 ู          =       34 (00.00%)
 נ          =       33 (00.00%)
 ๆ          =       33 (00.00%)
 ษ          =       33 (00.00%)
 ศ          =       33 (00.00%)
 غ          =       33 (00.00%)
 λ          =       32 (00.00%)
 ๋          =       32 (00.00%)
 ã          =       31 (00.00%)
 §          =       31 (00.00%)
 ฯ          =       31 (00.00%)
 ๕          =       30 (00.00%)
 ל          =       29 (00.00%)
 ò          =       29 (00.00%)
 ש          =       28 (00.00%)
 ¡          =       28 (00.00%)
 ๗          =       28 (00.00%)
 ר          =       28 (00.00%)
 ó          =       27 (00.00%)
 ฑ          =       27 (00.00%)
 ¸          =       27 (00.00%)
 ญ          =       26 (00.00%)
 ο          =       25 (00.00%)
 İ          =       25 (00.00%)
 ็          =       25 (00.00%)
 ฉ          =       25 (00.00%)
 а          =       25 (00.00%)
 ¶          =       25 (00.00%)
 ص          =       24 (00.00%)
 א          =       24 (00.00%)
 ρ          =       24 (00.00%)
 ν          =       24 (00.00%)
 ك          =       23 (00.00%)
 ت          =       23 (00.00%)
 å          =       22 (00.00%)
 ฺ          =       22 (00.00%)
 ה          =       21 (00.00%)
 ø          =       20 (00.00%)
 н          =       20 (00.00%)
 ฆ          =       20 (00.00%)
 η          =       20 (00.00%)
 ε          =       20 (00.00%)
 ğ          =       20 (00.00%)
 †          =       19 (00.00%)
 í          =       19 (00.00%)
 ฏ          =       19 (00.00%)
 ד          =       19 (00.00%)
 ф          =       19 (00.00%)
 μ          =       19 (00.00%)
 ô          =       18 (00.00%)
 д          =       18 (00.00%)
 у          =       18 (00.00%)
 и          =       18 (00.00%)
 в          =       18 (00.00%)
 č          =       18 (00.00%)
 ¿          =       17 (00.00%)
 ํ          =       17 (00.00%)
 ฌ          =       17 (00.00%)
 к          =       17 (00.00%)
 т          =       17 (00.00%)
 ק          =       16 (00.00%)
 ª          =       16 (00.00%)
 ๒          =       16 (00.00%)
 ๖          =       16 (00.00%)
 מ          =       16 (00.00%)
 с          =       16 (00.00%)
 ы          =       16 (00.00%)
 τ          =       16 (00.00%)
 κ          =       16 (00.00%)
 °          =       16 (00.00%)
 ß          =       15 (00.00%)
 л          =       15 (00.00%)
 ™          =       14 (00.00%)
 æ          =       13 (00.00%)
 š          =       13 (00.00%)
 е          =       13 (00.00%)
 ‗          =       13 (00.00%)
 ฿          =       13 (00.00%)
 ฮ          =       13 (00.00%)
 ¢          =       13 (00.00%)
 є          =       13 (00.00%)
 р          =       13 (00.00%)
 Α          =       13 (00.00%)
 ù          =       12 (00.00%)
 ♠          =       12 (00.00%)
 ๔          =       12 (00.00%)
 ן          =       12 (00.00%)
 פ          =       12 (00.00%)
 ь          =       12 (00.00%)
 ш          =       12 (00.00%)
 υ          =       12 (00.00%)
 ž          =       12 (00.00%)
 Ç          =       11 (00.00%)
 ซ          =       11 (00.00%)
 ؤ          =       11 (00.00%)
 ج          =       11 (00.00%)
 ם          =       11 (00.00%)
 м          =       11 (00.00%)
 о          =       11 (00.00%)
 δ          =       11 (00.00%)
 Τ          =       11 (00.00%)
 €          =       10 (00.00%)
 ئ          =       10 (00.00%)
 ز          =       10 (00.00%)
 ב          =       10 (00.00%)
 π          =        9 (00.00%)
 γ          =        9 (00.00%)
 ║          =        9 (00.00%)
 ๙          =        9 (00.00%)
 ط          =        9 (00.00%)
 ء          =        9 (00.00%)
 ת          =        9 (00.00%)
 й          =        9 (00.00%)
 г          =        9 (00.00%)
 ω          =        9 (00.00%)
 â          =        9 (00.00%)
 ¬          =        8 (00.00%)
 Á          =        8 (00.00%)
 █          =        8 (00.00%)
 ض          =        8 (00.00%)
 ז          =        8 (00.00%)
 ѕ          =        8 (00.00%)
 я          =        8 (00.00%)
 Ο          =        8 (00.00%)
 Ι          =        8 (00.00%)
 Ν          =        8 (00.00%)
 ý          =        8 (00.00%)
 µ          =        8 (00.00%)
 ฝ          =        7 (00.00%)
 β          =        7 (00.00%)
 ¹          =        7 (00.00%)
 ๓          =        7 (00.00%)
 أ          =        7 (00.00%)
 כ          =        7 (00.00%)
 ע          =        7 (00.00%)
 ס          =        7 (00.00%)
 Κ          =        7 (00.00%)
 ח          =        6 (00.00%)
 ς          =        6 (00.00%)
 ·          =        6 (00.00%)
 «          =        6 (00.00%)
 »          =        6 (00.00%)
 │          =        6 (00.00%)
 •          =        6 (00.00%)
 θ          =        6 (00.00%)
 Σ          =        6 (00.00%)
 Š          =        6 (00.00%)
 þ          =        6 (00.00%)
 õ          =        6 (00.00%)
 É          =        6 (00.00%)
 ì          =        5 (00.00%)
 ú          =        5 (00.00%)
 ０          =        5 (00.00%)
 ５          =        5 (00.00%)
 ט          =        5 (00.00%)
 ג          =        5 (00.00%)
 ц          =        5 (00.00%)
 щ          =        5 (00.00%)
 п          =        5 (00.00%)
 Λ          =        5 (00.00%)
 ć          =        5 (00.00%)
 đ          =        5 (00.00%)
 î          =        5 (00.00%)
 ©          =        5 (00.00%)
 Ä          =        5 (00.00%)
 Ã          =        5 (00.00%)
 ℓ          =        5 (00.00%)
 ﾓ          =        4 (00.00%)
 ﾁ          =        4 (00.00%)
 ฒ          =        4 (00.00%)
 ¤          =        4 (00.00%)
 ®          =        4 (00.00%)
 ﾇ          =        4 (00.00%)
 ｱ          =        4 (00.00%)
 ９          =        4 (00.00%)
 ３          =        4 (00.00%)
 ♫          =        4 (00.00%)
 ☼          =        4 (00.00%)
 ∂          =        4 (00.00%)
 ỏ          =        4 (00.00%)
 ọ          =        4 (00.00%)
 з          =        4 (00.00%)
 х          =        4 (00.00%)
 ψ          =        4 (00.00%)
 Ρ          =        4 (00.00%)
 Θ          =        4 (00.00%)
 ˆ          =        4 (00.00%)
 ą          =        4 (00.00%)
 ê          =        4 (00.00%)
 …          =        4 (00.00%)
 Ö          =        4 (00.00%)
 Æ          =        4 (00.00%)
 ﾐ          =        3 (00.00%)
 ř          =        3 (00.00%)
 ¦          =        3 (00.00%)
 Ü          =        3 (00.00%)
 ¯          =        3 (00.00%)
 ７          =        3 (00.00%)
 ８          =        3 (00.00%)
 э          =        3 (00.00%)
 ူ          =        3 (00.00%)
 ္          =        3 (00.00%)
 ף          =        3 (00.00%)
 צ          =        3 (00.00%)
 ץ          =        3 (00.00%)
 ך          =        3 (00.00%)
 ү          =        3 (00.00%)
 ж          =        3 (00.00%)
 б          =        3 (00.00%)
 ч          =        3 (00.00%)
 Н          =        3 (00.00%)
 Ф          =        3 (00.00%)
 χ          =        3 (00.00%)
 φ          =        3 (00.00%)
 ζ          =        3 (00.00%)
 Π          =        3 (00.00%)
 Μ          =        3 (00.00%)
 Γ          =        3 (00.00%)
 ě          =        3 (00.00%)
 ă          =        3 (00.00%)
 ð          =        3 (00.00%)
 Ž          =        3 (00.00%)
 ư          =        2 (00.00%)
 ﾝ          =        2 (00.00%)
 ﾗ          =        2 (00.00%)
 ｴ          =        2 (00.00%)
 ﾕ          =        2 (00.00%)
 ﾖ          =        2 (00.00%)
 ｐ          =        2 (00.00%)
 １          =        2 (00.00%)
 使          =        2 (00.00%)
 到          =        2 (00.00%)
 我          =        2 (00.00%)
 的          =        2 (00.00%)
 东          =        2 (00.00%)
 西          =        2 (00.00%)
 ㅁ          =        2 (00.00%)
 ㅣ          =        2 (00.00%)
 ♦          =        2 (00.00%)
 ♣          =        2 (00.00%)
 ◕          =        2 (00.00%)
 ▬          =        2 (00.00%)
 ▒          =        2 (00.00%)
 “          =        2 (00.00%)
 ớ          =        2 (00.00%)
 ố          =        2 (00.00%)
 ာ          =        2 (00.00%)
 န          =        2 (00.00%)
 ေ          =        2 (00.00%)
 စ          =        2 (00.00%)
 သ          =        2 (00.00%)
 က          =        2 (00.00%)
 ခ          =        2 (00.00%)
 ယ          =        2 (00.00%)
 အ          =        2 (00.00%)
 ˹          =        2 (00.00%)
 ་          =        2 (00.00%)
 ད          =        2 (00.00%)
 ๛          =        2 (00.00%)
 ฃ          =        2 (00.00%)
 ฐ          =        2 (00.00%)
 ల          =        2 (00.00%)
 బ          =        2 (00.00%)
 ూ          =        2 (00.00%)
 ی          =        2 (00.00%)
 ً          =        2 (00.00%)
 ѹ          =        2 (00.00%)
 ъ          =        2 (00.00%)
 Д          =        2 (00.00%)
 Е          =        2 (00.00%)
 И          =        2 (00.00%)
 Η          =        2 (00.00%)
 Ε          =        2 (00.00%)
 Υ          =        2 (00.00%)
 ‘          =        2 (00.00%)
 Đ          =        2 (00.00%)
 ˿          =        2 (00.00%)
 Ò          =        2 (00.00%)
 ľ          =        2 (00.00%)
 ę          =        2 (00.00%)
 ́          =        2 (00.00%)
 ̉          =        2 (00.00%)
 ū          =        2 (00.00%)
 ÿ          =        2 (00.00%)
 ť          =        2 (00.00%)
 û          =        2 (00.00%)
 ẻ          =        2 (00.00%)
 –          =        2 (00.00%)
 ±          =        2 (00.00%)
 Ô          =        2 (00.00%)
 Í          =        2 (00.00%)
 Ë          =        2 (00.00%)
 Ř          =        2 (00.00%)
 ｺ          =        1 (00.00%)
 ﾅ          =        1 (00.00%)
 ۶          =        1 (00.00%)
 Ó          =        1 (00.00%)
 񥯮          =        1 (00.00%)
 ﾘ          =        1 (00.00%)
 ｼ          =        1 (00.00%)
 ﾉ          =        1 (00.00%)
 ﾄ          =        1 (00.00%)
 ﾋ          =        1 (00.00%)
 ｲ          =        1 (00.00%)
 ﾜ          =        1 (00.00%)
 ｵ          =        1 (00.00%)
 ｿ          =        1 (00.00%)
 ﾏ          =        1 (00.00%)
 ｾ          =        1 (00.00%)
 ｗ          =        1 (00.00%)
 ｘ          =        1 (00.00%)
 ｉ          =        1 (00.00%)
 ｎ          =        1 (00.00%)
 ｈ          =        1 (00.00%)
 ６          =        1 (00.00%)
 ２          =        1 (00.00%)
 聽          =        1 (00.00%)
 日          =        1 (00.00%)
 唔          =        1 (00.00%)
 番          =        1 (00.00%)
 牙          =        1 (00.00%)
 你          =        1 (00.00%)
 空          =        1 (00.00%)
 尐          =        1 (00.00%)
 淘          =        1 (00.00%)
 氣          =        1 (00.00%)
 寯          =        1 (00.00%)
 保          =        1 (00.00%)
 存          =        1 (00.00%)
 （          =        1 (00.00%)
 推          =        1 (00.00%)
 荐          =        1 (00.00%)
 ）          =        1 (00.00%)
 中          =        1 (00.00%)
 文          =        1 (00.00%)
 ㅋ          =        1 (00.00%)
 ㄷ          =        1 (00.00%)
 ㅠ          =        1 (00.00%)
 ㅕ          =        1 (00.00%)
 ㅊ          =        1 (00.00%)
 ㄴ          =        1 (00.00%)
 샤          =        1 (00.00%)
 ㅐ          =        1 (00.00%)
 ㄓ          =        1 (00.00%)
 べ          =        1 (00.00%)
 え          =        1 (00.00%)
 ぽ          =        1 (00.00%)
 こ          =        1 (00.00%)
 ん          =        1 (00.00%)
 に          =        1 (00.00%)
 ち          =        1 (00.00%)
 は          =        1 (00.00%)
 ☜          =        1 (00.00%)
 ❤          =        1 (00.00%)
 ☞          =        1 (00.00%)
 ｡          =        1 (00.00%)
 ‿          =        1 (00.00%)
 づ          =        1 (00.00%)
 ◙          =        1 (00.00%)
 ╥          =        1 (00.00%)
 ▌          =        1 (00.00%)
 Ċ          =        1 (00.00%)
 ђ          =        1 (00.00%)
 ”          =        1 (00.00%)
 ỳ          =        1 (00.00%)
 ỗ          =        1 (00.00%)
 ổ          =        1 (00.00%)
 ấ          =        1 (00.00%)
 ნ          =        1 (00.00%)
 ო          =        1 (00.00%)
 მ          =        1 (00.00%)
 ე          =        1 (00.00%)
 დ          =        1 (00.00%)
 ი          =        1 (00.00%)
 გ          =        1 (00.00%)
 ა          =        1 (00.00%)
 ს          =        1 (00.00%)
 ၾ          =        1 (00.00%)
 ၆          =        1 (00.00%)
 ။          =        1 (00.00%)
 ည          =        1 (00.00%)
 ႑          =        1 (00.00%)
 ပ          =        1 (00.00%)
 ်          =        1 (00.00%)
 တ          =        1 (00.00%)
 ထ          =        1 (00.00%)
 း          =        1 (00.00%)
 ရ          =        1 (00.00%)
 ့          =        1 (00.00%)
 င          =        1 (00.00%)
 མ          =        1 (00.00%)
 ི          =        1 (00.00%)
 ྲ          =        1 (00.00%)
 ེ          =        1 (00.00%)
 ๐          =        1 (00.00%)
 Ÿ          =        1 (00.00%)
 ో          =        1 (00.00%)
 క          =        1 (00.00%)
 గ          =        1 (00.00%)
 ɮ          =        1 (00.00%)
 Ҿ          =        1 (00.00%)
 ِ          =        1 (00.00%)
 إ          =        1 (00.00%)
 ؟          =        1 (00.00%)
 ’          =        1 (00.00%)
 آ          =        1 (00.00%)
 ظ          =        1 (00.00%)
 ،          =        1 (00.00%)
 ؘ          =        1 (00.00%)
 墾          =        1 (00.00%)
 ҹ          =        1 (00.00%)
 Ѽ          =        1 (00.00%)
 ƒ          =        1 (00.00%)
 ю          =        1 (00.00%)
 џ          =        1 (00.00%)
 ј          =        1 (00.00%)
 Г          =        1 (00.00%)
 ә          =        1 (00.00%)
 Ы          =        1 (00.00%)
 Ь          =        1 (00.00%)
 Л          =        1 (00.00%)
 Ц          =        1 (00.00%)
 Χ          =        1 (00.00%)
 Я          =        1 (00.00%)
 Ч          =        1 (00.00%)
 ͔          =        1 (00.00%)
 㝔          =        1 (00.00%)
 㤢          =        1 (00.00%)
 ˓          =        1 (00.00%)
 ș          =        1 (00.00%)
 ơ          =        1 (00.00%)
 ź          =        1 (00.00%)
 Ş          =        1 (00.00%)
 ś          =        1 (00.00%)
 Ł          =        1 (00.00%)
 ̀          =        1 (00.00%)
 ̃          =        1 (00.00%)
 Ā          =        1 (00.00%)
 Î          =        1 (00.00%)
 ‰          =        1 (00.00%)
 —          =        1 (00.00%)
 Œ          =        1 (00.00%)
 ²          =        1 (00.00%)
 ը          =        1 (00.00%)
 Ğ          =        1 (00.00%)
 Ï          =        1 (00.00%)
 Č          =        1 (00.00%)
 À          =        1 (00.00%)
 Ê          =        1 (00.00%)
           =        1 (00.00%)
 Õ          =        1 (00.00%)
           =        1 (00.00%)
 Ś          =        1 (00.00%)
 Ϊ          =        1 (00.00%)
 Ě          =        1 (00.00%)
 ☻          =        1 (00.00%)
           =        1 (00.00%)
 œ          =        1 (00.00%)
 ¥          =        1 (00.00%)
 ẩ          =        1 (00.00%)
 ő          =        1 (00.00%)
 ‎          =        1 (00.00%)
--------------------Character Composition End--------------------

```
