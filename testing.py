import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

# Sample data parsing (replace this with your actual data parsing)
data = """
aX = 14988 | aY = -6344 | aZ = -6080 | gX = -458 | gY = -189 | gZ = 178
aX = 15156 | aY = -5572 | aZ = -6468 | gX = -567 | gY = -206 | gZ = 125
aX = 14784 | aY = -5948 | aZ = -6552 | gX = -497 | gY = 0 | gZ = 115
aX = 14804 | aY = -5608 | aZ = -6480 | gX = -657 | gY = -192 | gZ = 41
aX = 14780 | aY = -5756 | aZ = -6312 | gX = -297 | gY = -367 | gZ = 461
aX = 14908 | aY = -5460 | aZ = -7008 | gX = -681 | gY = -367 | gZ = -25
aX = 15444 | aY = -4920 | aZ = -8068 | gX = -615 | gY = -1136 | gZ = -107
aX = 14648 | aY = -4816 | aZ = -8372 | gX = -394 | gY = -1156 | gZ = -246
aX = 13588 | aY = -4820 | aZ = -9116 | gX = -1082 | gY = -1063 | gZ = 418
aX = 13020 | aY = -3092 | aZ = -10696 | gX = -1620 | gY = -1699 | gZ = -28
aX = 13064 | aY = -3780 | aZ = -10852 | gX = -698 | gY = -721 | gZ = 638
aX = 13260 | aY = -4256 | aZ = -9936 | gX = -263 | gY = 1221 | gZ = 593
aX = 14580 | aY = -4412 | aZ = -8404 | gX = -27 | gY = 1335 | gZ = 283
aX = 15132 | aY = -4656 | aZ = -7088 | gX = -370 | gY = 466 | gZ = 392
aX = 15256 | aY = -4712 | aZ = -5988 | gX = 34 | gY = 1476 | gZ = 136
aX = 16920 | aY = -4460 | aZ = -3492 | gX = -307 | gY = 1453 | gZ = -493
aX = 16276 | aY = -5124 | aZ = -2172 | gX = -236 | gY = 400 | gZ = 132
aX = 16444 | aY = -4768 | aZ = -1940 | gX = -430 | gY = 54 | gZ = 462
aX = 17716 | aY = -4972 | aZ = -2316 | gX = -1080 | gY = -1717 | gZ = 11
aX = 15440 | aY = -4836 | aZ = -5476 | gX = -590 | gY = -2342 | gZ = 505
aX = 15304 | aY = -4264 | aZ = -7172 | gX = -364 | gY = -465 | gZ = -122
aX = 15028 | aY = -4912 | aZ = -6852 | gX = -368 | gY = 109 | gZ = -4
aX = 15488 | aY = -4728 | aZ = -6708 | gX = -543 | gY = -46 | gZ = 376
"""
data12 = """
aX = 16400 | aY = -740 | aZ = 3636 | gX = -620 | gY = -2442 | gZ = -859
aX = 16512 | aY = -1512 | aZ = 3048 | gX = 256 | gY = -1123 | gZ = 736
aX = 16920 | aY = -1064 | aZ = 1452 | gX = -731 | gY = -655 | gZ = 672
aX = 17300 | aY = -1204 | aZ = 1032 | gX = -708 | gY = 465 | gZ = 1338
aX = 16996 | aY = -1592 | aZ = 428 | gX = -824 | gY = -1491 | gZ = 161
aX = 17404 | aY = -1416 | aZ = -932 | gX = -1035 | gY = -1461 | gZ = 35
aX = 16544 | aY = -1308 | aZ = -2692 | gX = -254 | gY = -1252 | gZ = 330
aX = 16288 | aY = -1432 | aZ = -3492 | gX = -653 | gY = -417 | gZ = 111
aX = 17020 | aY = -1424 | aZ = -3896 | gX = -658 | gY = -152 | gZ = 345
aX = 16704 | aY = -1640 | aZ = -3736 | gX = -519 | gY = -509 | gZ = 372
aX = 16744 | aY = -1056 | aZ = -4208 | gX = -354 | gY = -193 | gZ = 123
aX = 16616 | aY = -1608 | aZ = -3980 | gX = -575 | gY = -455 | gZ = 267
aX = 15880 | aY = -2052 | aZ = -3596 | gX = 111 | gY = -300 | gZ = 604
aX = 17228 | aY = -2120 | aZ = -4652 | gX = -592 | gY = -2380 | gZ = -731
aX = 15624 | aY = -1308 | aZ = -6060 | gX = -1182 | gY = -2032 | gZ = 629
aX = 15212 | aY = -1656 | aZ = -7568 | gX = -519 | gY = -933 | gZ = 85
aX = 15784 | aY = -2028 | aZ = -6456 | gX = -869 | gY = 393 | gZ = 34
aX = 15912 | aY = -1548 | aZ = -6064 | gX = -303 | gY = 1003 | gZ = -225
aX = 16228 | aY = -1376 | aZ = -4736 | gX = -844 | gY = 1126 | gZ = 72
aX = 16640 | aY = -716 | aZ = -3244 | gX = -551 | gY = 1192 | gZ = -197
aX = 17388 | aY = -240 | aZ = -1600 | gX = -639 | gY = 926 | gZ = -130
aX = 17276 | aY = 224 | aZ = -972 | gX = -518 | gY = 747 | gZ = -1055
aX = 16868 | aY = 1000 | aZ = 116 | gX = -607 | gY = 1010 | gZ = -719
aX = 15956 | aY = 480 | aZ = 1780 | gX = -1187 | gY = 1917 | gZ = -191
aX = 16120 | aY = 1712 | aZ = 2120 | gX = -927 | gY = 632 | gZ = 720
aX = 17880 | aY = 2764 | aZ = 2880 | gX = -491 | gY = -545 | gZ = -794
"""
data11 = """
aX = 15296 | aY = 2284 | aZ = -9488 | gX = -221 | gY = 550 | gZ = 537
aX = 15172 | aY = 2104 | aZ = -9220 | gX = -219 | gY = 264 | gZ = 583
aX = 15104 | aY = 1928 | aZ = -9144 | gX = -186 | gY = 112 | gZ = 495
aX = 15036 | aY = 1816 | aZ = -9272 | gX = -195 | gY = 225 | gZ = 618
aX = 15004 | aY = 1816 | aZ = -9304 | gX = -331 | gY = 424 | gZ = 713
aX = 15416 | aY = 1716 | aZ = -9236 | gX = -397 | gY = 400 | gZ = 661
aX = 15564 | aY = 1544 | aZ = -9128 | gX = -509 | gY = 489 | gZ = 640
aX = 15912 | aY = 1676 | aZ = -9184 | gX = -649 | gY = 411 | gZ = 765
aX = 16152 | aY = 1688 | aZ = -9176 | gX = -769 | gY = 329 | gZ = 940
aX = 15576 | aY = 1832 | aZ = -9100 | gX = -649 | gY = 398 | gZ = 882
aX = 16052 | aY = 1620 | aZ = -8684 | gX = -804 | gY = -453 | gZ = 274
aX = 16456 | aY = 1740 | aZ = -8836 | gX = -950 | gY = 349 | gZ = 1179
aX = 14920 | aY = 1704 | aZ = -9108 | gX = -849 | gY = -757 | gZ = 314
aX = 14492 | aY = 1916 | aZ = -9480 | gX = -768 | gY = -505 | gZ = 201
aX = 14372 | aY = 1800 | aZ = -9548 | gX = -824 | gY = 40 | gZ = 608
aX = 14560 | aY = 1460 | aZ = -9064 | gX = -821 | gY = 95 | gZ = 918
aX = 17600 | aY = 876 | aZ = -8688 | gX = -1433 | gY = 1094 | gZ = 2911
aX = 16480 | aY = -108 | aZ = -8380 | gX = -1934 | gY = 1725 | gZ = 4118
aX = 14648 | aY = 708 | aZ = -8676 | gX = -1563 | gY = -1466 | gZ = -73
aX = 14172 | aY = 2140 | aZ = -9828 | gX = -897 | gY = -1923 | gZ = -1784
aX = 13924 | aY = 2760 | aZ = -9564 | gX = -475 | gY = -2730 | gZ = -3404
aX = 14976 | aY = 3608 | aZ = -9756 | gX = -200 | gY = -2074 | gZ = -2777
aX = 14932 | aY = 3740 | aZ = -9896 | gX = -238 | gY = -300 | gZ = -521
aX = 15096 | aY = 3160 | aZ = -9520 | gX = -64 | gY = 900 | gZ = 932
aX = 15564 | aY = 2364 | aZ = -9344 | gX = 72 | gY = 379 | gZ = 737
aX = 15324 | aY = 1596 | aZ = -9036 | gX = 203 | gY = 78 | gZ = 475
aX = 14852 | aY = 1388 | aZ = -9196 | gX = -12 | gY = -94 | gZ = 505
aX = 14496 | aY = 1220 | aZ = -9196 | gX = -202 | gY = 143 | gZ = 728
aX = 14648 | aY = 1232 | aZ = -9136 | gX = -216 | gY = 293 | gZ = 402
aX = 15164 | aY = 1328 | aZ = -9244 | gX = -204 | gY = -19 | gZ = 129
"""
data10 = """
aX = -108 | aY = -1552 | aZ = 2024 | gX = -1939 | gY = -2640 | gZ = -854
aX = -72 | aY = -1660 | aZ = 1908 | gX = -1608 | gY = -4236 | gZ = -648
aX = -492 | aY = -2304 | aZ = 2300 | gX = -2359 | gY = -3677 | gZ = -904
aX = -584 | aY = -2452 | aZ = 2184 | gX = -2121 | gY = -4475 | gZ = -1005
aX = 52 | aY = -3220 | aZ = 2836 | gX = -2681 | gY = -3557 | gZ = -141
aX = 120 | aY = -2548 | aZ = 1880 | gX = -2179 | gY = -4877 | gZ = -795
aX = -940 | aY = -3436 | aZ = 1348 | gX = -2893 | gY = -4264 | gZ = -1317
aX = -2636 | aY = -2908 | aZ = 80 | gX = -2212 | gY = -4071 | gZ = -740
aX = -644 | aY = -2612 | aZ = 568 | gX = -1663 | gY = -3783 | gZ = -947
aX = -1632 | aY = -2452 | aZ = -88 | gX = -2393 | gY = -4146 | gZ = -1047
aX = -1716 | aY = -3056 | aZ = 500 | gX = -2315 | gY = -3524 | gZ = -857
aX = -2004 | aY = -3304 | aZ = 416 | gX = -2227 | gY = -2803 | gZ = -291
aX = -1004 | aY = -3052 | aZ = 980 | gX = -2672 | gY = -3301 | gZ = -1426
aX = -1208 | aY = -3440 | aZ = 1264 | gX = -2218 | gY = -3052 | gZ = -975
aX = -424 | aY = -2660 | aZ = 1704 | gX = -2217 | gY = -3063 | gZ = -963
aX = -860 | aY = -3192 | aZ = 2544 | gX = -2296 | gY = -3107 | gZ = -892
aX = 104 | aY = -2928 | aZ = 3244 | gX = -2341 | gY = -2920 | gZ = -562
aX = 92 | aY = -3200 | aZ = 3676 | gX = -2313 | gY = -2826 | gZ = -1153
aX = 436 | aY = -3512 | aZ = 4896 | gX = -1892 | gY = -2572 | gZ = -906
aX = 508 | aY = -2996 | aZ = 5780 | gX = -2244 | gY = -2944 | gZ = -692
aX = 1796 | aY = -3520 | aZ = 6912 | gX = -2942 | gY = -3677 | gZ = -802
aX = 804 | aY = -3016 | aZ = 7404 | gX = -2261 | gY = -2396 | gZ = -1802
aX = 980 | aY = -2360 | aZ = 8176 | gX = -1822 | gY = -3066 | gZ = -1370
aX = 2468 | aY = -1184 | aZ = 8344 | gX = -3429 | gY = -2378 | gZ = -2831
aX = -2020 | aY = 2340 | aZ = 7860 | gX = -2333 | gY = -478 | gZ = 400
aX = -736 | aY = -736 | aZ = 10356 | gX = -2773 | gY = -4593 | gZ = -2877
aX = 108 | aY = 240 | aZ = 9980 | gX = -2111 | gY = -3477 | gZ = -968
"""
data9 = """
aX = -108 | aY = -68 | aZ = -220 | gX = -220 | gY = -103 | gZ = -226
aX = -104 | aY = -4 | aZ = -44 | gX = 98 | gY = 148 | gZ = -206
aX = 524 | aY = -388 | aZ = -288 | gX = -174 | gY = -435 | gZ = 379
aX = 820 | aY = 400 | aZ = -376 | gX = -262 | gY = -631 | gZ = -110
aX = 72 | aY = 224 | aZ = -448 | gX = -303 | gY = -1283 | gZ = -53
aX = 0 | aY = 256 | aZ = -1068 | gX = 134 | gY = 277 | gZ = -612
aX = -1060 | aY = 216 | aZ = -1152 | gX = -552 | gY = 724 | gZ = -1336
aX = -636 | aY = 280 | aZ = -1976 | gX = 81 | gY = -600 | gZ = -374
aX = -240 | aY = 520 | aZ = -1896 | gX = -476 | gY = 422 | gZ = -397
aX = -408 | aY = 716 | aZ = -1500 | gX = -226 | gY = 993 | gZ = 187
aX = -476 | aY = 392 | aZ = -128 | gX = -369 | gY = 556 | gZ = -595
aX = -232 | aY = 8 | aZ = 368 | gX = -524 | gY = 376 | gZ = -245
aX = 368 | aY = -460 | aZ = 796 | gX = 177 | gY = 689 | gZ = 21
aX = -204 | aY = 200 | aZ = 336 | gX = 122 | gY = -50 | gZ = -39
aX = -48 | aY = -296 | aZ = 604 | gX = -290 | gY = -60 | gZ = -979
aX = -136 | aY = 160 | aZ = 380 | gX = 237 | gY = 187 | gZ = -206
aX = -368 | aY = 140 | aZ = 536 | gX = 96 | gY = 168 | gZ = -327
aX = -60 | aY = 284 | aZ = 416 | gX = -321 | gY = -79 | gZ = -1069
aX = -20 | aY = 1016 | aZ = 308 | gX = -71 | gY = -29 | gZ = -211
aX = -164 | aY = 712 | aZ = -8 | gX = 349 | gY = 352 | gZ = 41
"""
data8 = """
aX = -1024 | aY = 52 | aZ = 624 | gX = -25 | gY = 155 | gZ = 21
aX = -972 | aY = -40 | aZ = 516 | gX = 15 | gY = 18 | gZ = 31
aX = -1016 | aY = -12 | aZ = 876 | gX = 113 | gY = -79 | gZ = -43
aX = -1000 | aY = -92 | aZ = 752 | gX = 109 | gY = -126 | gZ = -7
aX = -1128 | aY = -52 | aZ = 472 | gX = 34 | gY = 3 | gZ = 29
aX = -1348 | aY = -68 | aZ = 768 | gX = 136 | gY = -228 | gZ = -164
aX = -1340 | aY = -276 | aZ = 1096 | gX = 215 | gY = 138 | gZ = -99
aX = -1788 | aY = -560 | aZ = 608 | gX = -317 | gY = 563 | gZ = 207
aX = -2188 | aY = -852 | aZ = 1172 | gX = 988 | gY = -1557 | gZ = -365
aX = -1552 | aY = -320 | aZ = 660 | gX = 450 | gY = -542 | gZ = -220
aX = -1100 | aY = 56 | aZ = 352 | gX = 122 | gY = 2 | gZ = -44
aX = -944 | aY = 116 | aZ = 340 | gX = 79 | gY = -67 | gZ = -61
aX = -912 | aY = 68 | aZ = 468 | gX = 100 | gY = 62 | gZ = -79
aX = -988 | aY = 224 | aZ = 356 | gX = 55 | gY = 5 | gZ = -51
aX = -904 | aY = 100 | aZ = 428 | gX = 93 | gY = 23 | gZ = -44
aX = -420 | aY = 44 | aZ = 848 | gX = 1921 | gY = -2811 | gZ = -1255
aX = 1300 | aY = 1836 | aZ = -1132 | gX = 1455 | gY = -1250 | gZ = -732
aX = 1568 | aY = 2112 | aZ = -1524 | gX = -74 | gY = -5 | gZ = 137
aX = 1192 | aY = 1676 | aZ = -1108 | gX = -1192 | gY = 1183 | gZ = 584
aX = 880 | aY = 1136 | aZ = -824 | gX = -16 | gY = 206 | gZ = 11
aX = 804 | aY = 1156 | aZ = -600 | gX = 155 | gY = -70 | gZ = -93
aX = 540 | aY = 1116 | aZ = -588 | gX = 59 | gY = 110 | gZ = -45
aX = 424 | aY = 1088 | aZ = -496 | gX = 99 | gY = 114 | gZ = -87
aX = 284 | aY = 1016 | aZ = -288 | gX = 54 | gY = 162 | gZ = 13
aX = 276 | aY = 892 | aZ = -208 | gX = 65 | gY = 90 | gZ = -52
aX = 108 | aY = 820 | aZ = -388 | gX = 29 | gY = 81 | gZ = -15
aX = 196 | aY = 912 | aZ = -316 | gX = 73 | gY = -3 | gZ = -34
aX = 196 | aY = 776 | aZ = -212 | gX = 2 | gY = 223 | gZ = 12
aX = 80 | aY = 568 | aZ = -260 | gX = -20 | gY = 34 | gZ = 14
"""
data6 = """
aX = 16932 | aY = 2032 | aZ = 1204 | gX = -1409 | gY = -4046 | gZ = 1438
aX = 16776 | aY = 1824 | aZ = -3692 | gX = 1716 | gY = -3073 | gZ = 1255
aX = 14624 | aY = 308 | aZ = -6156 | gX = 135 | gY = -1198 | gZ = 589
aX = 17788 | aY = 752 | aZ = -5400 | gX = -680 | gY = 4985 | gZ = 1053
aX = 17784 | aY = 4612 | aZ = -1192 | gX = -2611 | gY = 4189 | gZ = -4666
aX = 13768 | aY = 7500 | aZ = 4768 | gX = -2890 | gY = 5665 | gZ = -3442
aX = 9968 | aY = 9916 | aZ = 6832 | gX = 1477 | gY = -785 | gZ = -3661
aX = 9868 | aY = 9948 | aZ = 8008 | gX = -1543 | gY = 239 | gZ = 911
aX = 10572 | aY = 9480 | aZ = 7712 | gX = -351 | gY = -625 | gZ = 467
aX = 10464 | aY = 9340 | aZ = 8088 | gX = -611 | gY = -16 | gZ = 267
aX = 10584 | aY = 9484 | aZ = 7724 | gX = -304 | gY = -406 | gZ = 233
aX = 10856 | aY = 9584 | aZ = 7448 | gX = -553 | gY = -96 | gZ = 251
aX = 10768 | aY = 9580 | aZ = 7864 | gX = -783 | gY = 372 | gZ = -129
"""
data5 = """
aX = -4336 | aY = -3496 | aZ = -25996 | gX = -4710 | gY = 4770 | gZ = 66
aX = -1424 | aY = -21708 | aZ = 9120 | gX = -1992 | gY = -1916 | gZ = -1662
aX = 1304 | aY = -16116 | aZ = -88 | gX = -892 | gY = -139 | gZ = 247
aX = 1348 | aY = -16084 | aZ = -164 | gX = -762 | gY = 69 | gZ = 71
aX = 1392 | aY = -15996 | aZ = -1280 | gX = -1733 | gY = -765 | gZ = 836
aX = 1164 | aY = -16128 | aZ = -1496 | gX = -894 | gY = -837 | gZ = 522
aX = 1156 | aY = -16236 | aZ = 636 | gX = -4395 | gY = 771 | gZ = 684
"""
data4 = """
aX = 16248 | aY = -2016 | aZ = -6760 | gX = 70 | gY = -736 | gZ = 1146
aX = 14636 | aY = -2816 | aZ = -8700 | gX = -963 | gY = -4146 | gZ = -2
aX = 12680 | aY = -368 | aZ = -12208 | gX = -2801 | gY = -2807 | gZ = -1916
aX = 11268 | aY = 2936 | aZ = -13816 | gX = -2717 | gY = -1885 | gZ = -2221
aX = 9604 | aY = 8600 | aZ = -13280 | gX = -3074 | gY = -137 | gZ = -3120
aX = 11964 | aY = 8088 | aZ = -8964 | gX = -969 | gY = 4115 | gZ = -284
aX = 14012 | aY = 7272 | aZ = -7416 | gX = 757 | gY = 2720 | gZ = 4029
aX = 15732 | aY = 4212 | aZ = -5784 | gX = 919 | gY = 1026 | gZ = 2751
aX = 16580 | aY = 88 | aZ = -4468 | gX = -244 | gY = 1157 | gZ = 1315
aX = 15808 | aY = -356 | aZ = -5952 | gX = -956 | gY = -413 | gZ = -225
aX = 16320 | aY = -372 | aZ = -5764 | gX = -733 | gY = 139 | gZ = 39
aX = 16380 | aY = -276 | aZ = -5984 | gX = -366 | gY = -222 | gZ = 433
aX = 16652 | aY = -368 | aZ = -6308 | gX = -711 | gY = -157 | gZ = 34
aX = 16492 | aY = -796 | aZ = -6084 | gX = -814 | gY = -46 | gZ = 263
"""
data2 = """
aX = 14444 | aY = -1812 | aZ = -9156 | gX = -802 | gY = 301 | gZ = 393
aX = 15220 | aY = -2360 | aZ = -8252 | gX = -650 | gY = 170 | gZ = 754
aX = 15796 | aY = -2580 | aZ = -8132 | gX = -220 | gY = 216 | gZ = 413
aX = 15444 | aY = -1916 | aZ = -7672 | gX = 555 | gY = 720 | gZ = -303
aX = 17584 | aY = -2112 | aZ = -5632 | gX = -334 | gY = 1623 | gZ = 682
aX = 16872 | aY = -1292 | aZ = -4020 | gX = -920 | gY = 866 | gZ = 754
aX = 17836 | aY = -2132 | aZ = -3132 | gX = -412 | gY = -430 | gZ = 980
aX = 17204 | aY = -2388 | aZ = -4064 | gX = -17 | gY = -503 | gZ = -176
aX = 16948 | aY = -1752 | aZ = -4592 | gX = -728 | gY = 126 | gZ = -185
aX = 16976 | aY = -1956 | aZ = -3956 | gX = -632 | gY = -321 | gZ = 343
aX = 16708 | aY = -2104 | aZ = -4100 | gX = -472 | gY = 28 | gZ = 270
aX = 17416 | aY = -1596 | aZ = -4976 | gX = -578 | gY = 76 | gZ = 693
aX = 16792 | aY = -2072 | aZ = -4144 | gX = -531 | gY = -161 | gZ = 81
aX = 16868 | aY = -2052 | aZ = -4432 | gX = -180 | gY = 23 | gZ = -117
"""
data3 = """
aX = 1808 | aY = 15752 | aZ = -6252 | gX = -397 | gY = -195 | gZ = 127
aX = 1824 | aY = 15808 | aZ = -5828 | gX = 645 | gY = -484 | gZ = -169
aX = 1764 | aY = 15800 | aZ = -6164 | gX = -232 | gY = -221 | gZ = 79
aX = 1940 | aY = 15736 | aZ = -5980 | gX = -498 | gY = -244 | gZ = 79
aX = 1932 | aY = 15744 | aZ = -5924 | gX = -743 | gY = -271 | gZ = 563
aX = 2356 | aY = 15904 | aZ = -5328 | gX = -1039 | gY = 30 | gZ = 202
aX = 2008 | aY = 15824 | aZ = -5700 | gX = 1525 | gY = -1223 | gZ = -363
aX = 1720 | aY = 15652 | aZ = -6516 | gX = -518 | gY = -155 | gZ = 45
aX = 1656 | aY = 15656 | aZ = -6900 | gX = -971 | gY = -19 | gZ = 444
aX = 1584 | aY = 15740 | aZ = -6828 | gX = -196 | gY = -524 | gZ = 354
aX = 1648 | aY = 15828 | aZ = -6364 | gX = -1455 | gY = 432 | gZ = 420
aX = 1712 | aY = 15772 | aZ = -6340 | gX = -1029 | gY = -60 | gZ = 320
aX = 1936 | aY = 15760 | aZ = -5860 | gX = 144 | gY = -435 | gZ = -86
aX = 1652 | aY = 15784 | aZ = -6604 | gX = -793 | gY = -106 | gZ = 233
aX = 1732 | aY = 15088 | aZ = -7396 | gX = 243 | gY = -522 | gZ = 168
aX = 1900 | aY = 15740 | aZ = -6272 | gX = -627 | gY = -78 | gZ = -24
aX = 1860 | aY = 15880 | aZ = -5960 | gX = 28 | gY = -309 | gZ = -27
aX = 1996 | aY = 15892 | aZ = -6052 | gX = 178 | gY = -381 | gZ = 17
aX = 1840 | aY = 15704 | aZ = -6300 | gX = 957 | gY = -729 | gZ = -224
aX = 1636 | aY = 15876 | aZ = -6396 | gX = -153 | gY = -284 | gZ = 129
aX = 1840 | aY = 15748 | aZ = -6280 | gX = -748 | gY = -193 | gZ = 339
aX = 1664 | aY = 15824 | aZ = -6304 | gX = 306 | gY = -572 | gZ = -38
aX = 1856 | aY = 15656 | aZ = -6440 | gX = -1078 | gY = 57 | gZ = 476
aX = 1788 | aY = 15912 | aZ = -6320 | gX = -106 | gY = -538 | gZ = 100
aX = 2168 | aY = 18620 | aZ = -2580 | gX = 8374 | gY = -31530 | gZ = 3929
aX = 1488 | aY = 15636 | aZ = -7104 | gX = -1078 | gY = 95 | gZ = 731
"""

