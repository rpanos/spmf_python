import subprocess

from spmf_python.spmf_configs.config_objects import Algorithm, SPMFconfigObjects
import os


class SPMFManager(object):

    def __init__(self, spmf_file_handle, spmf_path=None):
        # print 'spmf_file_handle: ' + spmf_file_handle.name

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

        print "SPMFconfigObjects.algo_obj._name_:" + SPMFconfigObjects.algo_obj._name_

        # todo: if SPMFconfigObjects is not valid, throw error

        path = os.path.abspath(__file__)

        cmd_str = 'run ' + SPMFconfigObjects.algo_obj._name_ + ' ' + in_file + ' ' + out_file + ' ' + \
                  str(SPMFconfigObjects.min_sup_val) + ' ' + str(SPMFconfigObjects.min_conf_val)

        print "(" + cmd_str + ") " + self.spmf_path
        subprocess.call(['java', '-jar',  self.spmf_path,  'run',
                         SPMFconfigObjects.algo_obj._name_, in_file, out_file,
                         str(SPMFconfigObjects.min_sup_val), str(SPMFconfigObjects.min_conf_val)])




if __name__=='__main__':

    path = os.environ['PATH']
    print "path: " + str(path)

    spmf_home = os.environ['SPMF_HOME']
    print "spmf_home: " + str(spmf_home)

    spmf_obj = SPMFconfigObjects("RuleGrowth", .5, .6)

    # spmf = open('SPMF.jar')
    spmf = open('/Users/rpanos/Documents/GitHub/spmf_python/SPMF.jar')
    SPMF_manager = SPMFManager(spmf)

    # SPMF_manager.call_spmf(spmf_obj)
    SPMF_manager.call_spmf(spmf_obj, in_file='/Users/rpanos/Documents/GitHub/spmf_python/in_file.spmf',
                           out_file='/Users/rpanos/Documents/GitHub/spmf_python/spmf_data/out3.txt',
                           over_write_ouput=True)