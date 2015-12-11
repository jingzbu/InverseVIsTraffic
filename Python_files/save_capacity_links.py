from load_dicts import *
from util import *


tmc_set_link_1_1 = [i for i in tmc_list_link_1 if ('P' in i or '+' in i)]
tmc_set_link_1_2 = [i for i in tmc_list_link_1 if ('N' in i or '-' in i)]
AM_capac_link_1_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_1_1])
AM_capac_link_1_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_1_2])
MD_capac_link_1_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_1_1])
MD_capac_link_1_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_1_2])
PM_capac_link_1_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_1_1])
PM_capac_link_1_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_1_2])
NT_capac_link_1_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_1_1])
NT_capac_link_1_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_1_2])

tmc_set_link_2_1 = [i for i in tmc_list_link_2 if ('P' in i or '+' in i)]
tmc_set_link_2_2 = [i for i in tmc_list_link_2 if ('N' in i or '-' in i)]
AM_capac_link_2_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_2_1])
AM_capac_link_2_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_2_2])
MD_capac_link_2_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_2_1])
MD_capac_link_2_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_2_2])
PM_capac_link_2_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_2_1])
PM_capac_link_2_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_2_2])
NT_capac_link_2_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_2_1])
NT_capac_link_2_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_2_2])

tmc_set_link_3_1 = [i for i in tmc_list_link_3 if ('P' in i or '+' in i)]
tmc_set_link_3_2 = [i for i in tmc_list_link_3 if ('N' in i or '-' in i)]
AM_capac_link_3_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_3_1])
AM_capac_link_3_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_3_2])
MD_capac_link_3_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_3_1])
MD_capac_link_3_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_3_2])
PM_capac_link_3_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_3_1])
PM_capac_link_3_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_3_2])
NT_capac_link_3_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_3_1])
NT_capac_link_3_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_3_2])

tmc_set_link_4_1 = [i for i in tmc_list_link_4 if ('P' in i or '+' in i)]
tmc_set_link_4_2 = [i for i in tmc_list_link_4 if ('N' in i or '-' in i)]
AM_capac_link_4_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_4_1])
AM_capac_link_4_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_4_2])
MD_capac_link_4_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_4_1])
MD_capac_link_4_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_4_2])
PM_capac_link_4_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_4_1])
PM_capac_link_4_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_4_2])
NT_capac_link_4_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_4_1])
NT_capac_link_4_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_4_2])

tmc_set_link_5_1 = [i for i in tmc_list_link_5 if ('P' in i or '+' in i)]
tmc_set_link_5_2 = [i for i in tmc_list_link_5 if ('N' in i or '-' in i)]
AM_capac_link_5_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_5_1])
AM_capac_link_5_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_5_2])
MD_capac_link_5_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_5_1])
MD_capac_link_5_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_5_2])
PM_capac_link_5_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_5_1])
PM_capac_link_5_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_5_2])
NT_capac_link_5_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_5_1])
NT_capac_link_5_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_5_2])

tmc_set_link_6_1 = [i for i in tmc_list_link_6 if ('P' in i or '+' in i)]
tmc_set_link_6_2 = [i for i in tmc_list_link_6 if ('N' in i or '-' in i)]
AM_capac_link_6_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_6_1])
AM_capac_link_6_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_6_2])
MD_capac_link_6_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_6_1])
MD_capac_link_6_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_6_2])
PM_capac_link_6_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_6_1])
PM_capac_link_6_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_6_2])
NT_capac_link_6_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_6_1])
NT_capac_link_6_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_6_2])

tmc_set_link_7_1 = [i for i in tmc_list_link_7 if ('P' in i or '+' in i)]
tmc_set_link_7_2 = [i for i in tmc_list_link_7 if ('N' in i or '-' in i)]
AM_capac_link_7_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_7_1])
AM_capac_link_7_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_7_2])
MD_capac_link_7_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_7_1])
MD_capac_link_7_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_7_2])
PM_capac_link_7_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_7_1])
PM_capac_link_7_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_7_2])
NT_capac_link_7_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_7_1])
NT_capac_link_7_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_7_2])

