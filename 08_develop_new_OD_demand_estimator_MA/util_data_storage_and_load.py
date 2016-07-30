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

def dump(obj, f_name):
    f = open(f_name,'wb', proto)
    pickle.dump(obj,f)
    f.close()

def load(f_name):
    f = open(f_name,'rb', proto)
    obj = pickle.load(f)
    f.close()
    return obj

