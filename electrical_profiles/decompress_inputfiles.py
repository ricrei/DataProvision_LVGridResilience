import bz2
import pickle
import _pickle as cPickle

#####################################################################
### Pickle a file and then compress it into a file with extension ###
#####################################################################
def compress_pickle(title, data):
     '''
     Method to pickle a file and then compress it into a file with extension.

     :param title: string
     :param data:  DataFrame
     '''
     with bz2.BZ2File(title, 'w') as f: 
      cPickle.dump(data, f)
     f.close()

#######################################
### Load any compressed pickle file ###
#######################################
def decompress_pickle(file):
     '''
     Method to load a compressed pickle file.

     :param file: string
     :return: DataFrame
     '''
     f = bz2.BZ2File(file, 'rb')
     data = cPickle.load(f)
     f.close()
     return data

# Example of loading a input file of thermal and electrical heat demand
data = decompress_pickle('inputdata_winter/13_hp_short.pbz2')
print(data)