tmc_set_link_8_1 = [i for i in tmc_list_link_8 if ('P' in i or '+' in i)]
tmc_set_link_8_2 = [i for i in tmc_list_link_8 if ('N' in i or '-' in i)]
AM_capac_link_8_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_8_1])
AM_capac_link_8_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_8_2])
MD_capac_link_8_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_8_1])
MD_capac_link_8_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_8_2])
PM_capac_link_8_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_8_1])
PM_capac_link_8_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_8_2])
NT_capac_link_8_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_8_1])
NT_capac_link_8_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_8_2])

tmc_set_link_9_1 = [i for i in tmc_list_link_9 if ('P' in i or '+' in i)]
tmc_set_link_9_2 = [i for i in tmc_list_link_9 if ('N' in i or '-' in i)]
AM_capac_link_9_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_9_1])
AM_capac_link_9_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_9_2])
MD_capac_link_9_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_9_1])
MD_capac_link_9_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_9_2])
PM_capac_link_9_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_9_1])
PM_capac_link_9_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_9_2])
NT_capac_link_9_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_9_1])
NT_capac_link_9_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_9_2])

tmc_set_link_10_1 = [i for i in tmc_list_link_10 if ('P' in i or '+' in i)]
tmc_set_link_10_2 = [i for i in tmc_list_link_10 if ('N' in i or '-' in i)]
AM_capac_link_10_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_10_1])
AM_capac_link_10_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_10_2])
MD_capac_link_10_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_10_1])
MD_capac_link_10_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_10_2])
PM_capac_link_10_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_10_1])
PM_capac_link_10_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_10_2])
NT_capac_link_10_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_10_1])
NT_capac_link_10_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_10_2])

tmc_set_link_11_1 = [i for i in tmc_list_link_11 if ('P' in i or '+' in i)]
tmc_set_link_11_2 = [i for i in tmc_list_link_11 if ('N' in i or '-' in i)]
AM_capac_link_11_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_11_1])
AM_capac_link_11_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_11_2])
MD_capac_link_11_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_11_1])
MD_capac_link_11_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_11_2])
PM_capac_link_11_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_11_1])
PM_capac_link_11_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_11_2])
NT_capac_link_11_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_11_1])
NT_capac_link_11_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_11_2])

tmc_set_link_12_1 = [i for i in tmc_list_link_12 if ('P' in i or '+' in i)]
tmc_set_link_12_2 = [i for i in tmc_list_link_12 if ('N' in i or '-' in i)]
AM_capac_link_12_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_12_1])
AM_capac_link_12_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_12_2])
MD_capac_link_12_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_12_1])
MD_capac_link_12_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_12_2])
PM_capac_link_12_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_12_1])
PM_capac_link_12_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_12_2])
NT_capac_link_12_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_12_1])
NT_capac_link_12_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_12_2])

tmc_set_link_13_1 = [i for i in tmc_list_link_13 if ('P' in i or '+' in i)]
tmc_set_link_13_2 = [i for i in tmc_list_link_13 if ('N' in i or '-' in i)]
AM_capac_link_13_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_13_1])
AM_capac_link_13_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_13_2])
MD_capac_link_13_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_13_1])
MD_capac_link_13_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_13_2])
PM_capac_link_13_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_13_1])
PM_capac_link_13_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_13_2])
NT_capac_link_13_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_13_1])
NT_capac_link_13_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_13_2])

tmc_set_link_14_1 = [i for i in tmc_list_link_14 if ('P' in i or '+' in i)]
tmc_set_link_14_2 = [i for i in tmc_list_link_14 if ('N' in i or '-' in i)]
AM_capac_link_14_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_14_1])
AM_capac_link_14_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_14_2])
MD_capac_link_14_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_14_1])
MD_capac_link_14_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_14_2])
PM_capac_link_14_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_14_1])
PM_capac_link_14_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_14_2])
NT_capac_link_14_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_14_1])
NT_capac_link_14_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_14_2])

tmc_set_link_15_1 = [i for i in tmc_list_link_15 if ('P' in i or '+' in i)]
tmc_set_link_15_2 = [i for i in tmc_list_link_15 if ('N' in i or '-' in i)]
AM_capac_link_15_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_15_1])
AM_capac_link_15_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_15_2])
MD_capac_link_15_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_15_1])
MD_capac_link_15_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_15_2])
PM_capac_link_15_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_15_1])
PM_capac_link_15_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_15_2])
NT_capac_link_15_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_15_1])
NT_capac_link_15_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_15_2])

