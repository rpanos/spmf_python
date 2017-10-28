import subprocess

from spmf_configs.config_objects import Algorithm, SPMFconfigObjects
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


    #@staticmethod
    def call_spmf(self, SPMFconfigObjects, in_file=None, out_file=None):

        # very temp - todo: give warnings or prevent overwriting or something
        if not in_file:
            in_file = '../in_file.spmf'
        if not out_file:
            out_file = 'out.txt'

        print "SPMFconfigObjects.algo_obj._name_:" + SPMFconfigObjects.algo_obj._name_

        # todo: if SPMFconfigObjects is not valid, throw error

        # java -jar spmf.jar run RuleGrowth contextPrefixSpan.txt output.txt 75% 50%
                            #run RuleGrowth in_file.spmf out.txt 0.5 0.6
        # java -jar SPMF.jar run RuleGrowth in_file.spmf out.txt 0.5 0.6


        path = os.path.abspath(__file__)


        cmd_str = 'run ' + SPMFconfigObjects.algo_obj._name_ + ' ' + in_file + ' ' + out_file + ' ' + \
                  str(SPMFconfigObjects.min_sup_val) + ' ' + str(SPMFconfigObjects.min_conf_val)

        print "(" + cmd_str + ") " + self.spmf_path

        subprocess.call(['java', '-jar',  self.spmf_path,  'run',
                         SPMFconfigObjects.algo_obj._name_, in_file, out_file,
                         str(SPMFconfigObjects.min_sup_val), str(SPMFconfigObjects.min_conf_val)])

        # subprocess.call(['java', '-jar', 'SPMF.jar', cmd_str])



if __name__=='__main__':

    spmf_obj = SPMFconfigObjects("RuleGrowth", .5, .6)

    spmf = open('SPMF.jar')
    SPMF_manager = SPMFManager(spmf)

    # SPMF_manager.call_spmf(spmf_obj)
    SPMF_manager.call_spmf(spmf_obj, in_file='../in_file.spmf', out_file='out2.txt')