# Define scaling factors
ACCEL_SCALE = 2 / 32768  # Accelerometer scaling factor (g per count)
GYRO_SCALE = 250 / 32768  # Gyroscope scaling factor (°/s per count)
G_CONVERSION = 9.80665  # Conversion from g to m/s²

# Parse the data into arrays
accelerometer_data = []
gyroscope_data = []

for line in data.strip().split('\n'):
    parts = line.strip().split('|')
    ax_raw = float(parts[0].split('=')[1])
    ay_raw = float(parts[1].split('=')[1])
    az_raw = float(parts[2].split('=')[1])
    gx_raw = float(parts[3].split('=')[1])
    gy_raw = float(parts[4].split('=')[1])
    gz_raw = float(parts[5].split('=')[1])

    # Convert raw accelerometer data to m/s²
    ax = ax_raw * ACCEL_SCALE * G_CONVERSION
    ay = ay_raw * ACCEL_SCALE * G_CONVERSION
    az = az_raw * ACCEL_SCALE * G_CONVERSION

    # Convert raw gyroscope data to radians per second
    gx = np.deg2rad(gx_raw * GYRO_SCALE)
    gy = np.deg2rad(gy_raw * GYRO_SCALE)
    gz = np.deg2rad(gz_raw * GYRO_SCALE)

    print("Raw accelerometer data:", ax_raw, ay_raw, az_raw)
    print("Scaled accelerometer data (m/s²):", ax, ay, az)

    accelerometer_data.append([ax, ay, az])
    gyroscope_data.append([gx, gy, gz])

