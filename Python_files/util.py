from util_data_storage_and_load import *


try:
    from load_dicts import tmc_length_dict, tmc_ref_speed_dict
except ImportError:
    print "No dicts found; please check load_dicts..."

# define a function converting speed to flow, based on Greenshield's model
def speed_to_flow(capac, ref_speed, speed):
    # assume the free speed equals 1.5 * ref_speed
    free_speed = 1.5 * ref_speed
    if speed > free_speed:
	return 0
    return 4 * capac * speed / free_speed - 4 * capac * (speed ** 2) / (free_speed ** 2)

##### define classes

# define a road segment class corresponding to the original filtered shape file
# Inr indicates INRIX
class RoadSegInr(object):
    def __init__(self, tmc, road_num, shape_length):
        self.tmc = tmc
        self.road_num = road_num
        self.shape_length = shape_length

# define a road segment capacity class corresponding to the capacity file
class RoadSegCapac(object):
    def __init__(self, road_invent, length, route_num, AB_AM_capac, \
                 AB_MD_capac, AB_PM_capac, AB_NT_capac):
        self.road_invent = road_invent
        self.length = length
        self.route_num = route_num
        self.AB_AM_capac = AB_AM_capac
        self.AB_MD_capac = AB_MD_capac
        self.AB_PM_capac = AB_PM_capac
        self.AB_NT_capac = AB_NT_capac

# define a lookup class corresponding to the lookup table file
class LookUp(object):
    def __init__(self, road_inv_ID, tmc):
        self.road_inv_ID = road_inv_ID
        self.tmc = tmc

# define a derived road segment class containing the capacity info
class RoadSegInrCapac(RoadSegInr):
    def __init__(self, tmc, road_num, shape_length, AB_AM_capac, \
                 AB_MD_capac, AB_PM_capac, AB_NT_capac):
        RoadSegInr.__init__(self, tmc, road_num, shape_length)
        self.AB_AM_capac = AB_AM_capac
        self.AB_MD_capac = AB_MD_capac
        self.AB_PM_capac = AB_PM_capac
        self.AB_NT_capac = AB_NT_capac

# define a class containing tmc, day, and average speed
class TMC_Day_Speed(object):
    def __init__(self, tmc, day, speed, travel_time):
        self.tmc = tmc
        self.day = day
        self.speed = speed
        self.travel_time = travel_time
    def ave_speed(self):
        return sum([self.speed[i] * self.travel_time[i] for i in range(len(self.speed))]) / sum(self.travel_time)

# define a derived road segment class containing the flow info
class RoadSegInrCapacFlow(RoadSegInrCapac):
    def __init__(self, tmc, road_num, shape_length, day,
		 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac, \
		 AM_ave_speed, MD_ave_speed, PM_ave_speed, NT_ave_speed):
        RoadSegInrCapac.__init__(self, tmc, road_num, shape_length, \
				 AB_AM_capac, AB_MD_capac, AB_PM_capac, AB_NT_capac)
        self.day = day
        self.AM_ave_speed = AM_ave_speed
        self.MD_ave_speed = MD_ave_speed
        self.PM_ave_speed = PM_ave_speed
	self.NT_ave_speed = NT_ave_speed
    def AM_flow(self):
	return speed_to_flow(self.AB_AM_capac, tmc_ref_speed_dict[self.tmc], self.AM_ave_speed)
    def MD_flow(self):
	return speed_to_flow(self.AB_MD_capac, tmc_ref_speed_dict[self.tmc], self.MD_ave_speed)
    def PM_flow(self):
	return speed_to_flow(self.AB_PM_capac, tmc_ref_speed_dict[self.tmc], self.PM_ave_speed)
    def NT_flow(self):
	return speed_to_flow(self.AB_NT_capac, tmc_ref_speed_dict[self.tmc], self.NT_ave_speed)

# define a road link class
class Link(object):
    def __init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
                 PM_capac, NT_capac, free_flow_time, \
                 AM_flow, MD_flow, PM_flow, NT_flow):
	self.init_node = init_node
        self.term_node = term_node
        self.tmc_set = tmc_set
        self.AM_capac = AM_capac
        self.MD_capac = MD_capac
        self.PM_capac = PM_capac
        self.NT_capac = NT_capac
        self.free_flow_time = free_flow_time
        self.AM_flow = AM_flow
        self.MD_flow = MD_flow
        self.PM_flow = PM_flow
        self.NT_flow = NT_flow

# define a road link class that is a derived class of Link
class Link_with_Free_Flow_Time(Link):
    def __init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
                 PM_capac, NT_capac, free_flow_time, \
                 AM_flow, MD_flow, PM_flow, NT_flow):
	Link.__init__(self, init_node, term_node, tmc_set, AM_capac, MD_capac, \
                      PM_capac, NT_capac, free_flow_time, \
                      AM_flow, MD_flow, PM_flow, NT_flow)
	# notice that the length is in meters, and the speed is in mph; we calculate the time in minutes
	# assume free_speed = 1.5 * ref_speed
        self.free_flow_time = sum([60 * 0.000621371 * tmc_length_dict[i] / (1.5 * tmc_ref_speed_dict[i]) for i in self.tmc_set])



