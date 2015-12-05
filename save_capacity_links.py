from util import *

tmc_list_link_1, tmc_list_link_2, tmc_list_link_3, tmc_list_link_4, tmc_list_link_5, \
	tmc_list_link_6, tmc_list_link_7, tmc_list_link_8, tmc_list_link_9, tmc_list_link_10, \
	tmc_list_link_11, tmc_list_link_12, tmc_list_link_13, tmc_list_link_14, \
	tmc_list_link_15, tmc_list_link_16, tmc_list_link_17, tmc_list_link_18, \
	tmc_list_link_19, tmc_list_link_20, tmc_list_link_21, tmc_list_link_22 = zload('./temp_files/tmc_list_links.pkz')

tmc_capac_dict_AM, tmc_capac_dict_MD, tmc_capac_dict_PM, \
    tmc_capac_dict_NT, tmc_length_dict = zload('./temp_files/link_dicts.pkz')

AM_capac_link_1_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_1 if ('P' in i or '+' in i)])
AM_capac_link_1_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_1 if ('N' in i or '-' in i)])
MD_capac_link_1_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_1 if ('P' in i or '+' in i)])
MD_capac_link_1_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_1 if ('N' in i or '-' in i)])
PM_capac_link_1_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_1 if ('P' in i or '+' in i)])
PM_capac_link_1_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_1 if ('N' in i or '-' in i)])
NT_capac_link_1_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_1 if ('P' in i or '+' in i)])
NT_capac_link_1_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_1 if ('N' in i or '-' in i)])

AM_capac_link_2_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_2 if ('P' in i or '+' in i)])
AM_capac_link_2_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_2 if ('N' in i or '-' in i)])
MD_capac_link_2_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_2 if ('P' in i or '+' in i)])
MD_capac_link_2_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_2 if ('N' in i or '-' in i)])
PM_capac_link_2_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_2 if ('P' in i or '+' in i)])
PM_capac_link_2_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_2 if ('N' in i or '-' in i)])
NT_capac_link_2_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_2 if ('P' in i or '+' in i)])
NT_capac_link_2_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_2 if ('N' in i or '-' in i)])

AM_capac_link_3_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_3 if ('P' in i or '+' in i)])
AM_capac_link_3_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_3 if ('N' in i or '-' in i)])
MD_capac_link_3_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_3 if ('P' in i or '+' in i)])
MD_capac_link_3_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_3 if ('N' in i or '-' in i)])
PM_capac_link_3_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_3 if ('P' in i or '+' in i)])
PM_capac_link_3_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_3 if ('N' in i or '-' in i)])
NT_capac_link_3_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_3 if ('P' in i or '+' in i)])
NT_capac_link_3_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_3 if ('N' in i or '-' in i)])

AM_capac_link_4_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_4 if ('P' in i or '+' in i)])
AM_capac_link_4_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_4 if ('N' in i or '-' in i)])
MD_capac_link_4_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_4 if ('P' in i or '+' in i)])
MD_capac_link_4_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_4 if ('N' in i or '-' in i)])
PM_capac_link_4_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_4 if ('P' in i or '+' in i)])
PM_capac_link_4_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_4 if ('N' in i or '-' in i)])
NT_capac_link_4_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_4 if ('P' in i or '+' in i)])
NT_capac_link_4_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_4 if ('N' in i or '-' in i)])

AM_capac_link_5_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_5 if ('P' in i or '+' in i)])
AM_capac_link_5_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_5 if ('N' in i or '-' in i)])
MD_capac_link_5_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_5 if ('P' in i or '+' in i)])
MD_capac_link_5_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_5 if ('N' in i or '-' in i)])
PM_capac_link_5_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_5 if ('P' in i or '+' in i)])
PM_capac_link_5_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_5 if ('N' in i or '-' in i)])
NT_capac_link_5_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_5 if ('P' in i or '+' in i)])
NT_capac_link_5_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_5 if ('N' in i or '-' in i)])

