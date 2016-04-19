from load_dicts import *
from util import *


tmc_set_link_1_1 = [i for i in tmc_list_ext_link_dict['1'] if ('P' in i or '+' in i)]
tmc_set_link_1_2 = [i for i in tmc_list_ext_link_dict['1'] if ('N' in i or '-' in i)]
AM_capac_link_1_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_1])
AM_capac_link_1_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_2])
MD_capac_link_1_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_1])
MD_capac_link_1_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_2])
PM_capac_link_1_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_1])
PM_capac_link_1_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_2])
NT_capac_link_1_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_1])
NT_capac_link_1_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_1_2])

tmc_set_link_2_1 = [i for i in tmc_list_ext_link_dict['2'] if ('P' in i or '+' in i)]
tmc_set_link_2_2 = [i for i in tmc_list_ext_link_dict['2'] if ('N' in i or '-' in i)]
AM_capac_link_2_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_1])
AM_capac_link_2_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_2])
MD_capac_link_2_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_1])
MD_capac_link_2_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_2])
PM_capac_link_2_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_1])
PM_capac_link_2_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_2])
NT_capac_link_2_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_1])
NT_capac_link_2_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_2_2])

tmc_set_link_3_1 = [i for i in tmc_list_ext_link_dict['3'] if ('P' in i or '+' in i)]
tmc_set_link_3_2 = [i for i in tmc_list_ext_link_dict['3'] if ('N' in i or '-' in i)]
AM_capac_link_3_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_1])
AM_capac_link_3_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_2])
MD_capac_link_3_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_1])
MD_capac_link_3_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_2])
PM_capac_link_3_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_1])
PM_capac_link_3_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_2])
NT_capac_link_3_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_1])
NT_capac_link_3_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_3_2])

tmc_set_link_4_1 = [i for i in tmc_list_ext_link_dict['4'] if ('P' in i or '+' in i)]
tmc_set_link_4_2 = [i for i in tmc_list_ext_link_dict['4'] if ('N' in i or '-' in i)]
AM_capac_link_4_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_1])
AM_capac_link_4_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_2])
MD_capac_link_4_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_1])
MD_capac_link_4_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_2])
PM_capac_link_4_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_1])
PM_capac_link_4_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_2])
NT_capac_link_4_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_1])
NT_capac_link_4_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_4_2])

tmc_set_link_5_1 = [i for i in tmc_list_ext_link_dict['5'] if ('P' in i or '+' in i)]
tmc_set_link_5_2 = [i for i in tmc_list_ext_link_dict['5'] if ('N' in i or '-' in i)]
AM_capac_link_5_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_1])
AM_capac_link_5_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_2])
MD_capac_link_5_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_1])
MD_capac_link_5_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_2])
PM_capac_link_5_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_1])
PM_capac_link_5_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_2])
NT_capac_link_5_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_1])
NT_capac_link_5_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_5_2])

tmc_set_link_6_1 = [i for i in tmc_list_ext_link_dict['6'] if ('P' in i or '+' in i)]
tmc_set_link_6_2 = [i for i in tmc_list_ext_link_dict['6'] if ('N' in i or '-' in i)]
AM_capac_link_6_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_1])
AM_capac_link_6_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_2])
MD_capac_link_6_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_1])
MD_capac_link_6_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_2])
PM_capac_link_6_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_1])
PM_capac_link_6_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_2])
NT_capac_link_6_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_1])
NT_capac_link_6_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_6_2])

tmc_set_link_7_1 = [i for i in tmc_list_ext_link_dict['7'] if ('P' in i or '+' in i)]
tmc_set_link_7_2 = [i for i in tmc_list_ext_link_dict['7'] if ('N' in i or '-' in i)]
AM_capac_link_7_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_1])
AM_capac_link_7_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_2])
MD_capac_link_7_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_1])
MD_capac_link_7_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_2])
PM_capac_link_7_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_1])
PM_capac_link_7_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_2])
NT_capac_link_7_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_1])
NT_capac_link_7_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_7_2])

tmc_set_link_8_1 = [i for i in tmc_list_ext_link_dict['8'] if ('P' in i or '+' in i)]
tmc_set_link_8_2 = [i for i in tmc_list_ext_link_dict['8'] if ('N' in i or '-' in i)]
AM_capac_link_8_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_1])
AM_capac_link_8_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_2])
MD_capac_link_8_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_1])
MD_capac_link_8_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_2])
PM_capac_link_8_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_1])
PM_capac_link_8_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_2])
NT_capac_link_8_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_1])
NT_capac_link_8_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_8_2])

