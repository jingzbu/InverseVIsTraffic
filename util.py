# Data Storage and Load
# These two functions "zdump" and "zload" were written by Jing Wang
# cf. https://github.com/hbhzwj/GAD/blob/master/gad/util/util.py

try:
    import cPickle as pickle
except ImportError:
    import pickle
import gzip
proto = pickle.HIGHEST_PROTOCOL

def zdump(obj, f_name):
    f = gzip.open(f_name,'wb', proto)
    pickle.dump(obj,f)
    f.close()

def zload(f_name):
    f = gzip.open(f_name,'rb', proto)
    obj = pickle.load(f)
    f.close()
    return obj


##### define classes

# define a road segment class corresponding to the original filtered shape file
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