AM_capac_link_6_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_6 if ('P' in i or '+' in i)])
AM_capac_link_6_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_6 if ('N' in i or '-' in i)])
MD_capac_link_6_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_6 if ('P' in i or '+' in i)])
MD_capac_link_6_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_6 if ('N' in i or '-' in i)])
PM_capac_link_6_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_6 if ('P' in i or '+' in i)])
PM_capac_link_6_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_6 if ('N' in i or '-' in i)])
NT_capac_link_6_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_6 if ('P' in i or '+' in i)])
NT_capac_link_6_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_6 if ('N' in i or '-' in i)])

AM_capac_link_7_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_7 if ('P' in i or '+' in i)])
AM_capac_link_7_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_7 if ('N' in i or '-' in i)])
MD_capac_link_7_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_7 if ('P' in i or '+' in i)])
MD_capac_link_7_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_7 if ('N' in i or '-' in i)])
PM_capac_link_7_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_7 if ('P' in i or '+' in i)])
PM_capac_link_7_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_7 if ('N' in i or '-' in i)])
NT_capac_link_7_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_7 if ('P' in i or '+' in i)])
NT_capac_link_7_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_7 if ('N' in i or '-' in i)])

AM_capac_link_8_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_8 if ('P' in i or '+' in i)])
AM_capac_link_8_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_8 if ('N' in i or '-' in i)])
MD_capac_link_8_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_8 if ('P' in i or '+' in i)])
MD_capac_link_8_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_8 if ('N' in i or '-' in i)])
PM_capac_link_8_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_8 if ('P' in i or '+' in i)])
PM_capac_link_8_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_8 if ('N' in i or '-' in i)])
NT_capac_link_8_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_8 if ('P' in i or '+' in i)])
NT_capac_link_8_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_8 if ('N' in i or '-' in i)])

AM_capac_link_9_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_9 if ('P' in i or '+' in i)])
AM_capac_link_9_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_9 if ('N' in i or '-' in i)])
MD_capac_link_9_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_9 if ('P' in i or '+' in i)])
MD_capac_link_9_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_9 if ('N' in i or '-' in i)])
PM_capac_link_9_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_9 if ('P' in i or '+' in i)])
PM_capac_link_9_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_9 if ('N' in i or '-' in i)])
NT_capac_link_9_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_9 if ('P' in i or '+' in i)])
NT_capac_link_9_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_9 if ('N' in i or '-' in i)])

AM_capac_link_10_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_10 if ('P' in i or '+' in i)])
AM_capac_link_10_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_10 if ('N' in i or '-' in i)])
MD_capac_link_10_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_10 if ('P' in i or '+' in i)])
MD_capac_link_10_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_10 if ('N' in i or '-' in i)])
PM_capac_link_10_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_10 if ('P' in i or '+' in i)])
PM_capac_link_10_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_10 if ('N' in i or '-' in i)])
NT_capac_link_10_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_10 if ('P' in i or '+' in i)])
NT_capac_link_10_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_10 if ('N' in i or '-' in i)])

AM_capac_link_11_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_11 if ('P' in i or '+' in i)])
AM_capac_link_11_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_11 if ('N' in i or '-' in i)])
MD_capac_link_11_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_11 if ('P' in i or '+' in i)])
MD_capac_link_11_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_11 if ('N' in i or '-' in i)])
PM_capac_link_11_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_11 if ('P' in i or '+' in i)])
PM_capac_link_11_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_11 if ('N' in i or '-' in i)])
NT_capac_link_11_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_11 if ('P' in i or '+' in i)])
NT_capac_link_11_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_11 if ('N' in i or '-' in i)])

AM_capac_link_12_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_12 if ('P' in i or '+' in i)])
AM_capac_link_12_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_12 if ('N' in i or '-' in i)])
MD_capac_link_12_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_12 if ('P' in i or '+' in i)])
MD_capac_link_12_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_12 if ('N' in i or '-' in i)])
PM_capac_link_12_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_12 if ('P' in i or '+' in i)])
PM_capac_link_12_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_12 if ('N' in i or '-' in i)])
NT_capac_link_12_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_12 if ('P' in i or '+' in i)])
NT_capac_link_12_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_12 if ('N' in i or '-' in i)])