tmc_set_link_16_1 = [i for i in tmc_list_link_16 if ('P' in i or '+' in i)]
tmc_set_link_16_2 = [i for i in tmc_list_link_16 if ('N' in i or '-' in i)]
AM_capac_link_16_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_16_1])
AM_capac_link_16_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_16_2])
MD_capac_link_16_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_16_1])
MD_capac_link_16_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_16_2])
PM_capac_link_16_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_16_1])
PM_capac_link_16_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_16_2])
NT_capac_link_16_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_16_1])
NT_capac_link_16_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_16_2])

tmc_set_link_17_1 = [i for i in tmc_list_link_17 if ('P' in i or '+' in i)]
tmc_set_link_17_2 = [i for i in tmc_list_link_17 if ('N' in i or '-' in i)]
AM_capac_link_17_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_17_1])
AM_capac_link_17_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_17_2])
MD_capac_link_17_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_17_1])
MD_capac_link_17_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_17_2])
PM_capac_link_17_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_17_1])
PM_capac_link_17_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_17_2])
NT_capac_link_17_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_17_1])
NT_capac_link_17_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_17_2])

tmc_set_link_18_1 = [i for i in tmc_list_link_18 if ('P' in i or '+' in i)]
tmc_set_link_18_2 = [i for i in tmc_list_link_18 if ('N' in i or '-' in i)]
AM_capac_link_18_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_18_1])
AM_capac_link_18_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_18_2])
MD_capac_link_18_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_18_1])
MD_capac_link_18_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_18_2])
PM_capac_link_18_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_18_1])
PM_capac_link_18_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_18_2])
NT_capac_link_18_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_18_1])
NT_capac_link_18_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_18_2])

tmc_set_link_19_1 = [i for i in tmc_list_link_19 if ('P' in i or '+' in i)]
tmc_set_link_19_2 = [i for i in tmc_list_link_19 if ('N' in i or '-' in i)]
AM_capac_link_19_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_19_1])
AM_capac_link_19_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_19_2])
MD_capac_link_19_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_19_1])
MD_capac_link_19_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_19_2])
PM_capac_link_19_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_19_1])
PM_capac_link_19_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_19_2])
NT_capac_link_19_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_19_1])
NT_capac_link_19_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_19_2])

tmc_set_link_20_1 = [i for i in tmc_list_link_20 if ('P' in i or '+' in i)]
tmc_set_link_20_2 = [i for i in tmc_list_link_20 if ('N' in i or '-' in i)]
AM_capac_link_20_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_20_1])
AM_capac_link_20_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_20_2])
MD_capac_link_20_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_20_1])
MD_capac_link_20_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_20_2])
PM_capac_link_20_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_20_1])
PM_capac_link_20_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_20_2])
NT_capac_link_20_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_20_1])
NT_capac_link_20_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_20_2])

tmc_set_link_21_1 = [i for i in tmc_list_link_21 if ('P' in i or '+' in i)]
tmc_set_link_21_2 = [i for i in tmc_list_link_21 if ('N' in i or '-' in i)]
AM_capac_link_21_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_21_1])
AM_capac_link_21_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_21_2])
MD_capac_link_21_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_21_1])
MD_capac_link_21_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_21_2])
PM_capac_link_21_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_21_1])
PM_capac_link_21_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_21_2])
NT_capac_link_21_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_21_1])
NT_capac_link_21_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_21_2])

tmc_set_link_22_1 = [i for i in tmc_list_link_22 if ('P' in i or '+' in i)]
tmc_set_link_22_2 = [i for i in tmc_list_link_22 if ('N' in i or '-' in i)]
AM_capac_link_22_1 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_22_1])
AM_capac_link_22_2 = sum([tmc_capac_dict_AM[i] for i in tmc_set_link_22_2])
MD_capac_link_22_1 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_22_1])
MD_capac_link_22_2 = sum([tmc_capac_dict_MD[i] for i in tmc_set_link_22_2])
PM_capac_link_22_1 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_22_1])
PM_capac_link_22_2 = sum([tmc_capac_dict_PM[i] for i in tmc_set_link_22_2])
NT_capac_link_22_1 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_22_1])
NT_capac_link_22_2 = sum([tmc_capac_dict_NT[i] for i in tmc_set_link_22_2])