accelerometer_data = np.array(accelerometer_data)
gyroscope_data = np.array(gyroscope_data)


dt = 0.5  # 500 ms delay

num_samples = len(accelerometer_data)

# Gravity vector in fixed frame
g_fixed = np.array([9.80665, 0, 0])  # Gravity in m/s²
# sensor is along teh postoive x axis for some reason, so crecualate the vector

# Compute initial orientation using the first accelerometer reading
acc_initial = accelerometer_data[0]
if np.linalg.norm(acc_initial) == 0:
    raise ValueError("Initial accelerometer reading is zero; cannot compute initial orientation.")
acc_initial_normalized = acc_initial / np.linalg.norm(acc_initial)
g_fixed_normalized = g_fixed / np.linalg.norm(g_fixed)
initial_orientation = R.align_vectors([g_fixed_normalized], [acc_initial_normalized])[0]
orientations = [initial_orientation]

positions = [np.zeros(3)]
velocities = [np.zeros(3)]

for i in range(1, num_samples):
    # Update orientation
    omega = gyroscope_data[i]
    delta_theta = omega * dt
    delta_rotation = R.from_rotvec(delta_theta)
    current_orientation = orientations[-1] * delta_rotation
    orientations.append(current_orientation)

    # Rotate accelerometer reading to the fixed frame
    acc = accelerometer_data[i]
    acc_fixed = current_orientation.apply(acc)

    # Subtract gravity
    acc_linear = acc_fixed - g_fixed

    # Update velocity and position
    v = velocities[-1] + acc_linear * dt
    velocities.append(v)
    p = positions[-1] + v * dt
    positions.append(p)

