import subprocess

from spmf_python.spmf_configs.config_objects import Algorithm, SPMFconfigObjects
import os
'''
        Pls note: This is very much in beta . .
'''

class SPMFManager(object):

    def __init__(self, spmf_file_handle, spmf_path=None):
        if spmf_file_handle and len(spmf_file_handle.name) > 0:
            self.spmf_path = spmf_file_handle.name
        elif spmf_path is not None:
            self.spmf_path = spmf_path
        else:
            self.spmf_path = 'SPMF.jar' ## no?

    def call_spmf(self, SPMFconfigObjects, in_file=None, out_file=None, over_write_ouput=False):

        # very temp - todo: give warnings or prevent overwriting or something
        if not in_file:
            in_file = '../in_file.spmf'
        if not out_file:
            out_file = 'out.txt'

        out_file_handle = open(out_file)
        if out_file_handle and len(out_file_handle.name) > 0 and not over_write_ouput:
            raise Exception('Output file Exists.  Use "over_write_ouput" option to overwrite')

        # todo: if SPMFconfigObjects is not valid, throw error

        # path = os.path.abspath(__file__)
        # cmd_str = 'run ' + SPMFconfigObjects.algo_obj._name_ + ' ' + in_file + ' ' + out_file + ' ' + \
        #           str(SPMFconfigObjects.min_sup_val) + ' ' + str(SPMFconfigObjects.min_conf_val)
        # print "(" + cmd_str + ") " + self.spmf_path

        subprocess.call(['java', '-jar',  self.spmf_path,  'run',
                         SPMFconfigObjects.algo_obj._name_, in_file, out_file,
                         str(SPMFconfigObjects.min_sup_val), str(SPMFconfigObjects.min_conf_val)])
