from util import zload

tmc_list_link_1, tmc_list_link_2, tmc_list_link_3, tmc_list_link_4, tmc_list_link_5, \
    tmc_list_link_6, tmc_list_link_7, tmc_list_link_8, tmc_list_link_9, tmc_list_link_10, \
    tmc_list_link_11, tmc_list_link_12 = zload('../temp_files/tmc_list_links.pkz')

tmc_capac_dict_AM, tmc_capac_dict_MD, tmc_capac_dict_PM, \
    tmc_capac_dict_NT, tmc_length_dict = zload('../temp_files/link_dicts.pkz')

tmc_ref_speed_dict = zload('../temp_files/tmc_ref_speed_dict.pkz')

##### for extended sup-map
tmc_list_ext_link_dict = zload('../temp_files/tmc_list_ext_links_dict.pkz')

tmc_ref_speed_dict_ext = zload('../temp_files/tmc_ref_speed_dict_ext.pkz')

tmc_capac_dict_AM_ext, tmc_capac_dict_MD_ext, tmc_capac_dict_PM_ext, \
    tmc_capac_dict_NT_ext, tmc_length_dict_ext = zload('../temp_files/link_dicts_ext.pkz')

##### for journal sup-map
tmc_list_journal_link_dict = zload('../temp_files/tmc_list_journal_links_dict.pkz')

tmc_ref_speed_dict_journal = zload('../temp_files/tmc_ref_speed_dict_journal.pkz')

tmc_capac_dict_AM_journal, tmc_capac_dict_MD_journal, tmc_capac_dict_PM_journal, \
    tmc_capac_dict_NT_journal, tmc_length_dict_journal = zload('../temp_files/link_dicts_journal.pkz')