AM_capac_link_13_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_13 if ('P' in i or '+' in i)])
AM_capac_link_13_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_13 if ('N' in i or '-' in i)])
MD_capac_link_13_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_13 if ('P' in i or '+' in i)])
MD_capac_link_13_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_13 if ('N' in i or '-' in i)])
PM_capac_link_13_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_13 if ('P' in i or '+' in i)])
PM_capac_link_13_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_13 if ('N' in i or '-' in i)])
NT_capac_link_13_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_13 if ('P' in i or '+' in i)])
NT_capac_link_13_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_13 if ('N' in i or '-' in i)])

AM_capac_link_14_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_14 if ('P' in i or '+' in i)])
AM_capac_link_14_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_14 if ('N' in i or '-' in i)])
MD_capac_link_14_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_14 if ('P' in i or '+' in i)])
MD_capac_link_14_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_14 if ('N' in i or '-' in i)])
PM_capac_link_14_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_14 if ('P' in i or '+' in i)])
PM_capac_link_14_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_14 if ('N' in i or '-' in i)])
NT_capac_link_14_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_14 if ('P' in i or '+' in i)])
NT_capac_link_14_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_14 if ('N' in i or '-' in i)])

AM_capac_link_15_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_15 if ('P' in i or '+' in i)])
AM_capac_link_15_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_15 if ('N' in i or '-' in i)])
MD_capac_link_15_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_15 if ('P' in i or '+' in i)])
MD_capac_link_15_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_15 if ('N' in i or '-' in i)])
PM_capac_link_15_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_15 if ('P' in i or '+' in i)])
PM_capac_link_15_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_15 if ('N' in i or '-' in i)])
NT_capac_link_15_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_15 if ('P' in i or '+' in i)])
NT_capac_link_15_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_15 if ('N' in i or '-' in i)])

AM_capac_link_16_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_16 if ('P' in i or '+' in i)])
AM_capac_link_16_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_16 if ('N' in i or '-' in i)])
MD_capac_link_16_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_16 if ('P' in i or '+' in i)])
MD_capac_link_16_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_16 if ('N' in i or '-' in i)])
PM_capac_link_16_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_16 if ('P' in i or '+' in i)])
PM_capac_link_16_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_16 if ('N' in i or '-' in i)])
NT_capac_link_16_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_16 if ('P' in i or '+' in i)])
NT_capac_link_16_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_16 if ('N' in i or '-' in i)])

AM_capac_link_17_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_17 if ('P' in i or '+' in i)])
AM_capac_link_17_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_17 if ('N' in i or '-' in i)])
MD_capac_link_17_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_17 if ('P' in i or '+' in i)])
MD_capac_link_17_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_17 if ('N' in i or '-' in i)])
PM_capac_link_17_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_17 if ('P' in i or '+' in i)])
PM_capac_link_17_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_17 if ('N' in i or '-' in i)])
NT_capac_link_17_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_17 if ('P' in i or '+' in i)])
NT_capac_link_17_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_17 if ('N' in i or '-' in i)])

AM_capac_link_18_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_18 if ('P' in i or '+' in i)])
AM_capac_link_18_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_18 if ('N' in i or '-' in i)])
MD_capac_link_18_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_18 if ('P' in i or '+' in i)])
MD_capac_link_18_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_18 if ('N' in i or '-' in i)])
PM_capac_link_18_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_18 if ('P' in i or '+' in i)])
PM_capac_link_18_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_18 if ('N' in i or '-' in i)])
NT_capac_link_18_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_18 if ('P' in i or '+' in i)])
NT_capac_link_18_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_18 if ('N' in i or '-' in i)])

AM_capac_link_19_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_19 if ('P' in i or '+' in i)])
AM_capac_link_19_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_19 if ('N' in i or '-' in i)])
MD_capac_link_19_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_19 if ('P' in i or '+' in i)])
MD_capac_link_19_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_19 if ('N' in i or '-' in i)])
PM_capac_link_19_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_19 if ('P' in i or '+' in i)])
PM_capac_link_19_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_19 if ('N' in i or '-' in i)])
NT_capac_link_19_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_19 if ('P' in i or '+' in i)])
NT_capac_link_19_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_19 if ('N' in i or '-' in i)])