# Convert positions to a NumPy array for plotting
positions = np.array(positions)

# # Plotting the trajectory
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], marker='o')
#
# ax.set_xlabel('X Position (m)')
# ax.set_ylabel('Y Position (m)')
# ax.set_zlabel('Z Position (m)')
# ax.set_title('3D Trajectory of Gyroscope')
#
# # also plot the XY, XZ, and YZ projections
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
# ax2.plot(positions[:, 0], positions[:, 1], marker='o')
# ax2.set_xlabel('X Position (m)')
# ax2.set_ylabel('Y Position (m)')
# ax2.set_title('XY Projection of Gyroscope')
#
# fig3 = plt.figure()
# ax3 = fig3.add_subplot(111)
# ax3.plot(positions[:, 0], positions[:, 2], marker='o')
# ax3.set_xlabel('X Position (m)')
# ax3.set_ylabel('Z Position (m)')
# ax3.set_title('XZ Projection of Gyroscope')
#
# fig4 = plt.figure()
# ax4 = fig4.add_subplot(111)
# ax4.plot(positions[:, 1], positions[:, 2], marker='o')
# ax4.set_xlabel('Y Position (m)')
# ax4.set_ylabel('Z Position (m)')
# ax4.set_title('YZ Projection of Gyroscope')

# Compute the overall minimum and maximum across all axes
overall_min = np.min(positions)
overall_max = np.max(positions)