tmc_set_link_9_1 = [i for i in tmc_list_ext_link_dict['9'] if ('P' in i or '+' in i)]
tmc_set_link_9_2 = [i for i in tmc_list_ext_link_dict['9'] if ('N' in i or '-' in i)]
AM_capac_link_9_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_1])
AM_capac_link_9_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_2])
MD_capac_link_9_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_1])
MD_capac_link_9_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_2])
PM_capac_link_9_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_1])
PM_capac_link_9_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_2])
NT_capac_link_9_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_1])
NT_capac_link_9_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_9_2])

tmc_set_link_10_1 = [i for i in tmc_list_ext_link_dict['10'] if ('P' in i or '+' in i)]
tmc_set_link_10_2 = [i for i in tmc_list_ext_link_dict['10'] if ('N' in i or '-' in i)]
AM_capac_link_10_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_1])
AM_capac_link_10_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_2])
MD_capac_link_10_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_1])
MD_capac_link_10_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_2])
PM_capac_link_10_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_1])
PM_capac_link_10_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_2])
NT_capac_link_10_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_1])
NT_capac_link_10_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_10_2])

tmc_set_link_11_1 = [i for i in tmc_list_ext_link_dict['11'] if ('P' in i or '+' in i)]
tmc_set_link_11_2 = [i for i in tmc_list_ext_link_dict['11'] if ('N' in i or '-' in i)]
AM_capac_link_11_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_1])
AM_capac_link_11_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_2])
MD_capac_link_11_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_1])
MD_capac_link_11_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_2])
PM_capac_link_11_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_1])
PM_capac_link_11_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_2])
NT_capac_link_11_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_1])
NT_capac_link_11_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_11_2])

tmc_set_link_12_1 = [i for i in tmc_list_ext_link_dict['12'] if ('P' in i or '+' in i)]
tmc_set_link_12_2 = [i for i in tmc_list_ext_link_dict['12'] if ('N' in i or '-' in i)]
AM_capac_link_12_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_1])
AM_capac_link_12_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_2])
MD_capac_link_12_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_1])
MD_capac_link_12_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_2])
PM_capac_link_12_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_1])
PM_capac_link_12_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_2])
NT_capac_link_12_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_1])
NT_capac_link_12_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_12_2])

tmc_set_link_13_1 = [i for i in tmc_list_ext_link_dict['13'] if ('P' in i or '+' in i)]
tmc_set_link_13_2 = [i for i in tmc_list_ext_link_dict['13'] if ('N' in i or '-' in i)]
AM_capac_link_13_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_1])
AM_capac_link_13_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_2])
MD_capac_link_13_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_1])
MD_capac_link_13_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_2])
PM_capac_link_13_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_1])
PM_capac_link_13_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_2])
NT_capac_link_13_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_1])
NT_capac_link_13_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_13_2])

tmc_set_link_14_1 = [i for i in tmc_list_ext_link_dict['14'] if ('P' in i or '+' in i)]
tmc_set_link_14_2 = [i for i in tmc_list_ext_link_dict['14'] if ('N' in i or '-' in i)]
AM_capac_link_14_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_1])
AM_capac_link_14_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_2])
MD_capac_link_14_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_1])
MD_capac_link_14_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_2])
PM_capac_link_14_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_1])
PM_capac_link_14_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_2])
NT_capac_link_14_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_1])
NT_capac_link_14_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_14_2])

tmc_set_link_15_1 = [i for i in tmc_list_ext_link_dict['15'] if ('P' in i or '+' in i)]
tmc_set_link_15_2 = [i for i in tmc_list_ext_link_dict['15'] if ('N' in i or '-' in i)]
AM_capac_link_15_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_1])
AM_capac_link_15_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_2])
MD_capac_link_15_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_1])
MD_capac_link_15_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_2])
PM_capac_link_15_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_1])
PM_capac_link_15_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_2])
NT_capac_link_15_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_1])
NT_capac_link_15_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_15_2])

tmc_set_link_16_1 = [i for i in tmc_list_ext_link_dict['16'] if ('P' in i or '+' in i)]
tmc_set_link_16_2 = [i for i in tmc_list_ext_link_dict['16'] if ('N' in i or '-' in i)]
AM_capac_link_16_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_1])
AM_capac_link_16_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_2])
MD_capac_link_16_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_1])
MD_capac_link_16_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_2])
PM_capac_link_16_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_1])
PM_capac_link_16_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_2])
NT_capac_link_16_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_1])
NT_capac_link_16_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_16_2])

tmc_set_link_17_1 = [i for i in tmc_list_ext_link_dict['17'] if ('P' in i or '+' in i)]
tmc_set_link_17_2 = [i for i in tmc_list_ext_link_dict['17'] if ('N' in i or '-' in i)]
AM_capac_link_17_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_1])
AM_capac_link_17_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_2])
MD_capac_link_17_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_1])
MD_capac_link_17_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_2])
PM_capac_link_17_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_1])
PM_capac_link_17_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_2])
NT_capac_link_17_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_1])
NT_capac_link_17_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_17_2])

