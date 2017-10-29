
from enum import Enum


class Algorithm(Enum):
    CMDeo = "CMDeo"
    CMRules = "CMRules"
    RuleGrowth = "RuleGrowth"
    ERMiner = "ERMiner"


class SPMFconfigObjects(object):

    def __init__(self, algo, min_sup_val, min_conf_val):

        self.min_sup_val = min_sup_val
        self.min_conf_val = min_conf_val

        if type(algo) == Algorithm:
            self.algo_obj = algo
        elif type(algo) == str and Algorithm(algo) is not None:
            self.algo_obj = Algorithm(algo)
        else:
            print " %% ERR: Algo missing"
            raise Exception(' %% ERR: Algorithm name or Enum is not currently supported by spmf_python')