# instantiation of Link class
link_1_1 = Link_with_Free_Flow_Time(1, 2, tmc_set_link_1_1, AM_capac_link_1_1, MD_capac_link_1_1, \
		 PM_capac_link_1_1, NT_capac_link_1_1, 0, \
		 0, 0, 0, 0)

link_1_2 = Link_with_Free_Flow_Time(2, 1, tmc_set_link_1_2, AM_capac_link_1_2, MD_capac_link_1_2, \
                 PM_capac_link_1_2, NT_capac_link_1_2, 0, \
		 0, 0, 0, 0)

link_2_1 = Link_with_Free_Flow_Time(10, 11, tmc_set_link_2_1, AM_capac_link_2_1, MD_capac_link_2_1, \
                 PM_capac_link_2_1, NT_capac_link_2_1, 0, \
                 0, 0, 0, 0)

link_2_2 = Link_with_Free_Flow_Time(11, 10, tmc_set_link_2_2, AM_capac_link_2_2, MD_capac_link_2_2, \
                 PM_capac_link_2_2, NT_capac_link_2_2, 0, \
                 0, 0, 0, 0)

link_3_1 = Link_with_Free_Flow_Time(17, 18, tmc_set_link_3_1, AM_capac_link_3_1, MD_capac_link_3_1, \
                 PM_capac_link_3_1, NT_capac_link_3_1, 0, \
                 0, 0, 0, 0)

link_3_2 = Link_with_Free_Flow_Time(18, 17, tmc_set_link_3_2, AM_capac_link_3_2, MD_capac_link_3_2, \
                 PM_capac_link_3_2, NT_capac_link_3_2, 0, \
                 0, 0, 0, 0)

link_4_1 = Link_with_Free_Flow_Time(4, 17, tmc_set_link_4_1, AM_capac_link_4_1, MD_capac_link_4_1, \
                 PM_capac_link_4_1, NT_capac_link_4_1, 0, \
                 0, 0, 0, 0)

link_4_2 = Link_with_Free_Flow_Time(17, 4, tmc_set_link_4_2, AM_capac_link_4_2, MD_capac_link_4_2, \
                 PM_capac_link_4_2, NT_capac_link_4_2, 0, \
                 0, 0, 0, 0)

link_5_1 = Link_with_Free_Flow_Time(8, 15, tmc_set_link_5_1, AM_capac_link_5_1, MD_capac_link_5_1, \
                 PM_capac_link_5_1, NT_capac_link_5_1, 0, \
                 0, 0, 0, 0)

link_5_2 = Link_with_Free_Flow_Time(15, 8, tmc_set_link_5_2, AM_capac_link_5_2, MD_capac_link_5_2, \
                 PM_capac_link_5_2, NT_capac_link_5_2, 0, \
                 0, 0, 0, 0)

link_6_1 = Link_with_Free_Flow_Time(5, 8, tmc_set_link_6_1, AM_capac_link_6_1, MD_capac_link_6_1, \
                 PM_capac_link_6_1, NT_capac_link_6_1, 0, \
                 0, 0, 0, 0)

link_6_2 = Link_with_Free_Flow_Time(8, 5, tmc_set_link_6_2, AM_capac_link_6_2, MD_capac_link_6_2, \
                 PM_capac_link_6_2, NT_capac_link_6_2, 0, \
                 0, 0, 0, 0)

link_7_1 = Link_with_Free_Flow_Time(4, 5, tmc_set_link_7_1, AM_capac_link_7_1, MD_capac_link_7_1, \
                 PM_capac_link_7_1, NT_capac_link_7_1, 0, \
                 0, 0, 0, 0)

link_7_2 = Link_with_Free_Flow_Time(5, 4, tmc_set_link_7_2, AM_capac_link_7_2, MD_capac_link_7_2, \
                 PM_capac_link_7_2, NT_capac_link_7_2, 0, \
                 0, 0, 0, 0)

link_8_1 = Link_with_Free_Flow_Time(15, 17, tmc_set_link_8_1, AM_capac_link_8_1, MD_capac_link_8_1, \
                 PM_capac_link_8_1, NT_capac_link_8_1, 0, \
                 0, 0, 0, 0)

link_8_2 = Link_with_Free_Flow_Time(17, 15, tmc_set_link_8_2, AM_capac_link_8_2, MD_capac_link_8_2, \
                 PM_capac_link_8_2, NT_capac_link_8_2, 0, \
                 0, 0, 0, 0)

