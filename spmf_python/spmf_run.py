import subprocess

from spmf_configs.config_objects import Algorithm, SPMFconfigObjects


def call_spmf(SPMFconfigObjects, in_file=None, out_file=None):

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


    cmd_str = 'run ' + SPMFconfigObjects.algo_obj._name_ + ' ' + in_file + ' ' + out_file + ' ' + \
              str(SPMFconfigObjects.min_sup_val) + ' ' + str(SPMFconfigObjects.min_conf_val)

    print "(" + cmd_str + ")"

    subprocess.call(['java', '-jar', 'SPMF.jar', 'run',
                     SPMFconfigObjects.algo_obj._name_, in_file, out_file,
                     str(SPMFconfigObjects.min_sup_val), str(SPMFconfigObjects.min_conf_val)])

    # subprocess.call(['java', '-jar', 'SPMF.jar', cmd_str])



if __name__=='__main__':

    spmf_obj = SPMFconfigObjects("RuleGrowth", .5, .6)

    call_spmf(spmf_obj)