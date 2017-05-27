
from enum import Enum


# >>> member = Color.RED
# >>> member.name
# 'RED'
# >>> member.value
# 1
class Algorithm(Enum):
    CMDeo = "CMDeo"
    CMRules = "CMRules"
    RuleGrowth = "RuleGrowth"
    ERMiner = "ERMiner"


class SPMFconfigObjects(object):

    def __init__(self, algo, min_sup_val, min_conf_val):

        self.min_sup_val = min_sup_val
        self.min_conf_val = min_conf_val

        print "algo type: " + str(type(algo))
        if type(algo) == Algorithm:
            self.algo_obj = algo
            print "YES Algorithm : " + str(self.algo_obj)
        elif type(algo) == str and Algorithm(algo) is not None:
            self.algo_obj = Algorithm(algo)
            print "YES look up Algorithm : " + str(self.algo_obj)
        else:
            print " %% ERR: Algo missing"
            # throw err?




if __name__=='__main__':

    algo1 = Algorithm.CMRules

    spmf_obj = SPMFconfigObjects(algo1, .8, .6)
    spmf_obj = SPMFconfigObjects("CMDeo", .8, .6)