tmc_set_link_18_1 = [i for i in tmc_list_ext_link_dict['18'] if ('P' in i or '+' in i)]
tmc_set_link_18_2 = [i for i in tmc_list_ext_link_dict['18'] if ('N' in i or '-' in i)]
AM_capac_link_18_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_1])
AM_capac_link_18_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_2])
MD_capac_link_18_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_1])
MD_capac_link_18_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_2])
PM_capac_link_18_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_1])
PM_capac_link_18_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_2])
NT_capac_link_18_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_1])
NT_capac_link_18_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_18_2])

tmc_set_link_19_1 = [i for i in tmc_list_ext_link_dict['19'] if ('P' in i or '+' in i)]
tmc_set_link_19_2 = [i for i in tmc_list_ext_link_dict['19'] if ('N' in i or '-' in i)]
AM_capac_link_19_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_1])
AM_capac_link_19_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_2])
MD_capac_link_19_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_1])
MD_capac_link_19_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_2])
PM_capac_link_19_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_1])
PM_capac_link_19_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_2])
NT_capac_link_19_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_1])
NT_capac_link_19_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_19_2])

tmc_set_link_20_1 = [i for i in tmc_list_ext_link_dict['20'] if ('P' in i or '+' in i)]
tmc_set_link_20_2 = [i for i in tmc_list_ext_link_dict['20'] if ('N' in i or '-' in i)]
AM_capac_link_20_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_1])
AM_capac_link_20_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_2])
MD_capac_link_20_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_1])
MD_capac_link_20_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_2])
PM_capac_link_20_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_1])
PM_capac_link_20_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_2])
NT_capac_link_20_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_1])
NT_capac_link_20_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_20_2])

tmc_set_link_21_1 = [i for i in tmc_list_ext_link_dict['21'] if ('P' in i or '+' in i)]
tmc_set_link_21_2 = [i for i in tmc_list_ext_link_dict['21'] if ('N' in i or '-' in i)]
AM_capac_link_21_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_1])
AM_capac_link_21_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_2])
MD_capac_link_21_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_1])
MD_capac_link_21_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_2])
PM_capac_link_21_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_1])
PM_capac_link_21_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_2])
NT_capac_link_21_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_1])
NT_capac_link_21_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_21_2])

tmc_set_link_22_1 = [i for i in tmc_list_ext_link_dict['22'] if ('P' in i or '+' in i)]
tmc_set_link_22_2 = [i for i in tmc_list_ext_link_dict['22'] if ('N' in i or '-' in i)]
AM_capac_link_22_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_1])
AM_capac_link_22_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_2])
MD_capac_link_22_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_1])
MD_capac_link_22_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_2])
PM_capac_link_22_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_1])
PM_capac_link_22_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_2])
NT_capac_link_22_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_1])
NT_capac_link_22_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_22_2])

tmc_set_link_23_1 = [i for i in tmc_list_ext_link_dict['23'] if ('P' in i or '+' in i)]
tmc_set_link_23_2 = [i for i in tmc_list_ext_link_dict['23'] if ('N' in i or '-' in i)]
AM_capac_link_23_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_1])
AM_capac_link_23_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_2])
MD_capac_link_23_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_1])
MD_capac_link_23_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_2])
PM_capac_link_23_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_1])
PM_capac_link_23_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_2])
NT_capac_link_23_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_1])
NT_capac_link_23_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_23_2])

tmc_set_link_24_1 = [i for i in tmc_list_ext_link_dict['24'] if ('P' in i or '+' in i)]
tmc_set_link_24_2 = [i for i in tmc_list_ext_link_dict['24'] if ('N' in i or '-' in i)]
AM_capac_link_24_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_1])
AM_capac_link_24_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_2])
MD_capac_link_24_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_1])
MD_capac_link_24_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_2])
PM_capac_link_24_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_1])
PM_capac_link_24_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_2])
NT_capac_link_24_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_1])
NT_capac_link_24_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_24_2])

tmc_set_link_25_1 = [i for i in tmc_list_ext_link_dict['25'] if ('P' in i or '+' in i)]
tmc_set_link_25_2 = [i for i in tmc_list_ext_link_dict['25'] if ('N' in i or '-' in i)]
AM_capac_link_25_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_1])
AM_capac_link_25_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_2])
MD_capac_link_25_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_1])
MD_capac_link_25_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_2])
PM_capac_link_25_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_1])
PM_capac_link_25_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_2])
NT_capac_link_25_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_1])
NT_capac_link_25_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_25_2])

tmc_set_link_26_1 = [i for i in tmc_list_ext_link_dict['26'] if ('P' in i or '+' in i)]
tmc_set_link_26_2 = [i for i in tmc_list_ext_link_dict['26'] if ('N' in i or '-' in i)]
AM_capac_link_26_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_1])
AM_capac_link_26_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_2])
MD_capac_link_26_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_1])
MD_capac_link_26_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_2])
PM_capac_link_26_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_1])
PM_capac_link_26_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_2])
NT_capac_link_26_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_1])
NT_capac_link_26_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_26_2])