AM_capac_link_20_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_20 if ('P' in i or '+' in i)])
AM_capac_link_20_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_20 if ('N' in i or '-' in i)])
MD_capac_link_20_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_20 if ('P' in i or '+' in i)])
MD_capac_link_20_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_20 if ('N' in i or '-' in i)])
PM_capac_link_20_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_20 if ('P' in i or '+' in i)])
PM_capac_link_20_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_20 if ('N' in i or '-' in i)])
NT_capac_link_20_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_20 if ('P' in i or '+' in i)])
NT_capac_link_20_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_20 if ('N' in i or '-' in i)])

AM_capac_link_21_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_21 if ('P' in i or '+' in i)])
AM_capac_link_21_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_21 if ('N' in i or '-' in i)])
MD_capac_link_21_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_21 if ('P' in i or '+' in i)])
MD_capac_link_21_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_21 if ('N' in i or '-' in i)])
PM_capac_link_21_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_21 if ('P' in i or '+' in i)])
PM_capac_link_21_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_21 if ('N' in i or '-' in i)])
NT_capac_link_21_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_21 if ('P' in i or '+' in i)])
NT_capac_link_21_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_21 if ('N' in i or '-' in i)])

AM_capac_link_22_1 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_22 if ('P' in i or '+' in i)])
AM_capac_link_22_2 = sum([tmc_capac_dict_AM[i] for i in tmc_list_link_22 if ('N' in i or '-' in i)])
MD_capac_link_22_1 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_22 if ('P' in i or '+' in i)])
MD_capac_link_22_2 = sum([tmc_capac_dict_MD[i] for i in tmc_list_link_22 if ('N' in i or '-' in i)])
PM_capac_link_22_1 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_22 if ('P' in i or '+' in i)])
PM_capac_link_22_2 = sum([tmc_capac_dict_PM[i] for i in tmc_list_link_22 if ('N' in i or '-' in i)])
NT_capac_link_22_1 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_22 if ('P' in i or '+' in i)])
NT_capac_link_22_2 = sum([tmc_capac_dict_NT[i] for i in tmc_list_link_22 if ('N' in i or '-' in i)])


# instantiation of Link class
link_1_1 = Link(1, 2, AM_capac_link_1_1, MD_capac_link_1_1, \
                 PM_capac_link_1_1, NT_capac_link_1_1, 0, \
                 0, 0, 0, 0)

link_1_2 = Link(2, 1, AM_capac_link_1_2, MD_capac_link_1_2, \
                 PM_capac_link_1_2, NT_capac_link_1_2, 0, \
                 0, 0, 0, 0)

link_2_1 = Link(10, 11, AM_capac_link_2_1, MD_capac_link_2_1, \
                 PM_capac_link_2_1, NT_capac_link_2_1, 0, \
                 0, 0, 0, 0)

link_2_2 = Link(11, 10, AM_capac_link_2_2, MD_capac_link_2_2, \
                 PM_capac_link_2_2, NT_capac_link_2_2, 0, \
                 0, 0, 0, 0)

link_3_1 = Link(17, 18, AM_capac_link_3_1, MD_capac_link_3_1, \
                 PM_capac_link_3_1, NT_capac_link_3_1, 0, \
                 0, 0, 0, 0)

link_3_2 = Link(18, 17, AM_capac_link_3_2, MD_capac_link_3_2, \
                 PM_capac_link_3_2, NT_capac_link_3_2, 0, \
                 0, 0, 0, 0)

link_4_1 = Link(4, 17, AM_capac_link_4_1, MD_capac_link_4_1, \
                 PM_capac_link_4_1, NT_capac_link_4_1, 0, \
                 0, 0, 0, 0)

link_4_2 = Link(17, 4, AM_capac_link_4_2, MD_capac_link_4_2, \
                 PM_capac_link_4_2, NT_capac_link_4_2, 0, \
                 0, 0, 0, 0)

link_5_1 = Link(8, 15, AM_capac_link_5_1, MD_capac_link_5_1, \
                 PM_capac_link_5_1, NT_capac_link_5_1, 0, \
                 0, 0, 0, 0)