link_9_1 = Link_with_Free_Flow_Time(10, 15, tmc_set_link_9_1, AM_capac_link_9_1, MD_capac_link_9_1, \
                 PM_capac_link_9_1, NT_capac_link_9_1, 0, \
                 0, 0, 0, 0)

link_9_2 = Link_with_Free_Flow_Time(15, 10, tmc_set_link_9_2, AM_capac_link_9_2, MD_capac_link_9_2, \
                 PM_capac_link_9_2, NT_capac_link_9_2, 0, \
                 0, 0, 0, 0)

link_10_1 = Link_with_Free_Flow_Time(9, 10, tmc_set_link_10_1, AM_capac_link_10_1, MD_capac_link_10_1, \
                 PM_capac_link_10_1, NT_capac_link_10_1, 0, \
                 0, 0, 0, 0)

link_10_2 = Link_with_Free_Flow_Time(10, 9, tmc_set_link_10_2, AM_capac_link_10_2, MD_capac_link_10_2, \
                 PM_capac_link_10_2, NT_capac_link_10_2, 0, \
                 0, 0, 0, 0)

link_11_1 = Link_with_Free_Flow_Time(8, 9, tmc_set_link_11_1, AM_capac_link_11_1, MD_capac_link_11_1, \
                 PM_capac_link_11_1, NT_capac_link_11_1, 0, \
                 0, 0, 0, 0)

link_11_2 = Link_with_Free_Flow_Time(9, 8, tmc_set_link_11_2, AM_capac_link_11_2, MD_capac_link_11_2, \
                 PM_capac_link_11_2, NT_capac_link_11_2, 0, \
                 0, 0, 0, 0)

link_12_1 = Link_with_Free_Flow_Time(7, 9, tmc_set_link_12_1, AM_capac_link_12_1, MD_capac_link_12_1, \
                 PM_capac_link_12_1, NT_capac_link_12_1, 0, \
                 0, 0, 0, 0)

link_12_2 = Link_with_Free_Flow_Time(9, 7, tmc_set_link_12_2, AM_capac_link_12_2, MD_capac_link_12_2, \
                 PM_capac_link_12_2, NT_capac_link_12_2, 0, \
                 0, 0, 0, 0)

link_13_1 = Link_with_Free_Flow_Time(7, 8, tmc_set_link_13_1, AM_capac_link_13_1, MD_capac_link_13_1, \
                 PM_capac_link_13_1, NT_capac_link_13_1, 0, \
                 0, 0, 0, 0)

link_13_2 = Link_with_Free_Flow_Time(8, 7, tmc_set_link_13_2, AM_capac_link_13_2, MD_capac_link_13_2, \
                 PM_capac_link_13_2, NT_capac_link_13_2, 0, \
                 0, 0, 0, 0)

link_14_1 = Link_with_Free_Flow_Time(5, 7, tmc_set_link_14_1, AM_capac_link_14_1, MD_capac_link_14_1, \
                 PM_capac_link_14_1, NT_capac_link_14_1, 0, \
                 0, 0, 0, 0)

link_14_2 = Link_with_Free_Flow_Time(7, 5, tmc_set_link_14_2, AM_capac_link_14_2, MD_capac_link_14_2, \
                 PM_capac_link_14_2, NT_capac_link_14_2, 0, \
                 0, 0, 0, 0)

link_15_1 = Link_with_Free_Flow_Time(1, 5, tmc_set_link_15_1, AM_capac_link_15_1, MD_capac_link_15_1, \
                 PM_capac_link_15_1, NT_capac_link_15_1, 0, \
                 0, 0, 0, 0)

link_15_2 = Link_with_Free_Flow_Time(5, 1, tmc_set_link_15_2, AM_capac_link_15_2, MD_capac_link_15_2, \
                 PM_capac_link_15_2, NT_capac_link_15_2, 0, \
                 0, 0, 0, 0)

link_16_1 = Link_with_Free_Flow_Time(2, 4, tmc_set_link_16_1, AM_capac_link_16_1, MD_capac_link_16_1, \
                 PM_capac_link_16_1, NT_capac_link_16_1, 0, \
                 0, 0, 0, 0)