tmc_set_link_27_1 = [i for i in tmc_list_ext_link_dict['27'] if ('P' in i or '+' in i)]
tmc_set_link_27_2 = [i for i in tmc_list_ext_link_dict['27'] if ('N' in i or '-' in i)]
AM_capac_link_27_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_1])
AM_capac_link_27_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_2])
MD_capac_link_27_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_1])
MD_capac_link_27_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_2])
PM_capac_link_27_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_1])
PM_capac_link_27_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_2])
NT_capac_link_27_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_1])
NT_capac_link_27_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_27_2])

tmc_set_link_28_1 = [i for i in tmc_list_ext_link_dict['28'] if ('P' in i or '+' in i)]
tmc_set_link_28_2 = [i for i in tmc_list_ext_link_dict['28'] if ('N' in i or '-' in i)]
AM_capac_link_28_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_1])
AM_capac_link_28_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_2])
MD_capac_link_28_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_1])
MD_capac_link_28_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_2])
PM_capac_link_28_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_1])
PM_capac_link_28_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_2])
NT_capac_link_28_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_1])
NT_capac_link_28_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_28_2])

tmc_set_link_29_1 = [i for i in tmc_list_ext_link_dict['29'] if ('P' in i or '+' in i)]
tmc_set_link_29_2 = [i for i in tmc_list_ext_link_dict['29'] if ('N' in i or '-' in i)]
AM_capac_link_29_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_1])
AM_capac_link_29_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_2])
MD_capac_link_29_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_1])
MD_capac_link_29_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_2])
PM_capac_link_29_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_1])
PM_capac_link_29_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_2])
NT_capac_link_29_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_1])
NT_capac_link_29_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_29_2])

tmc_set_link_30_1 = [i for i in tmc_list_ext_link_dict['30'] if ('P' in i or '+' in i)]
tmc_set_link_30_2 = [i for i in tmc_list_ext_link_dict['30'] if ('N' in i or '-' in i)]
AM_capac_link_30_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_1])
AM_capac_link_30_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_2])
MD_capac_link_30_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_1])
MD_capac_link_30_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_2])
PM_capac_link_30_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_1])
PM_capac_link_30_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_2])
NT_capac_link_30_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_1])
NT_capac_link_30_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_30_2])

tmc_set_link_31_1 = [i for i in tmc_list_ext_link_dict['31'] if ('P' in i or '+' in i)]
tmc_set_link_31_2 = [i for i in tmc_list_ext_link_dict['31'] if ('N' in i or '-' in i)]
AM_capac_link_31_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_1])
AM_capac_link_31_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_2])
MD_capac_link_31_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_1])
MD_capac_link_31_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_2])
PM_capac_link_31_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_1])
PM_capac_link_31_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_2])
NT_capac_link_31_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_1])
NT_capac_link_31_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_31_2])