link_5_2 = Link(15, 8, AM_capac_link_5_2, MD_capac_link_5_2, \
                 PM_capac_link_5_2, NT_capac_link_5_2, 0, \
                 0, 0, 0, 0)

link_6_1 = Link(5, 8, AM_capac_link_6_1, MD_capac_link_6_1, \
                 PM_capac_link_6_1, NT_capac_link_6_1, 0, \
                 0, 0, 0, 0)

link_6_2 = Link(8, 5, AM_capac_link_6_2, MD_capac_link_6_2, \
                 PM_capac_link_6_2, NT_capac_link_6_2, 0, \
                 0, 0, 0, 0)

link_7_1 = Link(4, 5, AM_capac_link_7_1, MD_capac_link_7_1, \
                 PM_capac_link_7_1, NT_capac_link_7_1, 0, \
                 0, 0, 0, 0)

link_7_2 = Link(5, 4, AM_capac_link_7_2, MD_capac_link_7_2, \
                 PM_capac_link_7_2, NT_capac_link_7_2, 0, \
                 0, 0, 0, 0)

link_8_1 = Link(15, 17, AM_capac_link_8_1, MD_capac_link_8_1, \
                 PM_capac_link_8_1, NT_capac_link_8_1, 0, \
                 0, 0, 0, 0)

link_8_2 = Link(17, 15, AM_capac_link_8_2, MD_capac_link_8_2, \
                 PM_capac_link_8_2, NT_capac_link_8_2, 0, \
                 0, 0, 0, 0)

link_9_1 = Link(10, 15, AM_capac_link_9_1, MD_capac_link_9_1, \
                 PM_capac_link_9_1, NT_capac_link_9_1, 0, \
                 0, 0, 0, 0)

link_9_2 = Link(15, 10, AM_capac_link_9_2, MD_capac_link_9_2, \
                 PM_capac_link_9_2, NT_capac_link_9_2, 0, \
                 0, 0, 0, 0)

link_10_1 = Link(9, 10, AM_capac_link_10_1, MD_capac_link_10_1, \
                 PM_capac_link_10_1, NT_capac_link_10_1, 0, \
                 0, 0, 0, 0)

link_10_2 = Link(10, 9, AM_capac_link_10_2, MD_capac_link_10_2, \
                 PM_capac_link_10_2, NT_capac_link_10_2, 0, \
                 0, 0, 0, 0)

link_11_1 = Link(8, 9, AM_capac_link_11_1, MD_capac_link_11_1, \
                 PM_capac_link_11_1, NT_capac_link_11_1, 0, \
                 0, 0, 0, 0)

link_11_2 = Link(9, 8, AM_capac_link_11_2, MD_capac_link_11_2, \
                 PM_capac_link_11_2, NT_capac_link_11_2, 0, \
                 0, 0, 0, 0)

link_12_1 = Link(7, 9, AM_capac_link_12_1, MD_capac_link_12_1, \
                 PM_capac_link_12_1, NT_capac_link_12_1, 0, \
                 0, 0, 0, 0)

link_12_2 = Link(9, 7, AM_capac_link_12_2, MD_capac_link_12_2, \
                 PM_capac_link_12_2, NT_capac_link_12_2, 0, \
                 0, 0, 0, 0)

link_13_1 = Link(7, 8, AM_capac_link_13_1, MD_capac_link_13_1, \
                 PM_capac_link_13_1, NT_capac_link_13_1, 0, \
                 0, 0, 0, 0)

link_13_2 = Link(8, 7, AM_capac_link_13_2, MD_capac_link_13_2, \
                 PM_capac_link_13_2, NT_capac_link_13_2, 0, \
                 0, 0, 0, 0)

link_14_1 = Link(5, 7, AM_capac_link_14_1, MD_capac_link_14_1, \
                 PM_capac_link_14_1, NT_capac_link_14_1, 0, \
                 0, 0, 0, 0)

link_14_2 = Link(7, 5, AM_capac_link_14_2, MD_capac_link_14_2, \
                 PM_capac_link_14_2, NT_capac_link_14_2, 0, \
                 0, 0, 0, 0)

