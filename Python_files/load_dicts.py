from util import zload

tmc_list_link_1, tmc_list_link_2, tmc_list_link_3, tmc_list_link_4, tmc_list_link_5, \
	tmc_list_link_6, tmc_list_link_7, tmc_list_link_8, tmc_list_link_9, tmc_list_link_10, \
	tmc_list_link_11, tmc_list_link_12 = zload('../temp_files/tmc_list_links.pkz')

tmc_capac_dict_AM, tmc_capac_dict_MD, tmc_capac_dict_PM, \
    tmc_capac_dict_NT, tmc_length_dict = zload('../temp_files/link_dicts.pkz')

tmc_ref_speed_dict = zload('../temp_files/tmc_ref_speed_dict.pkz')
