#!/usr/bin/env python
""" A library of utility functions
"""
from __future__ import absolute_import, division

__author__ = "Jing Zhang"
__email__ = "jingzbu@gmail.com"
__status__ = "Development"


from util import *
from util_ano_detec import *
from load_dicts import *

import pylab
from pylab import *
import json


def detec_stati(N, n):
    """
    N: number of states in the original chain
    n: num of samples per window
    """
    
    traffic_data_with_anomaly = zload('../temp_files/traffic_data_with_anomaly_actual.pkz')
    traffic_data_ref = zload('../temp_files/traffic_data_ref_actual.pkz')

    tmc = '129+04292'
    month = 7
    day_list = [2, 3, 5, 9, 10, 11, 12, 16, 17, 18]  # July 4 is a holiday; we do not include Fridays

    traffic_data_ref_list = []
    for hour in range(24):
        for minute in range(60):
            for day in day_list:
                key = str(tmc) + '_' + str(month) + '_' + str(day) + '_' + str(hour) + '_' + str(minute)
                traffic_data_ref_list.append(traffic_data_ref[key])

    inf = min(traffic_data_ref_list)
    sup = max(traffic_data_ref_list)

    traffic_data_ref_list_quantized = [quantize(s, N, inf, sup) for s in traffic_data_ref_list]

    mapping_dict = {}

    for i in range(N):
        for j in range(N):
            mapping_dict[(i, j)] = i * N + j

    traffic_data_ref_list_quantized_trans = [mapping_dict[(traffic_data_ref_list_quantized[i], \
                                                           traffic_data_ref_list_quantized[i+1])] \
                                             for i in range(len(traffic_data_ref_list_quantized)-1)]

    day = 19

    traffic_data_with_anomaly_list = []
    for hour in range(24):
        for minute in range(60):
            key = str(tmc) + '_' + str(month) + '_' + str(day) + '_' + str(hour) + '_' + str(minute)
            traffic_data_with_anomaly_list.append(traffic_data_with_anomaly[key])

    traffic_data_with_anomaly_list_quantized = [quantize(s, N, inf, sup) for s in traffic_data_with_anomaly_list]

    traffic_data_with_anomaly_list_quantized_trans = \
    [mapping_dict[(traffic_data_with_anomaly_list_quantized[i], \
                   traffic_data_with_anomaly_list_quantized[i+1])] \
     for i in range(len(traffic_data_with_anomaly_list_quantized)-1)]

    mu_1 = mu_est(traffic_data_ref_list_quantized_trans, N)  # normal PL

    mu_1 = mu_adjust(mu_1)  # normal PL
    mu_01, mu1, mu_11, P1, G_11, H_11, U_11 = ChainGen_(mu_1)

    zdump([mu1, mu_11, P1, G_11, H_11, U_11], '../temp_files/Traffic_ano_detec_PLs_(%s_%s)_actual.pkz'%(N,n))

    num_test_sample = 24 * 60 - n
    beta = 0.001

    eta_wc = {}
    eta_Sanov = {}

    # Get thresholds for Hoeffding's test corresponding to sample length n    
    key = str(n) + '_' + str(beta)
    G_list = [G_11]
    H_list = [H_11]
    U_list = [U_11]
    eta_1 = HoeffdingRuleMarkovRobust_(beta, G_list, H_list, U_list, n)
    eta_2 = - log(beta) / n
    eta_wc[key] = eta_1
    eta_Sanov[key] = eta_2
    zdump([eta_wc, eta_Sanov], '../temp_files/traffic_ano_detec_threshold_(%s_%s)_actual.pkz'%(N,n))

    time_range = range(num_test_sample)

    eta_wc_list = []
    eta_Sanov_list = []
    for idx in time_range:
        eta_wc_list.append(np.array(eta_wc[key]).tolist())
        eta_Sanov_list.append(np.array(eta_Sanov[key]).tolist())

    test_sample = []

    for idx in range(num_test_sample):
        test_sample.append(traffic_data_with_anomaly_list_quantized_trans[idx : (idx+n)])

    KL = []
    key = str(n) + '_' + str(beta)
    for idx in range(num_test_sample):
        KL.append(KL_est(test_sample[idx], mu_11))

    zdump(KL, '../temp_files/traffic_ano_detec_KL_(%s_%s)_actual.pkz'%(N,n))

    # Output the time instances reporting an anomaly  
    alarm_instance_WC_list = []
    for idx in range(num_test_sample):
	if KL[idx] > eta_wc_list[idx]:
	    # print('(WC-stationary) The earliest time instance detecting the anomaly is: %s' %(idx + n))
	    # break
	    alarm_instance_WC_list.append(idx + n)

    alarm_instance_Sanov_list = []
    for idx in range(num_test_sample):
	if KL[idx] > eta_Sanov_list[idx]:
	    # print('(Sanov-stationary) The earliest time instance detecting the anomaly is: %s' %(idx + n))
	    # break
	    alarm_instance_Sanov_list.append(idx + n)

    alarm_instance_dict = {}
    alarm_instance_dict['WC'] = alarm_instance_WC_list
    alarm_instance_dict['Sanov'] = alarm_instance_Sanov_list
    with open('../temp_files/alarm_instance_dict_stationary_(%s_%s).json'%(N,n), 'w') as json_file:
	json.dump(alarm_instance_dict, json_file)

    plot_points(time_range, KL, eta_wc_list)
    plt.ylabel('divergence')
    plt.xlabel('time (min)')
    pylab.ylim(-0.01, max(KL)+0.1)
    pylab.xlim(0, 24 * 60)
    plt.savefig('../temp_files/detec_results_(%s_%s)_WC_actual.eps'%(N,n))
    # plt.show()

    plot_points(time_range, KL, eta_Sanov_list)
    plt.ylabel('divergence')
    plt.xlabel('time (min)')
    pylab.ylim(-0.01, max(KL)+0.1)
    pylab.xlim(0, 24 * 60)
    plt.savefig('../temp_files/detec_results_(%s_%s)_Sanov_actual.eps'%(N,n))
    # plt.show()