# Define the common limits for all axes
common_lim = (overall_min, overall_max)

# Plotting the 3D trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], marker='o')

ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_zlabel('Z Position (m)')
ax.set_title('3D Trajectory of Gyroscope')

# Set the axes limits to the common limits
ax.set_xlim(common_lim)
ax.set_ylim(common_lim)
ax.set_zlim(common_lim)

# Function to set the aspect ratio of 3D plot to equal
def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale'''
    ax.set_box_aspect([1,1,1])  # For Matplotlib versions 3.3.0 and newer

# Set the aspect ratio to equal
set_axes_equal(ax)

# Plotting the XY projection
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(positions[:, 0], positions[:, 1], marker='o')
ax2.set_xlabel('X Position (m)')
ax2.set_ylabel('Y Position (m)')
ax2.set_title('XY Projection of Gyroscope')

# Set the axes limits and aspect ratio
ax2.set_xlim(common_lim)
ax2.set_ylim(common_lim)
ax2.set_aspect('equal', 'box')

# Plotting the XZ projection
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.plot(positions[:, 0], positions[:, 2], marker='o')
ax3.set_xlabel('X Position (m)')
ax3.set_ylabel('Z Position (m)')
ax3.set_title('XZ Projection of Gyroscope')

ax3.set_xlim(common_lim)
ax3.set_ylim(common_lim)
ax3.set_aspect('equal', 'box')

# Plotting the YZ projection
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.plot(positions[:, 1], positions[:, 2], marker='o')
ax4.set_xlabel('Y Position (m)')
ax4.set_ylabel('Z Position (m)')
ax4.set_title('YZ Projection of Gyroscope')

ax4.set_xlim(common_lim)
ax4.set_ylim(common_lim)
ax4.set_aspect('equal', 'box')

# now plot x y z separately vs time with a standard position axis
time = np.arange(num_samples) * dt

fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
ax5.plot(time, positions[:, 0], label='X Position')
ax5.plot(time, positions[:, 1], label='Y Position')
ax5.plot(time, positions[:, 2], label='Z Position')
ax5.set_xlabel('Time (s)')
ax5.set_ylabel('Position (m)')
ax5.set_title('Position vs Time')
ax5.legend()



plt.show()