link_15_1 = Link(1, 5, AM_capac_link_15_1, MD_capac_link_15_1, \
                 PM_capac_link_15_1, NT_capac_link_15_1, 0, \
                 0, 0, 0, 0)

link_15_2 = Link(5, 1, AM_capac_link_15_2, MD_capac_link_15_2, \
                 PM_capac_link_15_2, NT_capac_link_15_2, 0, \
                 0, 0, 0, 0)

link_16_1 = Link(2, 4, AM_capac_link_16_1, MD_capac_link_16_1, \
                 PM_capac_link_16_1, NT_capac_link_16_1, 0, \
                 0, 0, 0, 0)

link_16_2 = Link(4, 2, AM_capac_link_16_2, MD_capac_link_16_2, \
                 PM_capac_link_16_2, NT_capac_link_16_2, 0, \
                 0, 0, 0, 0)

link_17_1 = Link(3, 4, AM_capac_link_17_1, MD_capac_link_17_1, \
                 PM_capac_link_17_1, NT_capac_link_17_1, 0, \
                 0, 0, 0, 0)

link_17_2 = Link(4, 3, AM_capac_link_17_2, MD_capac_link_17_2, \
                 PM_capac_link_17_2, NT_capac_link_17_2, 0, \
                 0, 0, 0, 0)

link_18_1 = Link(6, 7, AM_capac_link_18_1, MD_capac_link_18_1, \
                 PM_capac_link_18_1, NT_capac_link_18_1, 0, \
                 0, 0, 0, 0)

link_18_2 = Link(7, 6, AM_capac_link_18_2, MD_capac_link_18_2, \
                 PM_capac_link_18_2, NT_capac_link_18_2, 0, \
                 0, 0, 0, 0)

link_19_1 = Link(15, 16, AM_capac_link_19_1, MD_capac_link_19_1, \
                 PM_capac_link_19_1, NT_capac_link_19_1, 0, \
                 0, 0, 0, 0)

link_19_2 = Link(16, 15, AM_capac_link_19_2, MD_capac_link_19_2, \
                 PM_capac_link_19_2, NT_capac_link_19_2, 0, \
                 0, 0, 0, 0)

link_20_1 = Link(12, 13, AM_capac_link_20_1, MD_capac_link_20_1, \
                 PM_capac_link_20_1, NT_capac_link_20_1, 0, \
                 0, 0, 0, 0)

link_20_2 = Link(13, 12, AM_capac_link_20_2, MD_capac_link_20_2, \
                 PM_capac_link_20_2, NT_capac_link_20_2, 0, \
                 0, 0, 0, 0)

link_21_1 = Link(12, 14, AM_capac_link_21_1, MD_capac_link_21_1, \
                 PM_capac_link_21_1, NT_capac_link_21_1, 0, \
                 0, 0, 0, 0)

link_21_2 = Link(14, 12, AM_capac_link_21_2, MD_capac_link_21_2, \
                 PM_capac_link_21_2, NT_capac_link_21_2, 0, \
                 0, 0, 0, 0)

link_22_1 = Link(10, 12, AM_capac_link_22_1, MD_capac_link_22_1, \
                 PM_capac_link_22_1, NT_capac_link_22_1, 0, \
                 0, 0, 0, 0)

link_22_2 = Link(12, 10, AM_capac_link_22_2, MD_capac_link_22_2, \
                 PM_capac_link_22_2, NT_capac_link_22_2, 0, \
                 0, 0, 0, 0)

zdump([link_1_1, link_1_2, link_2_1, link_2_2, link_3_1, link_3_2, \
	link_4_1, link_4_2, link_5_1, link_5_2, link_6_1, link_6_2, \
	link_7_1, link_7_2, link_8_1, link_8_2, link_9_1, link_9_2, \
	link_10_1, link_10_2, link_11_1, link_11_2, link_12_1, link_12_2, \
	link_13_1, link_13_2, link_14_1, link_14_2, link_15_1, link_15_2, \
	link_16_1, link_16_2, link_17_1, link_17_2, link_18_1, link_18_2, \
	link_19_1, link_19_2, link_20_1, link_20_2, link_21_1, link_21_2, \
	link_22_1, link_22_2], './temp_files/links_with_capac.pkz')