link_16_2 = Link_with_Free_Flow_Time(4, 2, tmc_set_link_16_2, AM_capac_link_16_2, MD_capac_link_16_2, \
                 PM_capac_link_16_2, NT_capac_link_16_2, 0, \
                 0, 0, 0, 0)

link_17_1 = Link_with_Free_Flow_Time(3, 4, tmc_set_link_17_1, AM_capac_link_17_1, MD_capac_link_17_1, \
                 PM_capac_link_17_1, NT_capac_link_17_1, 0, \
                 0, 0, 0, 0)

link_17_2 = Link_with_Free_Flow_Time(4, 3, tmc_set_link_17_2, AM_capac_link_17_2, MD_capac_link_17_2, \
                 PM_capac_link_17_2, NT_capac_link_17_2, 0, \
                 0, 0, 0, 0)

link_18_1 = Link_with_Free_Flow_Time(6, 7, tmc_set_link_18_1, AM_capac_link_18_1, MD_capac_link_18_1, \
                 PM_capac_link_18_1, NT_capac_link_18_1, 0, \
                 0, 0, 0, 0)

link_18_2 = Link_with_Free_Flow_Time(7, 6, tmc_set_link_18_2, AM_capac_link_18_2, MD_capac_link_18_2, \
                 PM_capac_link_18_2, NT_capac_link_18_2, 0, \
                 0, 0, 0, 0)

link_19_1 = Link_with_Free_Flow_Time(15, 16, tmc_set_link_19_1, AM_capac_link_19_1, MD_capac_link_19_1, \
                 PM_capac_link_19_1, NT_capac_link_19_1, 0, \
                 0, 0, 0, 0)

link_19_2 = Link_with_Free_Flow_Time(16, 15, tmc_set_link_19_2, AM_capac_link_19_2, MD_capac_link_19_2, \
                 PM_capac_link_19_2, NT_capac_link_19_2, 0, \
                 0, 0, 0, 0)

link_20_1 = Link_with_Free_Flow_Time(12, 13, tmc_set_link_20_1, AM_capac_link_20_1, MD_capac_link_20_1, \
                 PM_capac_link_20_1, NT_capac_link_20_1, 0, \
                 0, 0, 0, 0)

link_20_2 = Link_with_Free_Flow_Time(13, 12, tmc_set_link_20_2, AM_capac_link_20_2, MD_capac_link_20_2, \
                 PM_capac_link_20_2, NT_capac_link_20_2, 0, \
                 0, 0, 0, 0)

link_21_1 = Link_with_Free_Flow_Time(12, 14, tmc_set_link_21_1, AM_capac_link_21_1, MD_capac_link_21_1, \
                 PM_capac_link_21_1, NT_capac_link_21_1, 0, \
                 0, 0, 0, 0)

link_21_2 = Link_with_Free_Flow_Time(14, 12, tmc_set_link_21_2, AM_capac_link_21_2, MD_capac_link_21_2, \
                 PM_capac_link_21_2, NT_capac_link_21_2, 0, \
                 0, 0, 0, 0)

link_22_1 = Link_with_Free_Flow_Time(10, 12, tmc_set_link_22_1, AM_capac_link_22_1, MD_capac_link_22_1, \
                 PM_capac_link_22_1, NT_capac_link_22_1, 0, \
                 0, 0, 0, 0)

link_22_2 = Link_with_Free_Flow_Time(12, 10, tmc_set_link_22_2, AM_capac_link_22_2, MD_capac_link_22_2, \
                 PM_capac_link_22_2, NT_capac_link_22_2, 0, \
                 0, 0, 0, 0)

zdump([link_1_1, link_1_2, link_2_1, link_2_2, link_3_1, link_3_2, \
	link_4_1, link_4_2, link_5_1, link_5_2, link_6_1, link_6_2, \
	link_7_1, link_7_2, link_8_1, link_8_2, link_9_1, link_9_2, \
	link_10_1, link_10_2, link_11_1, link_11_2, link_12_1, link_12_2, \
	link_13_1, link_13_2, link_14_1, link_14_2, link_15_1, link_15_2, \
	link_16_1, link_16_2, link_17_1, link_17_2, link_18_1, link_18_2, \
	link_19_1, link_19_2, link_20_1, link_20_2, link_21_1, link_21_2, \
	link_22_1, link_22_2], '../temp_files/links_with_capac.pkz')