tmc_set_link_32_1 = [i for i in tmc_list_ext_link_dict['32'] if ('P' in i or '+' in i)]
tmc_set_link_32_2 = [i for i in tmc_list_ext_link_dict['32'] if ('N' in i or '-' in i)]
AM_capac_link_32_1 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_1])
AM_capac_link_32_2 = sum([tmc_capac_dict_AM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_2])
MD_capac_link_32_1 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_1])
MD_capac_link_32_2 = sum([tmc_capac_dict_MD_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_2])
PM_capac_link_32_1 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_1])
PM_capac_link_32_2 = sum([tmc_capac_dict_PM_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_2])
NT_capac_link_32_1 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_1]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_1])
NT_capac_link_32_2 = sum([tmc_capac_dict_NT_ext[i] * tmc_length_dict_ext[i] / \
			 (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_2]) / \
		    sum([tmc_length_dict_ext[i] / (tmc_ref_speed_dict_ext[i]) for i in tmc_set_link_32_2])


# instantiation of Link class
link_1_1 = Link_with_Free_Flow_Time_Ext(1, 2, tmc_set_link_1_1, AM_capac_link_1_1, MD_capac_link_1_1, \
		 PM_capac_link_1_1, NT_capac_link_1_1, 0, \
		 0, 0, 0, 0, 0)

link_1_2 = Link_with_Free_Flow_Time_Ext(2, 1, tmc_set_link_1_2, AM_capac_link_1_2, MD_capac_link_1_2, \
                 PM_capac_link_1_2, NT_capac_link_1_2, 0, \
		 0, 0, 0, 0, 0)

link_2_1 = Link_with_Free_Flow_Time_Ext(1, 3, tmc_set_link_2_1, AM_capac_link_2_1, MD_capac_link_2_1, \
                 PM_capac_link_2_1, NT_capac_link_2_1, 0, \
                 0, 0, 0, 0, 0)

link_2_2 = Link_with_Free_Flow_Time_Ext(3, 1, tmc_set_link_2_2, AM_capac_link_2_2, MD_capac_link_2_2, \
                 PM_capac_link_2_2, NT_capac_link_2_2, 0, \
                 0, 0, 0, 0, 0)

link_3_1 = Link_with_Free_Flow_Time_Ext(2, 3, tmc_set_link_3_1, AM_capac_link_3_1, MD_capac_link_3_1, \
                 PM_capac_link_3_1, NT_capac_link_3_1, 0, \
                 0, 0, 0, 0, 0)

link_3_2 = Link_with_Free_Flow_Time_Ext(3, 2, tmc_set_link_3_2, AM_capac_link_3_2, MD_capac_link_3_2, \
                 PM_capac_link_3_2, NT_capac_link_3_2, 0, \
                 0, 0, 0, 0, 0)

link_4_1 = Link_with_Free_Flow_Time_Ext(2, 4, tmc_set_link_4_1, AM_capac_link_4_1, MD_capac_link_4_1, \
                 PM_capac_link_4_1, NT_capac_link_4_1, 0, \
                 0, 0, 0, 0, 0)

link_4_2 = Link_with_Free_Flow_Time_Ext(4, 2, tmc_set_link_4_2, AM_capac_link_4_2, MD_capac_link_4_2, \
                 PM_capac_link_4_2, NT_capac_link_4_2, 0, \
                 0, 0, 0, 0, 0)

link_5_1 = Link_with_Free_Flow_Time_Ext(3, 6, tmc_set_link_5_1, AM_capac_link_5_1, MD_capac_link_5_1, \
                 PM_capac_link_5_1, NT_capac_link_5_1, 0, \
                 0, 0, 0, 0, 0)

link_5_2 = Link_with_Free_Flow_Time_Ext(6, 3, tmc_set_link_5_2, AM_capac_link_5_2, MD_capac_link_5_2, \
                 PM_capac_link_5_2, NT_capac_link_5_2, 0, \
                 0, 0, 0, 0, 0)

link_6_1 = Link_with_Free_Flow_Time_Ext(4, 6, tmc_set_link_6_1, AM_capac_link_6_1, MD_capac_link_6_1, \
                 PM_capac_link_6_1, NT_capac_link_6_1, 0, \
                 0, 0, 0, 0, 0)

link_6_2 = Link_with_Free_Flow_Time_Ext(6, 4, tmc_set_link_6_2, AM_capac_link_6_2, MD_capac_link_6_2, \
                 PM_capac_link_6_2, NT_capac_link_6_2, 0, \
                 0, 0, 0, 0, 0)

link_7_1 = Link_with_Free_Flow_Time_Ext(4, 7, tmc_set_link_7_1, AM_capac_link_7_1, MD_capac_link_7_1, \
                 PM_capac_link_7_1, NT_capac_link_7_1, 0, \
                 0, 0, 0, 0, 0)

link_7_2 = Link_with_Free_Flow_Time_Ext(7, 4, tmc_set_link_7_2, AM_capac_link_7_2, MD_capac_link_7_2, \
                 PM_capac_link_7_2, NT_capac_link_7_2, 0, \
                 0, 0, 0, 0, 0)

link_8_1 = Link_with_Free_Flow_Time_Ext(4, 7, tmc_set_link_8_1, AM_capac_link_8_1, MD_capac_link_8_1, \
                 PM_capac_link_8_1, NT_capac_link_8_1, 0, \
                 0, 0, 0, 0, 0)

link_8_2 = Link_with_Free_Flow_Time_Ext(7, 4, tmc_set_link_8_2, AM_capac_link_8_2, MD_capac_link_8_2, \
                 PM_capac_link_8_2, NT_capac_link_8_2, 0, \
                 0, 0, 0, 0, 0)

link_9_1 = Link_with_Free_Flow_Time_Ext(4, 5, tmc_set_link_9_1, AM_capac_link_9_1, MD_capac_link_9_1, \
                 PM_capac_link_9_1, NT_capac_link_9_1, 0, \
                 0, 0, 0, 0, 0)

link_9_2 = Link_with_Free_Flow_Time_Ext(5, 4, tmc_set_link_9_2, AM_capac_link_9_2, MD_capac_link_9_2, \
                 PM_capac_link_9_2, NT_capac_link_9_2, 0, \
                 0, 0, 0, 0, 0)

link_10_1 = Link_with_Free_Flow_Time_Ext(6, 7, tmc_set_link_10_1, AM_capac_link_10_1, MD_capac_link_10_1, \
                 PM_capac_link_10_1, NT_capac_link_10_1, 0, \
                 0, 0, 0, 0, 0)

link_10_2 = Link_with_Free_Flow_Time_Ext(7, 6, tmc_set_link_10_2, AM_capac_link_10_2, MD_capac_link_10_2, \
                 PM_capac_link_10_2, NT_capac_link_10_2, 0, \
                 0, 0, 0, 0, 0)

link_11_1 = Link_with_Free_Flow_Time_Ext(5, 8, tmc_set_link_11_1, AM_capac_link_11_1, MD_capac_link_11_1, \
                 PM_capac_link_11_1, NT_capac_link_11_1, 0, \
                 0, 0, 0, 0, 0)

link_11_2 = Link_with_Free_Flow_Time_Ext(8, 5, tmc_set_link_11_2, AM_capac_link_11_2, MD_capac_link_11_2, \
                 PM_capac_link_11_2, NT_capac_link_11_2, 0, \
                 0, 0, 0, 0, 0)

link_12_1 = Link_with_Free_Flow_Time_Ext(5, 9, tmc_set_link_12_1, AM_capac_link_12_1, MD_capac_link_12_1, \
                 PM_capac_link_12_1, NT_capac_link_12_1, 0, \
                 0, 0, 0, 0, 0)

link_12_2 = Link_with_Free_Flow_Time_Ext(9, 5, tmc_set_link_12_2, AM_capac_link_12_2, MD_capac_link_12_2, \
                 PM_capac_link_12_2, NT_capac_link_12_2, 0, \
                 0, 0, 0, 0, 0)

link_13_1 = Link_with_Free_Flow_Time_Ext(7, 9, tmc_set_link_13_1, AM_capac_link_13_1, MD_capac_link_13_1, \
		 PM_capac_link_13_1, NT_capac_link_13_1, 0, \
		 0, 0, 0, 0, 0)

link_13_2 = Link_with_Free_Flow_Time_Ext(9, 7, tmc_set_link_13_2, AM_capac_link_13_2, MD_capac_link_13_2, \
                 PM_capac_link_13_2, NT_capac_link_13_2, 0, \
		 0, 0, 0, 0, 0)

link_14_1 = Link_with_Free_Flow_Time_Ext(7, 11, tmc_set_link_14_1, AM_capac_link_14_1, MD_capac_link_14_1, \
                 PM_capac_link_14_1, NT_capac_link_14_1, 0, \
                 0, 0, 0, 0, 0)

link_14_2 = Link_with_Free_Flow_Time_Ext(11, 7, tmc_set_link_14_2, AM_capac_link_14_2, MD_capac_link_14_2, \
                 PM_capac_link_14_2, NT_capac_link_14_2, 0, \
                 0, 0, 0, 0, 0)

link_15_1 = Link_with_Free_Flow_Time_Ext(9, 10, tmc_set_link_15_1, AM_capac_link_15_1, MD_capac_link_15_1, \
                 PM_capac_link_15_1, NT_capac_link_15_1, 0, \
                 0, 0, 0, 0, 0)

link_15_2 = Link_with_Free_Flow_Time_Ext(10, 9, tmc_set_link_15_2, AM_capac_link_15_2, MD_capac_link_15_2, \
                 PM_capac_link_15_2, NT_capac_link_15_2, 0, \
                 0, 0, 0, 0, 0)

link_16_1 = Link_with_Free_Flow_Time_Ext(8, 10, tmc_set_link_16_1, AM_capac_link_16_1, MD_capac_link_16_1, \
                 PM_capac_link_16_1, NT_capac_link_16_1, 0, \
                 0, 0, 0, 0, 0)

link_16_2 = Link_with_Free_Flow_Time_Ext(10, 8, tmc_set_link_16_2, AM_capac_link_16_2, MD_capac_link_16_2, \
                 PM_capac_link_16_2, NT_capac_link_16_2, 0, \
                 0, 0, 0, 0, 0)

link_17_1 = Link_with_Free_Flow_Time_Ext(10, 11, tmc_set_link_17_1, AM_capac_link_17_1, MD_capac_link_17_1, \
                 PM_capac_link_17_1, NT_capac_link_17_1, 0, \
                 0, 0, 0, 0, 0)

link_17_2 = Link_with_Free_Flow_Time_Ext(11, 10, tmc_set_link_17_2, AM_capac_link_17_2, MD_capac_link_17_2, \
                 PM_capac_link_17_2, NT_capac_link_17_2, 0, \
                 0, 0, 0, 0, 0)

link_18_1 = Link_with_Free_Flow_Time_Ext(8, 12, tmc_set_link_18_1, AM_capac_link_18_1, MD_capac_link_18_1, \
                 PM_capac_link_18_1, NT_capac_link_18_1, 0, \
                 0, 0, 0, 0, 0)

link_18_2 = Link_with_Free_Flow_Time_Ext(12, 8, tmc_set_link_18_2, AM_capac_link_18_2, MD_capac_link_18_2, \
                 PM_capac_link_18_2, NT_capac_link_18_2, 0, \
                 0, 0, 0, 0, 0)

link_19_1 = Link_with_Free_Flow_Time_Ext(10, 13, tmc_set_link_19_1, AM_capac_link_19_1, MD_capac_link_19_1, \
                 PM_capac_link_19_1, NT_capac_link_19_1, 0, \
                 0, 0, 0, 0, 0)

link_19_2 = Link_with_Free_Flow_Time_Ext(13, 10, tmc_set_link_19_2, AM_capac_link_19_2, MD_capac_link_19_2, \
                 PM_capac_link_19_2, NT_capac_link_19_2, 0, \
                 0, 0, 0, 0, 0)

link_20_1 = Link_with_Free_Flow_Time_Ext(11, 14, tmc_set_link_20_1, AM_capac_link_20_1, MD_capac_link_20_1, \
                 PM_capac_link_20_1, NT_capac_link_20_1, 0, \
                 0, 0, 0, 0, 0)

link_20_2 = Link_with_Free_Flow_Time_Ext(14, 11, tmc_set_link_20_2, AM_capac_link_20_2, MD_capac_link_20_2, \
                 PM_capac_link_20_2, NT_capac_link_20_2, 0, \
                 0, 0, 0, 0, 0)

link_21_1 = Link_with_Free_Flow_Time_Ext(12, 13, tmc_set_link_21_1, AM_capac_link_21_1, MD_capac_link_21_1, \
                 PM_capac_link_21_1, NT_capac_link_21_1, 0, \
                 0, 0, 0, 0, 0)

link_21_2 = Link_with_Free_Flow_Time_Ext(13, 12, tmc_set_link_21_2, AM_capac_link_21_2, MD_capac_link_21_2, \
                 PM_capac_link_21_2, NT_capac_link_21_2, 0, \
                 0, 0, 0, 0, 0)

link_22_1 = Link_with_Free_Flow_Time_Ext(12, 13, tmc_set_link_10_1, AM_capac_link_10_1, MD_capac_link_10_1, \
                 PM_capac_link_10_1, NT_capac_link_10_1, 0, \
                 0, 0, 0, 0, 0)

link_22_2 = Link_with_Free_Flow_Time_Ext(13, 12, tmc_set_link_22_2, AM_capac_link_22_2, MD_capac_link_22_2, \
                 PM_capac_link_22_2, NT_capac_link_22_2, 0, \
                 0, 0, 0, 0, 0)

link_23_1 = Link_with_Free_Flow_Time_Ext(12, 13, tmc_set_link_23_1, AM_capac_link_23_1, MD_capac_link_23_1, \
                 PM_capac_link_23_1, NT_capac_link_23_1, 0, \
                 0, 0, 0, 0, 0)

link_23_2 = Link_with_Free_Flow_Time_Ext(13, 12, tmc_set_link_23_2, AM_capac_link_23_2, MD_capac_link_23_2, \
                 PM_capac_link_23_2, NT_capac_link_23_2, 0, \
                 0, 0, 0, 0, 0)

link_24_1 = Link_with_Free_Flow_Time_Ext(13, 14, tmc_set_link_24_1, AM_capac_link_24_1, MD_capac_link_24_1, \
                 PM_capac_link_24_1, NT_capac_link_24_1, 0, \
                 0, 0, 0, 0, 0)

link_24_2 = Link_with_Free_Flow_Time_Ext(14, 13, tmc_set_link_24_2, AM_capac_link_24_2, MD_capac_link_24_2, \
                 PM_capac_link_24_2, NT_capac_link_24_2, 0, \
                 0, 0, 0, 0, 0)

link_25_1 = Link_with_Free_Flow_Time_Ext(13, 14, tmc_set_link_25_1, AM_capac_link_25_1, MD_capac_link_25_1, \
		 PM_capac_link_25_1, NT_capac_link_25_1, 0, \
		 0, 0, 0, 0, 0)

link_25_2 = Link_with_Free_Flow_Time_Ext(14, 13, tmc_set_link_25_2, AM_capac_link_25_2, MD_capac_link_25_2, \
                 PM_capac_link_25_2, NT_capac_link_25_2, 0, \
		 0, 0, 0, 0, 0)

link_26_1 = Link_with_Free_Flow_Time_Ext(12, 15, tmc_set_link_26_1, AM_capac_link_26_1, MD_capac_link_26_1, \
                 PM_capac_link_26_1, NT_capac_link_26_1, 0, \
                 0, 0, 0, 0, 0)

link_26_2 = Link_with_Free_Flow_Time_Ext(15, 12, tmc_set_link_26_2, AM_capac_link_26_2, MD_capac_link_26_2, \
                 PM_capac_link_26_2, NT_capac_link_26_2, 0, \
                 0, 0, 0, 0, 0)

link_27_1 = Link_with_Free_Flow_Time_Ext(13, 15, tmc_set_link_27_1, AM_capac_link_27_1, MD_capac_link_27_1, \
                 PM_capac_link_27_1, NT_capac_link_27_1, 0, \
                 0, 0, 0, 0, 0)

link_27_2 = Link_with_Free_Flow_Time_Ext(15, 13, tmc_set_link_27_2, AM_capac_link_27_2, MD_capac_link_27_2, \
                 PM_capac_link_27_2, NT_capac_link_27_2, 0, \
                 0, 0, 0, 0, 0)

link_28_1 = Link_with_Free_Flow_Time_Ext(13, 16, tmc_set_link_28_1, AM_capac_link_28_1, MD_capac_link_28_1, \
                 PM_capac_link_28_1, NT_capac_link_28_1, 0, \
                 0, 0, 0, 0, 0)

link_28_2 = Link_with_Free_Flow_Time_Ext(16, 13, tmc_set_link_28_2, AM_capac_link_28_2, MD_capac_link_28_2, \
                 PM_capac_link_28_2, NT_capac_link_28_2, 0, \
                 0, 0, 0, 0, 0)

link_29_1 = Link_with_Free_Flow_Time_Ext(14, 16, tmc_set_link_29_1, AM_capac_link_29_1, MD_capac_link_29_1, \
                 PM_capac_link_29_1, NT_capac_link_29_1, 0, \
                 0, 0, 0, 0, 0)

link_29_2 = Link_with_Free_Flow_Time_Ext(16, 14, tmc_set_link_29_2, AM_capac_link_29_2, MD_capac_link_29_2, \
                 PM_capac_link_29_2, NT_capac_link_29_2, 0, \
                 0, 0, 0, 0, 0)

link_30_1 = Link_with_Free_Flow_Time_Ext(14, 16, tmc_set_link_30_1, AM_capac_link_30_1, MD_capac_link_30_1, \
                 PM_capac_link_30_1, NT_capac_link_30_1, 0, \
                 0, 0, 0, 0, 0)

link_30_2 = Link_with_Free_Flow_Time_Ext(16, 14, tmc_set_link_30_2, AM_capac_link_30_2, MD_capac_link_30_2, \
                 PM_capac_link_30_2, NT_capac_link_30_2, 0, \
                 0, 0, 0, 0, 0)

link_31_1 = Link_with_Free_Flow_Time_Ext(15, 17, tmc_set_link_31_1, AM_capac_link_31_1, MD_capac_link_31_1, \
                 PM_capac_link_31_1, NT_capac_link_31_1, 0, \
                 0, 0, 0, 0, 0)

link_31_2 = Link_with_Free_Flow_Time_Ext(17, 15, tmc_set_link_31_2, AM_capac_link_31_2, MD_capac_link_31_2, \
                 PM_capac_link_31_2, NT_capac_link_31_2, 0, \
                 0, 0, 0, 0, 0)

link_32_1 = Link_with_Free_Flow_Time_Ext(16, 17, tmc_set_link_32_1, AM_capac_link_32_1, MD_capac_link_32_1, \
                 PM_capac_link_32_1, NT_capac_link_32_1, 0, \
                 0, 0, 0, 0, 0)

link_32_2 = Link_with_Free_Flow_Time_Ext(17, 16, tmc_set_link_32_2, AM_capac_link_32_2, MD_capac_link_32_2, \
                 PM_capac_link_32_2, NT_capac_link_32_2, 0, \
                 0, 0, 0, 0, 0)


zdump([link_1_1, link_1_2, link_2_1, link_2_2, link_3_1, link_3_2, \
	link_4_1, link_4_2, link_5_1, link_5_2, link_6_1, link_6_2, \
	link_7_1, link_7_2, link_8_1, link_8_2, link_9_1, link_9_2, \
	link_10_1, link_10_2, link_11_1, link_11_2, link_12_1, link_12_2, \
	link_13_1, link_13_2, link_14_1, link_14_2, link_15_1, link_15_2, \
	link_16_1, link_16_2, link_17_1, link_17_2, link_18_1, link_18_2, \
	link_19_1, link_19_2, link_20_1, link_20_2, link_21_1, link_21_2, \
	link_22_1, link_22_2, link_23_1, link_23_2, link_24_1, link_24_2, \
	link_25_1, link_25_2, link_26_1, link_26_2, link_27_1, link_27_2, \
	link_28_1, link_28_2, link_29_1, link_29_2, link_30_1, link_30_2, \
	link_31_1, link_31_2, link_32_1, link_32_2], '../temp_files/links_with_capac_ext.pkz')
